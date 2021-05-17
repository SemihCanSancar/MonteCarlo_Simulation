import numpy as np
from random import *
import pandas as pd


def spin_array(N,file):
    ## function to print certain amount of random spins
    ## could not use lagged fibonacci number generator
    ## using random library instead

    l = []
    spins = open(file,"w")
    spins.write("spins \n")
    for _ in range(N):

        spin = choice([-1,1])
        l.append(spin)
        spins.write("%s \n"%(spin))

    spins.close()


spin_array(400,"400.txt")