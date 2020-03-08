#Charlie Juarez
#Example retrieved from https://www.youtube.com/watch?v=oNI0rf2P9gE

def floydAlg(matrix):
    numNodes = len(matrix)
    #all use range of numNodes due to square matrices
    for k in range(numNodes):
        for i in range(numNodes):
            for j in range(numNodes):
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
    return matrix


if __name__ == "__main__":
    print('Floyd algorithm serialized test')
    input_matrix = [[0,3,99999,7],[8,0,2,99999],[5,99999,0,1],[2,99999,99999,0]]
    solved_matrix = [[0,3,5,6],[5,0,2,3],[3,6,0,1],[2,5,7,0]]
    floyd_matrix = floydAlg(input_matrix)

    #Check if the answer is correct
    numNodes = len(floyd_matrix)
    for i in range(numNodes):
        for j in range(numNodes):
            print('solved matrix['+str(i)+']['+str(j)+']='+str(solved_matrix[i][j])
            +'\tfloyd matrix['+str(i)+']['+str(j)+']='+str(floyd_matrix[i][j]))
    print('Done')
