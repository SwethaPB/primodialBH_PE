import os
os.environ["OMP_NUM_THREADS"] = "4" # export OMP_NUM_THREADS=4
os.environ["OPENBLAS_NUM_THREADS"] = "4"# export OPENBLAS_NUM_THREADS=4 
os.environ["MKL_NUM_THREADS"] = "6" # export MKL_NUM_THREADS=6
os.environ["VECLIB_MAXIMUM_THREADS"] = "4"# export VECLIB_MAXIMUM_THREADS=4
os.environ["NUMEXPR_NUM_THREADS"] = "6" # export NUMEXPR_NUM_THREADS=6


import numpy as np
import matplotlib.pyplot as plt
import bilby
result = bilby.result.read_in_result(filename='nonAcc_prior_GW170818_result.json')

#result.plot_corner(filename='prior_on_source_hand_built_corner.png',parameters=['mass_1_source','mass_1','mass_2_source','mass_2','a_1','a_2'],priors='True', labels=[r"$m1_{source}$", r"$m1_{det}$",r"$m2_{source}$", r"$m2_{det}$",r"$a1$", r"$a2$"])

result.plot_corner(filename='nonAcc_prior_GW170818_hand_built_corner.png',parameters=['mass_1_source','mass_2_source','a_1','a_2'],priors=True,labels=[r"$m1_{source}$",r"$m2_{source}$",r"$a1$", r"$a2$"])
