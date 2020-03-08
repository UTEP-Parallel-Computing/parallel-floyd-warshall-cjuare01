# Parallel-Floyd-Warshall

This program creates a matrix out of each file; 'fwTestResult' and 'fwTestResult'
respectively. Which then applies the Floyd Warshall algorithm using parallelized
processes. I included a version of the algorithm using only one process in
the file, 'serialized.py', which does not use parallelized processes. The file
that does contain the parallelized version is in the file 'parallel.py'.

## How to run the programs

For the version that only uses one process can be ran with the following command:

'python3 serialized.py'

For the version that uses multiple processes, it can be ran with the following
command:

'mpiexec -n X python3 -m mpi4py parallel.py'

Where 'X' is the number of processes you choose to run the program with.

## Results

Using the 'parallel.py' file the following results yield their respective timed
results:

'mpiexec -n 1 python3 -m mpi4py parallel.py' averages at around .68 seconds

'mpiexec -n 2 python3 -m mpi4py parallel.py' averages at around .35 seconds

'mpiexec -n 4 python3 -m mpi4py parallel.py' averages at around .18 seconds

'mpiexec -n 8 python3 -m mpi4py parallel.py' time for this was indefinite
