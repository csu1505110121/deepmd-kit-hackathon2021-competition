#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


def load_data(filenanme):
	dpspace = []
	with open(filename,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				data = [float(x) for x in line.split()]
				#print(len(data))
				data = np.array(data)
				#data.reshape(1200,-1)
				data = data.reshape(-1,1200)
				#print(data.shape)
				dpspace.append(data)
	dpspace = np.concatenate(dpspace,axis=0)
	#print(dpspace)
	return dpspace

def _pca(data,n_components=10):
	pca = PCA(n_components=n_components)
	pca.fit(data)
	_variance_ratio = pca.explained_variance_ratio_
	_variance = pca.explained_variance_
	data_trans = pca.transform(data)
	
	return data_trans,_variance_ratio, _variance

def _kmeans(data,n_clusters=6):
	clf = KMeans(n_clusters=n_clusters)
	clf.fit(data)
	centers = clf.cluster_centers_
	labels = clf.labels_

	return centers, labels


if __name__ == '__main__':
	filename = 'doutput.dat'
	data = load_data(filename)
	
	#f,ax = plt.subplots()
	data_trans, _variance_ratio, _variance = _pca(data)
	print(data_trans, _variance_ratio, _variance)

	# plot the pca ratio
	f, ax = plt.subplots(figsize=(8,5))
	ax.plot([x+1 for x in range(len(_variance_ratio))],_variance_ratio,'o-')

	ax.xaxis.set_ticks(np.arange(1,10.1,2))

	ax.xaxis.set_tick_params(labelsize=16)
	ax.yaxis.set_tick_params(labelsize=16)

	ax.set_xlabel('PCA',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	ax.set_ylabel('Ratio',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	plt.tight_layout()
	plt.savefig('pca.png',dpi=500)
	#plt.show()

	# plot 3d
	data_center, _labels = _kmeans(data_trans)
	fig = plt.figure()
	ax1 = fig.add_subplot(111,projection='3d')
	#f1,ax1 = plt.subplots(figsize=(8,5))
	ax1.scatter(data_trans[:,0],data_trans[:,1],data_trans[:,2],c=_labels)

	ax1.set_xlabel('PC 1',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	ax1.set_ylabel('PC 2',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	ax1.set_zlabel('PC 3',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	
	ax1.set_xlim(-1,1)
	ax1.set_ylim(-0.1,1)
	ax1.set_zlim(-0.2,0.2)
	
	ax1.xaxis.set_ticks(np.arange(-1,1.1,0.5))
	ax1.yaxis.set_ticks(np.arange(-0.1,1.1,0.3))
	ax1.zaxis.set_ticks(np.arange(-0.2,0.21,0.1))

	ax1.xaxis.set_tick_params(labelsize=16)
	ax1.yaxis.set_tick_params(labelsize=16)
	ax1.zaxis.set_tick_params(labelsize=16)
	plt.tight_layout()
	plt.savefig('3d.png',dpi=500)
	#plt.show()

	# plot 3d: 2 centers
	data_center, _labels = _kmeans(data_trans,n_clusters=2)
	fig = plt.figure()
	ax2 = fig.add_subplot(111,projection='3d')
	#f1,ax2 = plt.subplots(figsize=(8,5))
	ax2.scatter(data_trans[:,0],data_trans[:,1],data_trans[:,2],c=_labels)

	ax2.set_xlabel('PC 1',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	ax2.set_ylabel('PC 2',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	ax2.set_zlabel('PC 3',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	
	ax2.set_xlim(-1,1)
	ax2.set_ylim(-0.1,1)
	ax2.set_zlim(-0.2,0.2)
	
	ax2.xaxis.set_ticks(np.arange(-1,1.1,0.5))
	ax2.yaxis.set_ticks(np.arange(-0.1,1.1,0.3))
	ax2.zaxis.set_ticks(np.arange(-0.2,0.21,0.1))

	ax2.xaxis.set_tick_params(labelsize=16)
	ax2.yaxis.set_tick_params(labelsize=16)
	ax2.zaxis.set_tick_params(labelsize=16)
	plt.tight_layout()
	plt.savefig('3d_2c.png',dpi=500)
