import numpy as np

def latticeneg(n):
    coeff = np.zeros([n*n, 8])
    for i in range(n):
        for j in range(n):
            coeff[i*n+j,0] = -1
            coeff[i*n+j,2] = -1
            coeff[i*n+j,4] = -1
            coeff[i*n+j,6] = -1
    return coeff

def setzero(n, coeff):
    for i in range(n):
        for j in range(n):
            if i == 0:
                coeff[i*n+j,0] = 0
                coeff[i*n+j,1] = 0
            if j == n-1:
                coeff[i*n+j,1] = 0
                coeff[i*n+j,2] = 0
                coeff[i*n+j,3] = 0
            if i == n-1:
                coeff[i*n+j,3] = 0
    return coeff

def Four2Eight(n, coeff_row):
    ns = n*n
    coeff = np.zeros([ns, 8])
    for i in range(ns):
        coeff[i, 0] = coeff_row[i, 0]
        coeff[i, 1] = coeff_row[i, 1]
        coeff[i, 2] = coeff_row[i, 2]
        coeff[i, 3] = coeff_row[i, 3]
        if i >= n*(n-1):
            coeff[i, 4] = 0
        else:
            coeff[i, 4] = coeff_row[i+n, 0]
        if i % n == 0 or i >= n*(n-1):
            coeff[i, 5] = 0
        else:
            coeff[i, 5] = coeff_row[i-5, 1]
        if i % n == 0:
            coeff[i, 6] = 0
        else:
            coeff[i, 6] = coeff_row[i-1, 2]
        if i < n or i % n == 0:
            coeff[i, 7] = 0
        else:
            coeff[i, 7] = coeff_row[i-7, 3]

    return coeff

def CoeffGen(n):
    coeff = latticeneg(n)
    coeff = setzero(n, coeff)
    coeff = Four2Eight(n, coeff)
    np.savetxt(f"coeff_{n}x{n}.csv", coeff, fmt='%d', delimiter=',')

CoeffGen(10)
