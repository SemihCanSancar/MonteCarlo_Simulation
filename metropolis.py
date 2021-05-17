import numpy as np
import pandas as pd
import random
import math
import geometry
import scipy.constants as sc
import pandas as pd
import matplotlib.pyplot as plt


def table(n,temp):
    ## calculating the energy table

    beta = 1/temp

    return np.exp(-beta*n)

def magn(spin_arr,nbr):
    ## calculating the magnetization

    m = 0
    for x in nbr:

        m += spin_arr[int(x)]
    
    return m


def metro(arr,temp,steps,nm,gm):

    ## geometry = gm
    ## iteration of snapshot = nm
    ## temp: temperature of the system
    ## steps: Monte Carlo steps
    ## arr: array of spins

    N = arr.shape[0]
    
    energies = []
    energy_avgs = []
    nbr = geometry.square_geom(gm)
    magnetisation = []
    
    for i in range(steps):
        if i % 1000 == 0:
            print("MCMC step: " + str(i))

        s = random.randint(0,N-1)

        ## spin flip attempt
        arr[s] = random.choice([-1,1])
        
        h = magn(arr,nbr[s])
        
        dE = 2*arr[s]*h

        ## case of not accepting 

        if dE > 0:
            
            if table(dE,temp) < random.randint(0,1):
                #print("not accepted")
                arr[s] = -arr[s]
        
        energy = geometry.energy_calc(arr,nbr)

        if i%nm==0:
            ##snapshot for plots
            energies.append(energy)
            magnetisation.append(np.abs(h))

    return energies, magnetisation,arr
