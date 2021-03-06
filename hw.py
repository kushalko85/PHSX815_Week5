import numpy as np 
import sys
import matplotlib.pyplot as plt 

def myfunc(x):
	return np.sin(x)*np.sin(x)
def plot(x,bin_width):
	return bin_width*myfunc(x)


myx = np.arange(0,3.14,0.1)
myy = myfunc(myx)



listx=[]
nsample = 100000

for  i in range (nsample):
	x = np.random.uniform(0,3.14)
	#print ("x",x)
	y = np.random.uniform(0,1)
	#print ("y",y)
	#print ("func", myfunc(x))
	if y<myfunc(x):
		listx.append(x)
wt = np.ones_like(listx)/len(listx)
print(wt[0])
n= plt.hist(listx, bins = 1000)
bin_width = n[1][1]-n[1][0]
print ("bin_width", bin_width)
scaled = list(map(plot,myx,np.ones_like(myx)*bin_width))
plt.plot(myx,scaled)

plt.show()