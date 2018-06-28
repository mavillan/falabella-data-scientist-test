import sys
import numba
import numpy as np
import numpy.ma as ma
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from sklearn.metrics import silhouette_score

mappings = {
    "alto_plataforma" : {"0 cm":0, "0":0, "0 5 cm":0, "1":1, "1 cm":1, "2":2, "2 cm":2, "3":3, "3 cm": 3,
                        "4":4, "4 cm":4, "5":5, "5 cm":5, "6":6, "6 cm":6, "7":7, "7 cm":7, "8":8, "8 cm":8,
                        "9":9, "9 cm":9, "10":10, "10 cm":10, "12 cm":11, "1 4 cm": 12, "redonda":13, "baja":14},
    "altura_cana" : {"7":0, "7 cm":0, "7 3 cm":0, "8 cm":1, "9":2, "11":3, "12":4, "12 cm":4, "15 cm":5},
    "altura_taco" : {"sin taco":0, "bajo":1, "bajon":1, "medio":2, "alto":3, "1 5 cm":4, "2 cm":5, "2 5 cm":6,
                    "3 cm":7, "3 2 cm":7, "3 3 cm":7, "3 5 cm":8},
    "medida_taco" : {"1":0, "2":1, "2 cm":1, "3":2, "3 cm":2, "3 3 cm":2, "4 cm":3, "5 cm":4}
    
}


def preprocessing(products, query):
	df1 = pd.read_csv(products, sep=",")
	df2 = pd.read_csv(query, sep=",")
	# number of query items
	n_query = df2.shape[0] 
	df = pd.concat([df1,df2])

	# replace values with no info to nan
	df.replace(to_replace="sin informacion", value=np.nan, inplace = True)
	df.replace(to_replace="no disponible", value=np.nan, inplace = True)
	df.replace(to_replace="n a", value=np.nan, inplace = True)
	df.replace(to_replace="no aplica", value=np.nan, inplace = True)
	df.replace(to_replace="", value=np.nan, inplace = True)
	df.replace(to_replace=" ", value=np.nan, inplace = True)
	df.replace(mappings, inplace=True)

	# categorical to category values
	for column in df.columns:
	    df[column] = df[column].astype('category')
	    df[column] = df[column].cat.codes
	df.replace(to_replace=-1, value=np.nan, inplace = True)

	# numpy dataset
	dataset = df.as_matrix()

	m,n = dataset.shape
	indexes = []
	for i in range(m):
	    if np.all(np.isnan(dataset[i,:])):
	        indexes.append(i)      
	dataset = np.delete(dataset, indexes, axis=0)      

	return dataset,n_query


# numba is used to speedup the computation through JIT
@numba.jit(nopython=True)
def similarity_matrix(dataset):
    n_samples,n_attr = dataset.shape
    smatrix = np.empty((n_samples,n_samples))
    for i in range(n_samples):
        for j in range(i,n_samples):
            smatrix[i,j] = np.sum(dataset[i]==dataset[j])/n_attr
            smatrix[j,i] = smatrix[i,j]
    
    for i in range(n_samples):
        # each row is scaled so that the diagonal value is 1,
        # since similirity between items (i,i) should be the same
        smatrix[i] /= smatrix[i,i]
    return smatrix



def get_cluster(query):
	"""
	test is an string with the path to a .csv file with the items to query
	"""
	dataset, n_query = preprocessing("data/products", query)

	return None


if __name__=="__main__":
	path_to_query = sys.argv[1]
	dataset,n_query = preprocessing("data/products", path_to_query)
	smatrix = similarity_matrix(dataset)
	dmatrix = 1.-smatrix

	# n_cluster set according to experiments in notebook
	clf = SpectralClustering(n_clusters=2, affinity="precomputed", n_jobs=2)
	pred = clf.fit_predict(smatrix)
	score = silhouette_score(dmatrix, pred, metric="precomputed")
	print("Silhouette score: ",score)
	print("Number of clusters:", np.max(pred)+1)
	print("\nPredictions:", pred[-n_query:])
