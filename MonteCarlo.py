import math
import numpy as np
import matplotlib.pyplot as plt
from RandomGen import RndGen

# Set initial spins
def hot_start(n):
    spin = np.random.randint(0, 2, n*n)
    spin[spin == 0] = -1
    return spin

# Calculate KPI
def kpi(n, spin, coeff, N):
    ns = n*n
    kpi_temp = 0
    for i in range(8):
        if coeff[N, i] != 0:
            if i == 0:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N-n]
            elif i == 1:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N-n+1]
            elif i == 2:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N+1]
            elif i == 3:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N+n+1]
            elif i == 4:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N+n]
            elif i == 5:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N+n-1]
            elif i == 6:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N-1]
            elif i == 7:
                kpi_temp = kpi_temp + coeff[N, i] * spin[N-n-1]

    return kpi_temp

def update(n, spin, coeff, RND):
    spin_pre = np.copy(spin)
    for i in range(n*n):
        E = kpi(n, spin, coeff, i) + RND
        if E >= 0:
            spin_pre[i] = 1
        else:
            spin_pre[i] = -1
    return spin_pre

# Main Function
def Ising(n, W, iteration):
    coeff = np.loadtxt(f"./coeff_{n}x{n}.csv", delimiter=',')
    spin = hot_start(n)
    spinlog = np.zeros([iteration, n*n])
    RND = W * RndGen(n, iteration)
    KPI = np.zeros(iteration)
    for i in range(iteration):
        spin = update(n, spin, coeff, RND[i])
        spinlog[i] = spin
        for j in range(n*n):
            KPI[i] = KPI[i] + kpi(n, spin, coeff, j)
    print(f"The minimum is {np.amin(KPI)}")
    np.savetxt("spin1.csv", spinlog, fmt='%d', delimiter=',')
    plt.figure(figsize=(10, 6))
    plt.plot(KPI)
    plt.title(f"{n}x{n} Spin", fontsize=18)
    plt.xlabel('Iteration', fontsize=10)
    plt.ylabel('KPI', fontsize=10)
    plt.grid()
    plt.show()

Ising(10, 2, 3000)





