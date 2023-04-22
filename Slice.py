import numpy as np
import time

n = 1000
A = np.random.randint(0, 10, size = (n,n))
B = np.random.randint(0, 10, size = (n,n))
#print("A is",A)
#print("B is",B)

start_time = time.time()
C = np.matmul(A,B)
print("time for numpy is", (time.time()-start_time))
#print(A[1:n,1:n])


def SliceMatMul(A_prime, B_prime):
    C_prime = []
    C_prime = np.empty((n, n))    
    for i in range(n):
        for j in range(n):
            #for k in range(n):
                #C_prime[i][j] = A_prime[i][k] * B_prime[k][j] + C_prime[i][j]
            C_prime[i][j] = np.matmul(A_prime[i], B_prime[:,j])
    return C_prime
    

start_time = time.time()
C = SliceMatMul(A,B)
#print(SliceMatMul(A,B))
print("time for slice is", (time.time()-start_time))