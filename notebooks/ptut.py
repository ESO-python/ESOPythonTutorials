""" a  short script with data structures from pandas"""

from numpy import loadtxt
from matplotlib.pyplot import show
from pandas import *		

ysec=loadtxt('../csp_sn/sec_max_files/y_sec_max_csp.dat', dtype='string')		
jsec=loadtxt('../csp_sn/sec_max_files/j_sec_max_csp.dat', dtype='string')	#loads files with two different sets of arrays in this example
#the j-band has fewer measurements than the y
d={}		#define two empty dictonaries to store the parameter values in
d1={}
for i in jsec:
	d[i[0]]=float(i[1])
for j in ysec:
	d1[j[0]]=float(j[1])		#makes python dictionaries out of the files 

s1=Series(ysec[:,1], index=ysec[:,0], dtype='float32')		#define a pandas series with indices given by the supernova name
s=Series(jsec[:,1], index=jsec[:,0], dtype='float32')		# same as above in j=band
d2={'y': d1, 'j':d}						# a dictionary with two columns for j and y 	
df=DataFrame(d2, columns=['j', 'y'])		#cast dictionary as dataframe, automatically assigns Nan's for no measurement
#df['flag']=df['j']>0		
df['dif']=df['j']-df['y']		#append column of differences between the two values
df.plot(kind='bar')		#plots the values in the dictionary as a bar graph with the differences as well. Useful to visualise a comparison between the
#different filters
show()		# matplotlib function to show plot
