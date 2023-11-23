#IMPORTS

import numpy as np
from POD import POD
from plots import *
import matplotlib.pyplot as plt


def load(location,plot = False,verbosity=0):
    if verbosity>0:
        print("Loading Data")
    tstart = 0
    tend = 201

    xs = np.loadtxt(location+'xs.dat')
    times = np.loadtxt(location+'times.dat')
    data = np.loadtxt(location+'data.dat')

    xlen = data.shape[0]
    time_len = data.shape[1]
            
    dx = xs[1]-xs[0]
    dt = times[1]-times[0]

    L = xs[-1]+dx

    data = data[:,tstart:tend]
    times = times[tstart:tend]

    # POD

    k = 4 # number of modes

    spatial, temporal = POD(data,k)

    if plot:
        # Visualize Data
        plot_solution(data,xs,times)
        plt.figure(2)
        plot_temporal(temporal,times,k)
        plt.figure(3)
        plot_spatial(spatial,xs,k)
        plt.show()
        
    if verbosity>0:
        print("spatial.shape: ", spatial.shape)
        print("temporal.shape: ", temporal.shape)
        print("times.shape: ", times.shape)
        print("xs.shape: ", xs.shape)

    return(spatial, temporal,times,xs)