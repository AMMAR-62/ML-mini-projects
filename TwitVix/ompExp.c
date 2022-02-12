#include <omp.h>
#include <stdio.h>
int main(int *args, char *args[]){
    // specify the block to be executed in the parallel way
    #pragma omp parallel //compiler directive
    // print hello world from thread.
    printf("Hello World");
    return 0;
}

/**
 * gcc fopenmp hello-world
 * ./a.out
 * by default considered two threads.
 */