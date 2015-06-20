import matplotlib 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy.spatial
import math
import numpy as np

def plot_points(p, pstar=[], rstar=0.):
    n= len(pstar)
    k= len(p)
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.plot(  p[:,0], p[:,1], 'b*')
    
    if len(pstar)>0:
        
        ax.plot(  pstar[0], pstar[1], 'r.')

        c = mpatches.Circle( pstar,  rstar ,  fc="w", ec="r", lw=1.5)
        ax.add_patch(c)

        hull= scipy.spatial.ConvexHull(p)
        for simplex in hull.simplices:
            plt.plot(p[simplex,0], p[simplex,1], 'g*--', lw=1.5)
 
        rindx=0
        for indx,pp in enumerate(p):
            d = np.linalg.norm(pstar - pp)
            if math.fabs(d-rstar )<1e-06:
                ax.plot( pp[0], pp[1], 'go')
                rindx=indx
                
        plt.plot([pstar[0],p[rindx,0]], [pstar[1], p[rindx,1]], 'r--', lw=2.5)
        
    plt.show()
 
