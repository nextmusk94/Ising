import numpy as np

def RndGen(n, iteration):
    x = int(iteration / 5)
    rnd = np.random.rand(iteration)
    for i in range(x):
        if rnd[i] > 0.5:
            rnd[i] = 1
        else:
            rnd[i] = -1
    for i in range(x, 2*x):
        if rnd[i] > 0.8:
            rnd[i] = 0
        elif rnd[i] <= 0.8 and rnd[i] > 0.4:
            rnd[i] = 1
        else:
            rnd[i] = -1
    for i in range(2*x, 3*x):
        if rnd[i] > 0.6:
            rnd[i] = 0
        elif rnd[i] <= 0.6 and rnd[i] > 0.3:
            rnd[i] = 1
        else:
            rnd[i] = -1
    for i in range(3*x, 4*x):
        if rnd[i] > 0.2:
            rnd[i] = 0
        elif rnd[i] <= 0.2 and rnd[i] > 0.1:
            rnd[i] = 1
        else:
            rnd[i] = -1
    for i in range(4*x, iteration):
        rnd[i] = 0
    
    return rnd



