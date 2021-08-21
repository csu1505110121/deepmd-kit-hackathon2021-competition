#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import mdtraj as md
import matplotlib.pyplot as plt

def _rdf(filename):
	traj = md.load_pdb(filename)
	bins = 300
	r_max = 1 # in the unit of nm
	r_min = 0.01 
	
	pair = traj.top.select_pairs([x for x in range(traj.topology.n_atoms)],[x for x in range(traj.topology.n_atoms)])

	mdtraj_rdf = md.compute_rdf(traj, pair, (r_min,r_max),n_bins=bins)

	return mdtraj_rdf

if __name__ == '__main__':
	f1 = 'cu.bcc.02x02x02.pdb'
	f2 = 'cu.fcc.02x02x02.pdb'
	f3 = 'cu.hcp.02x02x02.pdb'
	f4 = 'cu.bcc.02x02x02.high_pressure.pdb'
	f5 = 'cu.fcc.02x02x02.high_pressure.pdb'
	f6 = 'cu.fcc.02x02x02.high_pressure.pdb'

	d1 = _rdf(f1)
	d2 = _rdf(f2)
	d3 = _rdf(f3)
	d4 = _rdf(f4)
	d5 = _rdf(f5)
	d6 = _rdf(f6)

	fig,ax = plt.subplots(figsize=(8,6))

	ax.plot(*d1,label='cu.bcc')
	ax.plot(*d2,label='cu.fcc')
	ax.plot(*d3,label='cu.hcp')
	
	ax.plot(*d4,'--',label='cu.bcc.high_pressure')
	ax.plot(*d5,'--',label='cu.fcc.high_pressure')
	ax.plot(*d6,'--',label='cu.hcp.high_pressure')

	ax.set_xlabel(r'$r_{Cu \cdots Cu} ~(nm)$',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)
	ax.set_ylabel(r'$g(r_{Cu \cdots Cu})$',fontsize=18, fontfamily='sans-serif',fontstyle='italic',labelpad=10)

	ax.set_xlim(0,1)
	ax.set_ylim(0,12)

	ax.xaxis.set_ticks(np.arange(0,1.1,0.2))
	ax.yaxis.set_ticks(np.arange(0,12,3))

	ax.xaxis.set_tick_params(labelsize=16)
	ax.yaxis.set_tick_params(labelsize=16)

	plt.legend(fontsize=16,loc='best')
	plt.tight_layout()
	plt.savefig('rdf.png',dpi=800)
	
