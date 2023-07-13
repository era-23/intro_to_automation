from numpy import *

import matplotlib.pyplot as plt

def flux_surface(A = 2.2, kappa = 1.5, delta = 0.3, R0 = 2.5):
    """Make a flux surface

    Arguments
    ---------
    parameter:
        The maths parameter
        ....
    """
    
    theta = linspace(0, 2 * pi)
    r = R0 / A
    R_s = R0 + r * cos(theta + (arcsin(delta) * sin(theta)))
    Z_s = kappa * r * sin(theta)
    return R_s, Z_s
    
def plot_surface(R_s, Z_s):
    """Plot a flux surface

    Arguments
    ---------
    parameter:
        The maths parameter
        ....
    """
    
    plt.plot(R_s, Z_s)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    plt.savefig("miller.png")
    
def main():
    r, z = flux_surface() 
    plot_surface(r, z)

if __name__ == "__main__":
    main()
