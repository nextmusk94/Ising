import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt

n = 10
plotx = 2
ploty = 20
spin = np.loadtxt('./spin1.csv', delimiter=',')

spinplot = np.zeros([plotx*ploty, n, n])
for i in range(plotx):
    for j in range(ploty):
        spinplot[i*ploty+j] = np.zeros([n,n])

for x in range(plotx*ploty):
    for i in range(n):
        for j in range(n):
            spinplot[x,i,j] = spin[x, i*n+j]

# create discrete colormap
cmap = colors.ListedColormap(['red', 'blue'])
bounds = [-2, 0, 2]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots(plotx, ploty, tight_layout=True)
for i in range(plotx):
    for j in range(ploty):
        ax[i,j].set_title(f"{i*ploty+j}", fontsize=12)
        ax[i,j].imshow(spinplot[i*ploty+j], interpolation='none', cmap=cmap, extent=[0, n, 0, n], norm=norm, zorder=0)
    
#draw gridlines1
for x in range(n + 1):
    for i in range(plotx):
        for j in range(ploty):
            ax[i,j].axhline(x, lw=1, color='k', zorder=5)
            ax[i,j].axvline(x, lw=1, color='k', zorder=5)
            ax[i,j].axis('off')

plt.show()