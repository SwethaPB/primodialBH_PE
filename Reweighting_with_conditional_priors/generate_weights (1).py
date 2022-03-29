from __future__ import division, print_function
from __future__ import division, print_function
import os
os.environ["OMP_NUM_THREADS"] = "4" # export OMP_NUM_THREADS=4
os.environ["OPENBLAS_NUM_THREADS"] = "4"# export OPENBLAS_NUM_THREADS=4 
os.environ["MKL_NUM_THREADS"] = "6" # export MKL_NUM_THREADS=6
os.environ["VECLIB_MAXIMUM_THREADS"] = "4"# export VECLIB_MAXIMUM_THREADS=4
os.environ["NUMEXPR_NUM_THREADS"] = "6" # export NUMEXPR_NUM_THREADS=6
import pandas as pd
import numpy as np
df=pd.read_csv("AccPriorTable.csv")
df1=df.round(3)
#187.68,85.8889,0.825,0.175,0
#Index_label = df1[(df1['m1']==187.6800) & (df1['m2']==85.8889) & (df1['a1']==0.8250) & (df1['a2']==0.1750)].index.tolist()

df_test=pd.read_csv("Acc_gw170818_sample_point.csv")


weight=[]
for i in df_test.index:
	M1=df_test['mass1'][i]
	M2=df_test['mass2'][i]
	A1=df_test['spin1'][i]
	A2=df_test['spin2'][i]

	M1Closest = df1.iloc[(df1['m1']-M1).abs().argsort()[:1]]['m1'].tolist()
	M2Closest = df1.iloc[(df1['m2']-M2).abs().argsort()[:1]]['m2'].tolist()
	A1Closest = df1.iloc[(df1['a1']-A1).abs().argsort()[:1]]['a1'].tolist()
	A2Closest = df1.iloc[(df1['a2']-A2).abs().argsort()[:1]]['a2'].tolist()
	Index_label = df1[(df1['m1']==M1Closest[0]) & (df1['m2']==M2Closest[0]) & (df1['a1']==A1Closest[0]) & (df1['a2']==A2Closest[0])].index.tolist()
	#print(i)
	#print(Index[0])
	#Index=Index_label[0]+2
	#print(i)
	#print(Index_label)
	print(df1['we'][Index_label[0]])
	weight=np.append(weight,df1['we'][Index_label[0]])

print("Shape of the weight")
print(np.shape(weight))
#print(weight)

np.savetxt("Fake2_new_weight_gw170818.csv", weight, delimiter=",")
#df_test=pd.read_csv("fool_with_heading.csv")

