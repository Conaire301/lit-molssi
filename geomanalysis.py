"""
This is is a colossal mistake
"""

import numpy
import os
import argparse
def kyle (coords1, coords2):
    xdist= coords1[0]-coords2[0]
    ydist=coords1[1]-coords2[1]
    zdist=coords1[2]-coords2[2]
    jamesbondlength=numpy.sqrt(xdist**2 +ydist**2+zdist**2)
    return jamesbondlength

def checkbond(atom_distance, mindist=0, maxdist=1.5):
    """
    Gives a True/False answer whether a data is in a range
    Input: Select your data, range min, range max (defaulted to 0, 1.5 respectively)
    Output:True/False
    """
    if atom_distance >mindist and atom_distance <=maxdist:
        return True
    else:
        return False
parser= argparse.ArgumentParser(description="This script analyzes a user provided xyz file and outputs bonds")
parser.add_argument("xyz_file", help="The file path for the xyz file to analyze")
args= parser.parse_args()

file=args.xyz_file
patrick=numpy.genfromtxt(fname=file, skip_header=2, dtype='unicode')
mol=patrick[:,0]
coords=patrick[:,1:]
coords=coords.astype(numpy.float)
atoms=len(mol)
for start in range(0,atoms):
    for end in range(0,atoms):
        if start<end:
            jamesbondlength=kyle(coords[start],coords[end])
            if checkbond(jamesbondlength) is True:
                print(F'{mol[start]} to {mol[end]} : {jamesbondlength:.3f}')
