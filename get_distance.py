import sys
import numpy as np


def get_similarity(i, j):
	# this way we avoid recomputing and loading the whole similarity matrix
	smatrix = np.load("data/smatrix.npy", mmap_mode="r")
	return smatrix[i,j]

def get_distance(i, j):
	# this way we avoid recomputing and loading the whole similarity matrix
	smatrix = np.load("data/smatrix.npy", mmap_mode="r")
	return 1.-smatrix[i,j]


if __name__=="__main__":
	i = int(sys.argv[1])
	j = int(sys.argv[2])
	print("Distance between items {0} and {1} is {2}".format(i,j,get_distance(i,j)))

