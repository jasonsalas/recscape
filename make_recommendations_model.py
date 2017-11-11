from __future__ import (absolute_import, division, print_function, unicode_literals)
from surprise import Dataset, Reader, evaluate, SVD, print_perf, dump
import os, io

ratings_file = os.path.expanduser('ratings.txt')
reader = Reader(line_format='user item rating', sep='|')
data = Dataset.load_from_file(ratings_file, reader=reader)
training_set = data.build_full_trainset()

algorithm = SVD()					# use the singular value decomposition
algorithm.train(training_set)		# fit the data to the model

testing_set = training_set.build_anti_testset()
predictions = algorithm.test(testing_set)		# make predictions

dump.dump('./serialized_model', predictions, algo=algorithm)	# serialize the algorithm
print('COMPLETED AND SAVED!')
print('computing accuracy statistics...')
accuracy = evaluate(algorithm, data, measures=['RMSE', 'MAE'])
print(accuracy)