import numpy as np
import math
import pandas as pd
import metropolis as met
import matplotlib.pyplot as plt


## function to divide array into a number of bins

def binning_method(array):
    means = []
    vars = []
    serror = []
    energie_means = []
    energie_vars = []
    energie_serr = []

    for i in range(8):

        new_array = np.array_split(array,2**i)

        for j in range(len(new_array)):
            ## calculating the mean of certain bin and appending it to a list
            mean = np.mean(new_array[j])
            means.append(mean)
            
            ## calculating the means, vars and stat errors of the usable bins and appending
            ## it to another list
            energie_means.append(np.mean(means))
            energie_vars.append(np.var(energie_means))
            energie_serr.append(np.sqrt(energie_vars[-1]))
            
            
    return energie_means,energie_vars,energie_serr
