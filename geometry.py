import numpy as np
import math
import pandas as pd
import random


def magn_calc(s):
    ## defining the magnetization and energy function

    return np.sum(s)

def energy_calc(s,nbr):
    ## calculating the energies with the spin array (s) and the list of nearest neighbors (nbr)

    E = 0
    for i in range(s.shape[0]):
        E_in = 0
        for k in range(nbr.shape[1]):
            j = int(nbr[i][k])
            E_in += s[j]

        E += s[i]*E_in

    return -0.5*E

def shift_array(L):
    # function for the shift array and the nearest neighbours


    in_sh = np.zeros((2,L))
    i = 0
    for j in range(0,L):
        in_sh[0][j] = i -1
        in_sh[1][j] = i +1
        i += 1
    in_sh[0][0] = L-1
    in_sh[1][L-1] = 0

    return in_sh


def square_geom(L):
    ## function that returns the square geometry of the array with its nearest neighbours

    nbr = np.zeros((L*L,4))
    j = 0
    sh = shift_array(L)
    
    for iy in range(0,L):
        for ix in range(0,L):

            nbr[j][0] = sh[1][ix] + L*(iy) 
            nbr[j][1] = sh[0][ix] + L*(iy)
            nbr[j][2] = ix + L*(sh[1][iy]) 
            nbr[j][3] = ix + L*(sh[0][iy])

            j += 1
            
    return nbr
