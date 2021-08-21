#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def plot_rdf(filename):
	data = []
	with open(filename,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if '#' not in line and len(line.split())==4:
					data.append([float(line.split()[1]),float(line.split()[2]),float(line.split()[3])])
	data = np.array(data)
#	print(data[:,0],data[:,1])
	f,ax = plt.subplots(figsize=(8,5))
#	
	ax.plot(data[:,0],data[:,1],label='$g(r)$')
#
	xmin,xmax = min(data[:,0]), max(data[:,0])
	ymin,ymax = min(data[:,1]), max(data[:,1])

	ax.set_xlim(0,round(xmax))
	ax.set_ylim(-0.2,round(ymax+1))

	ax.xaxis.set_tick_params(labelsize=16)
	ax.yaxis.set_tick_params(labelsize=16)

	ax.set_xlabel('$r~(\AA)$',fontsize=18,fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	ax.set_ylabel('$g(r)$',fontsize=18,fontfamily='sans-serif',fontstyle='italic',labelpad=10)

	plt.legend(fontsize=16,loc='best')
	plt.tight_layout()

	plt.savefig('output.png',dpi=800)
#	print(data)


if __name__ == '__main__':
	filename = 'fcc-rdf.dat'
	plot_rdf(filename)


