#Charlie Juarez

from mpi4py import MPI
import time
import sys

#Create a matrix from the file specified
def retrieveMatrix(file):
    file = open(file, 'r')
    lines = file.readlines()
    matrix = []

    #Each line is a row for the matrix
    for i in range(len(lines)):
        matrix.append(lines[i].split())

    file.close()
    return matrix

if __name__ == "__main__":
    print('Floyd algorithm parallel test')

    #Get the world communicator
    worldcomm = MPI.COMM_WORLD

    #Create the matrices
    input_matrix = retrieveMatrix('fwTest.txt')
    solved_matrix = retrieveMatrix('fwTestResult.txt')

    #The following was put together from in class discussion
    numNodes = len(input_matrix)
    rows_per_thread = numNodes//worldcomm.Get_size()
    thread_per_thread = worldcomm.Get_size()/numNodes
    startrow = rows_per_thread*worldcomm.Get_rank()
    endrow = rows_per_thread*(worldcomm.Get_rank() + 1)

    if worldcomm.Get_rank() == 0:
        print('Starting Floyd algorithm')

    start_time = time.time()

    #Floyd algorithm
    for k in range(numNodes):
        #Division of work
        input_matrix[k] = worldcomm.bcast(input_matrix[k],
                                            root=int(thread_per_thread*k))
        for i in range(startrow, endrow):
            for j in range(numNodes):
                input_matrix[i][j] = min(int(input_matrix[i][j]),
                                int(input_matrix[i][k])+int(input_matrix[k][j]))

    #Put together work done by each rank
    if worldcomm.Get_rank() == 0:
        for k in range(endrow, numNodes):
            rankofK = int((worldcomm.Get_size()/numNodes)*k)
            input_matrix[k] = worldcomm.recv(source=rankofK, tag=42)

        #Check if the result of input is same as the one on file
        for i in range(numNodes):
            for j in range(numNodes):
                input = input_matrix[i][j]
                solved = int(solved_matrix[i][j])
                """
                #Tried printing but it would cause a buffer issue it seems
                #Prints only some and then stops
                print('input matrix['+str(i)+']['+str(j)+']='+str(input_matrix[i][j])
                  +'\tsolved matrix['+str(i)+']['+str(j)+']='+solved_matrix[i][j])
                """

                if input != solved:
                    sys.exit("Error: mismatch at row:"+str(i)+" column:"+str(j))
        end_time = time.time()
        final_time = end_time - start_time
        print()
        print('Done in '+str(final_time)+' seconds')
    else:
        #Send work done by each process to rank=0
        for k in range(startrow, endrow):
            worldcomm.send(input_matrix[k], dest=0, tag=42)
