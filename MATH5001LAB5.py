'''Math 5001 Lab 5 Quinlin Neuhaus'''
import numpy as np
from matplotlib import pyplot as plt

def normvar(n):
    '''returns variance of means of rows of nxn array of random normal variables'''
    return np.var(np.random.normal(size=(n,n)).mean(axis=1))

def plotnorm():
    '''plots normvar() output for 10 steps 100-1000'''
    plt.plot(np.array([normvar(n) for n in range(0, 1001, 100)]))
    plt.show()

def plottrig():
    '''plots sin, cos, and arctan on the same graph'''
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y = np.sin(x)
    z = np.cos(x)
    w = np.arctan(x)
    plt.plot(x,y)
    plt.plot(x,w)
    plt.plot(x,z)
    plt.show()

def plotrat():
    '''plots 1/x-1 on (-2,6) accounting for the discontinuity'''
    x1 = np.linspace(-2, .9, 30)
    x2 = np.linspace(1.1, 6, 50)
    plt.plot(x1, 1 / (x1 - 1), "m--", linewidth=4)
    plt.plot(x2, 1 / (x2 - 1), "m--", linewidth=4)
    plt.xlim(-2, 6)
    plt.ylim(-6, 6)
    plt.show()

def plotsin():
    '''plots 4 transformations of sin in a 2x2 subplot'''
    x = np.linspace(0, 2 * np.pi)
    plt.subplot(221)
    plt.plot(x, np.sin(x), "g-")
    plt.title("Sin(x)")
    plt.axis([0, 2*np.pi, -2, 2])
    plt.subplot(222)
    plt.plot(x, np.sin(2*x), "r--")
    plt.title("Sin(2x)")
    plt.axis([0, 2*np.pi, -2, 2])
    plt.subplot(223)
    plt.plot(x, 2* np.sin(x), "b--")
    plt.title("2Sin(x)")
    plt.axis([0, 2*np.pi, -2, 2])
    plt.subplot(224)
    plt.plot(x, 2 * np.sin(2 * x), "m:")
    plt.title("2Sin(2x)")
    plt.axis([0, 2*np.pi, -2, 2])
    plt.suptitle("Various Sin Transformations")
    plt.show()

def FARS():
    '''loads and FARS data set, then plot longitude and latitutde on a scatterplot'''
    data = np.load("FARS.npy")
    plt.plot(data[:, 1], data[:, 2], "k,")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.axis("equal")
    plt.show()
    plt.hist(data[:,0], bins=np.arange(0,25))
    plt.xlabel("Hours")
    plt.show()

def plot3d():
    '''plots a heatmap and contourmap of sin(x)sin(y)/xy with nondefault colors and the colorbar'''
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    y = x.copy()
    X, Y = np.meshgrid(x,y)
    Z = np.sin(X) * np.sin(Y) / (X * Y)
    plt.subplot(121)
    plt.pcolormesh(X, Y, Z, cmap="coolwarm")
    plt.colorbar()
    plt.xlim(-2 * np.pi, 2 * np.pi)
    plt.ylim(-2 * np.pi, 2 * np.pi)
    plt.subplot(122)
    plt.contour(X,Y,Z, 15, cmap="coolwarm")
    plt.colorbar()
    plt.xlim(-2 * np.pi, 2 * np.pi)
    plt.ylim(-2 * np.pi, 2 * np.pi)
    plt.show()

