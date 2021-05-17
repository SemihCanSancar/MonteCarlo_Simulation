import numpy as np
import binning
import pandas as pd
import metropolis
import geometry
import matplotlib.pyplot as plt
import autocorr


## PLOTTING the results from the metropolis algorithm + binning method

taus = []

report = open("report.txt",'w')

## nearest neigbour: nr = L
nr = 20
timesteps = 10**4
snaps = 10

temps = [2.0,2.27,2.6]

## stat. error per temperature lists
serr_temps_E = [[],[],[]]
serr_temps_M = [[],[],[]]
i = 0


## reading files
x = pd.read_csv("400.txt").to_numpy()
x = np.concatenate(x,axis=0)


## iteration over the temperatures
for temp in temps:

    energies,magnetisation,_  = metropolis.metro(x,temp,timesteps,snaps,nr)
    
    iac = autocorr.autocorr(energies)
    tau = autocorr.tau(energies)
    taus.append(tau)


    mean_E, vars_E, serror_E = binning.binning_method(np.array(energies))
    mean_M, vars_M, serror_M = binning.binning_method(np.array(magnetisation))

    serr_temps_E[i].append(serror_E)
    serr_temps_M[i].append(serror_M)
    i = i+1
    
    plt.figure(1)
    plt.xlabel("number of bins")
    plt.ylabel("energy")
    plt.title("First 30k datapoints Energy - Energy")
    plt.plot(mean_E[:10**3],color="green",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_energy30_mean_10k.png"%(temp))
    plt.close()

    plt.figure(2)
    plt.xlabel("number of bins")
    plt.ylabel("energy var")
    plt.title("First 30k datapoints - variance energy")
    plt.plot(vars_E[:10**3],color="red",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_energy30_var_10k.png"%(temp))
    plt.close()

    plt.figure(3)
    plt.xlabel("number of bins")
    plt.ylabel("energy serr")
    plt.title("First 30k datapoints - stat. error Energy")
    plt.plot(serror_E[:10**3],color="black",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_energy30_err_10k.png"%(temp))
    plt.close()

    plt.figure(4)
    plt.xlabel("number of bins")
    plt.ylabel("|M|")
    plt.title("First 30k datapoints - mean Magn")
    plt.plot(mean_M[:10**3],color="green",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_magn30_mean_10k.png"%(temp))
    plt.close()

    plt.figure(5)
    plt.xlabel("number of bins")
    plt.ylabel("magn var")
    plt.title("First 30k datapoints - var Magn")
    plt.plot(vars_M[:10**3],color="red",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_magn30_var_10k.png"%(temp))
    plt.close()

    plt.figure(6)
    plt.xlabel("number of bins")
    plt.ylabel("magn serr")
    plt.title("First 30k datapoints - stat. error Magn")
    plt.plot(serror_M[:10**3],color="black",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_magn30_err_10k.png"%(temp))
    plt.close()

    plt.figure(7)
    plt.xlabel("number of bins")
    plt.ylabel("energy mean")
    plt.title("energy")
    plt.plot(mean_E,color="green",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_energy50_mean_10k.png"%(temp))
    plt.close()

    plt.figure(8)
    plt.xlabel("number of bins")
    plt.ylabel("energy var")
    plt.title("variance energy")
    plt.plot(vars_E,color="red",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_energy50_var_10k.png"%(temp))
    plt.close()

    plt.figure(9)
    plt.xlabel("number of bins")
    plt.ylabel("energy serr")
    plt.title(" stat error energy")
    plt.plot(serror_M,color="black",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_energy50_err_10k.png"%(temp))
    plt.close()

    plt.figure(10)
    plt.xlabel("number of bins")
    plt.ylabel("|M|")
    plt.title("Magn")
    plt.plot(mean_M,color="green",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_magn50_mean_10k.png"%(temp))
    plt.close()

    plt.figure(11)
    plt.xlabel("number of bins")
    plt.ylabel("magn var")
    plt.title("variance Magn")
    plt.plot(vars_M,color="red",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_magn50_var_10k.png"%(temp))
    plt.close()

    plt.figure(12)
    plt.xlabel("number of bins")
    plt.ylabel("magn serr")
    plt.title("stat error Magn")
    plt.plot(serror_M,color="black",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_magn50_err_10k.png"%(temp))
    plt.close()
    
    plt.figure(13)
    plt.xlabel("number of bins")
    plt.ylabel("<E>/N")
    plt.title("Energy per spin")
    plt.plot(np.array(mean_E)/nr**2,color="black",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_NBR_%i_err_10k.png"%(temp,nr))
    plt.close()

    plt.figure(14)
    plt.xlabel("number of bins")
    plt.ylabel("<M>/N")
    plt.title("Magn per spin")
    plt.plot(np.array(mean_M)/nr**2,color="black",label=r"temp: %.2f"%(temp))
    plt.legend()
    plt.savefig(r"T_%.2f_NBR_%i_err_10k.png"%(temp,nr))
    plt.close()
    
    report.write("Temperatur: %.2f \n"%(temp))
    report.write("Autocorrelation time: %.2f \n"%(temp))
    report.write("<E>/L^2: %.7f +/- %.7f \n"%(mean_E[-1]/nr**2,serror_E[-1]/nr**2))
    report.write("<M>/L^2: %.7f +/- %.7f \n\n"%(abs(mean_M[-1])/nr**2,serror_M[-1]/nr**2))
    
    print("Temperature: " + str(temp))
    print("Autocorrelation time: " + str(taus))
    print("<E>/L^2: %.7f +/- %.7f "%(mean_E[-1]/nr**2,serror_E[-1]/nr**2))
    print("<M>/L^2: %.7f +/- %.7f "%(abs(mean_M[-1])/nr**2,serror_M[-1]/nr**2))
    

report.close()

plt.figure(15)
plt.xlabel("number of bins")
plt.ylabel("serror")
plt.title("stat error (M) wrt. temp, with nbr=100")
plt.plot(serr_temps_M[0][0],color="black",label="temp: 2.0")
plt.plot(serr_temps_M[1][0],color="green",label="temp: 2.27")
plt.plot(serr_temps_M[2][0],color="blue",label="temp: 2.6")
plt.legend()
plt.savefig("100_temp_serrors_100nbr.png")
plt.close()

plt.figure(16)
plt.xlabel("number of bins")
plt.ylabel("serror")
plt.title("stat error (E) wrt. temp, with nbr=100")
plt.plot(serr_temps_E[0][0],color="black",label="temp: 2.0")
plt.plot(serr_temps_E[1][0],color="green",label="temp: 2.27")
plt.plot(serr_temps_E[2][0],color="blue",label="temp: 2.6")
plt.legend()
plt.savefig("100_temp_serrors_100nbr.png")
plt.close()