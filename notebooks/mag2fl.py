""" the script uses pandas Panel functionality to store mutliband light curves in a convenient way

for the purposes of the pandas functions, only the class 'conv' is useful esp., the function df_crt

"""

from numpy import log10, loadtxt, linspace, delete, array, pi, trapz, vstack, ones, linalg
from pandas import *
from matplotlib.pyplot import show, plot
from scipy.interpolate import interp1d
from scipy.stats import pearsonr

import math
import sys
h='../pap_files/CSP_Photometry_DR2/'
tl='opt+nir_photo.dat'
disf=loadtxt('csp_dist.txt', dtype='string')
#decl=loadtxt('../tests_paper/ni/files_snpy/tmax_dm15.dat', dtype='string')
obj=sys.argv[1]
#filt=sys.argv[2]
#zp=6.322e-11
wsset=loadtxt('../tests_paper/csp_sn/sec_max_files/y_sec_max_csp.dat', dtype='string')	
tmax=loadtxt('../tests_paper/ni/files_snpy/tmax_dm15.dat', dtype='string')

class conv:					#class reads in the dat file and stores it as a python dictionary. the second function							#converts dicts to a panel after converting them to dataframes
	def rd_lc(self, sn, band):	#using usual python file i/o, the function stores a light curve as a dictionary
		f=open(h+sn+tl, 'r')	#reads complete file (with redshift, coordinate information)
		f1=loadtxt(h+sn+tl, skiprows=5)	#reads in only the	light curve values  
		ls=[]
		for row in f:
			ls.append(row.split())
		ind=ls[4].index(band)		#the row in the file with filter id's 
		lc={}	#define empty dictionaries 
		lc['MJD']=f1[:,0][f1[:,ind]<90]		#store mjd's
		lc[band]=f1[:,ind-1][f1[:,ind]<90]	#store magnitudes
		lc['e_'+band]=f1[:,ind][f1[:,ind]<90]		#store magnitude errors
		return lc
	def f_ord(self, sn):		#uses the file currently read in using the object (supernova) name to obtain filter order
		e=open(h+sn+tl, 'r')
		ls=[]
		for row in e:
			ls.append(row.split())
		ind=ls[4].index(ls[4][3])
		s=array(ls[4])
		aub=s[(s != s[3]) & (s !='MJD') & (s!='#')]		#extracts that filter order from the file. 
		return aub
		
	def df_crt(self, sn, bands):	#creates a pandas panel
		data={}		#define empty dictionary
		for i in bands:
			data[i]=DataFrame(self.rd_lc(sn, i))		#casts each filter's light curve as a dataframe.
		pn=Panel(data)	#uses panel function to store different filters. stores nan's for mjd's with no observations in the given filter    
		return pn
class m2f:
	def dm(self, sn):
		return float(disf[disf[:,0]==sn][0][1])
	def spl_fit(self, sn, band):
		lc1=conv().rd_lc(sn, band)
		mjd=lc1['MJD']
		b=lc1[band]
		l=linspace(min(mjd), max(mjd), 100)
		sp=interp1d(mjd, b, kind='cubic')
		gp=sp(l)
		return l[gp==min(gp)], min(gp)
	def mag2f(self, obj, filt):				
		tm, mm=self.spl_fit(obj,filt)
		wv=wvarr[bands==filt]
		print obj
		absm=mm-self.dm(obj)
		zp=zparr[bands==filt]
		apfl=wv*zp*pow(10, mm/2.5)*1e-9
		dist=self.dm(obj)#pow(10, (self.dm(obj)-25)/5.0)*3.08e18
		lbol=apfl*4*pi*(dist**2)
		#lbol=pow(10, (5.48-absm)/2.5)
		return lbol, absm
	def slp(self, arr1, arr2):
		arr3=arr1[(arr1>40) & (arr1<90)]
		arr4=arr2[(arr1>40) & (arr1<90)]
		a=vstack([arr3, ones(len(arr4))]).T
		m=linalg.lstsq(a, arr4)[0]
		return m
	#def trap(self, snar, wvarr):
		#return (sum(snar)*2-snar[0])*(wvarr[-1]-wvarr[0])/4.0

ar=[]
ar1=[]
for obj in wsset[:,0]:
	try:
		lc1=conv().rd_lc(obj, 'Y')
		ph=lc1['MJD']-float(tmax[tmax[:,0]==obj][0][1])
		t2=float(wsset[wsset[:,0]==obj][0][1])
		mag=lc1['Y']
		mu=float(disf[disf[:,0]==obj][0][1])
		u=m2f().slp(ph, mag)
		m5=u[0]*(t2+25)+u[1]
		print u
		if u[0]<0.1:
			ar.append(m5-mu)
			ar1.append(float(tmax[tmax[:,0]==obj][0][3]))
	except:
		obj
ar=array(ar)
ar1=array(ar1)
print pearsonr(ar, ar1), len(ar)
'''
#
#plot(lc1['MJD'], lc1['B'], 'r.')
#show()
wvarr=array([4330, 5456, 6156, 7472])
zparr=array([6.32, 3.63, 2.17, 1.13 ])
bands=array(['B'])#, 'V', 'r', 'i'])
bfl=[]
dmarr=[]
#for k in wsset:
#	if k in disf[:,0]:	
	#	snar=array([m2f().mag2f(k, i) for i in bands])
	#	bfl.append(m2f().trap(snar, wvarr)[0])
		#dmarr.append(float(decl[decl[:,0]==k][0][3]))		
	
bfl=[m2f().mag2f(i, 'B') for  i in wsset]
#r=[float(decl[decl[:,0]==k][0][3]) for i in wsset]
bfl=array(bfl)
print pearsonr(bfl[:,0], bfl[:,1]) #dmarr, #pearsonr(bfl, dmarr)
#tr=trapz(snar, wvarr)
 #pearsonr(arr[:,0], arr[:,1])#, 5.006743e-44*lb+3.4823e-87
#print m2f().spl_fit(obj, filt), conv().f_ord(obj)
'''
