import numpy as np
import matplotlib.pyplot as plt
import pydotplus
from io import StringIO
from sklearn.model_selection import cross_val_score
from sklearn import neighbors
from data_preprocessor import get_data

def run_k_nearest_neighbour():
	X_train, X_test, y_train, y_test = get_data()

	clf = neighbors.KNeighborsClassifier(10, 'uniform')
	clf.fit(X_train, y_train)
	scores = cross_val_score(clf, X_test, y_test, cv=5)
	print("k_nearest_neighbour: %.15f" % scores.mean())

if __name__ == '__main__':
	run_k_nearest_neighbour()