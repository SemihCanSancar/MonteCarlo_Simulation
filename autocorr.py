import numpy as np
import metropolis
import binning
import pandas as pd
import matplotlib.pyplot as plt


## computing the autocorrelation function
def autocorr(x):
    kappa = 2000
    n = len(x)
    variance = np.var(x)
    mean = np.mean(x)

    x = x - mean
    r = np.correlate(x,x,mode="full")[-n:]
    res = r/(variance*np.arange(n,0,-1))

    return res[0:kappa]

## calculating the autocorrelation time
def tau(x):
    auto_corr = autocorr(x)
    t = 1+ 2*np.sum(auto_corr)
    return int(t)
    
