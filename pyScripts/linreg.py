import pandas as pd
import math
import datetime
import numpy as np
from sklearn import preprocessing, svm, model_selection
from sklearn.linear_model import LinearRegression, Ridge, Lasso, BayesianRidge
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error as mse
from scipy.stats import pearsonr as pn
import matplotlib.pyplot as plt
from matplotlib import style
import dataloader
from retailerdata import retailerData
import sklearn.naive_bayes as nb
import sklearn.tree as tree
import graphviz

style.use('ggplot')

# load dataframe with features:

# data = ....

# select features

def pretty_print_linear(coefs, names = None, sort = False):
    if names == None:
        names = ["X%s" % x for x in range(len(coefs))]
    lst = zip(coefs, names)
    if sort:
        lst = sorted(lst,  key = lambda x:-np.abs(x[0]))
    return " + ".join("%s * %s" % (round(coef, 3), name)
                                   for coef, name in lst)

def regress(data, features, target):
	# print(target)
	features.append(target)
	print('Features:')
	print(features)
	df = data[features].copy()

	df.dropna(inplace = True)

	split_ratio = 0.9

	# extracting features, scaling,
	X = np.array(df.drop(target, 1))
	# X = preprocessing.scale(X)

	# target
	y = np.array(df[target])

	#  splitting data
	split_index = math.ceil(len(X) * split_ratio)

	X_train = X[:split_index]
	X_test = X[split_index:]

	y_train = y[:split_index]
	y_test = y[split_index:]


	# creating regressor lin_regr
	reg = LinearRegression(n_jobs=-1)
	# reg = MLPRegressor(hidden_layer_sizes=(80,80), activation='logistic', alpha=0.0001,
	# 				   learning_rate='constant', learning_rate_init=0.001,
	# 				   power_t=0.5, max_iter=1000, shuffle=False, tol=0.0001)
	# reg = Ridge(alpha = 0.5)
	# reg = Lasso(alpha = 0.1)
	# reg = BayesianRidge()

	# reg = nb.BernoulliNB()
	# reg = nb.GaussianNB()
    #
	# reg = tree.DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=5, min_samples_split=2, min_samples_leaf=1,
	# 								min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None,
	# 														min_impurity_decrease=0.0, min_impurity_split=None, presort=False)
	# reg = tree.ExtraTreeRegressor()


	reg.fit(X_train, y_train)
	accuracy = reg.score(X_test, y_test)
	prediction_set = reg.predict(X_test)


	# print('Model: Y = ' + pretty_print_linear(reg.coef_, features) + ' + ' + str(reg.intercept_) )
	print('accuracy (R^2) :' + str(accuracy))
	mserror = mse(y_test, prediction_set)
	print('MSE: '+ str(mserror))
	# print('coefficients: ' + str(reg.coef_))
	pearson = pn(y_test, prediction_set)
	print('Pearson: ' + str(pearson))
	maxerror = max(abs(y_test - prediction_set))
	print('max error: ' + str(maxerror))
	print()

	return ('placeholder', #pd.DataFrame({'feature': features[0], 'target': features[1], 'coef':reg.coef_[0], 'intercept': reg.intercept_, 'r2': accuracy, 'mse' : mserror, 'pearson': pearson[0] , 'max_error' : maxerror}, index = [0]),
			prediction_set, y_test)

def regress_use_case(train, test, features, target, featuressave):
		print(target)
		# features.append(target)
		print('Features:')
		print(features)
		df = train[features].copy()
		df2 = test[features].copy()

		X_train = df.drop(target, 1)
		X_test = df2.drop(target, 1)


		y_train = df[target]
		y_test = df2[target]



		# creating regressor lin_regr
		# reg = LinearRegression(n_jobs=-1)
		# reg = MLPRegressor(hidden_layer_sizes=(80, 80), activation='logistic', alpha=0.0001,
		# 				   learning_rate='constant', learning_rate_init=0.001,
		# 				   power_t=0.5, max_iter=1000, shuffle=False, tol=0.0001)
		# reg = MLPRegressor(hidden_layer_sizes=(5), activation='logistic', alpha=0.0001,
		# 				   learning_rate='constant', learning_rate_init=0.001,
		# 				   power_t=0.5, max_iter=1000, shuffle=False, tol=0.0001)

		# reg = Ridge(alpha = 0.5)
		# reg = Lasso(alpha = 0.1)
		# reg = BayesianRidge()

		# reg = nb.GaussianNB()

		reg = tree.DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=8, min_samples_split=2, min_samples_leaf=5,
										min_weight_fraction_leaf=0.0, max_features=7, random_state=None, max_leaf_nodes=25,
															min_impurity_decrease=0.0, min_impurity_split=None, presort=False)


		reg.fit(X_train, y_train)
		# accuracy = reg.score(X_test, y_test)
		prediction_set = reg.predict(X_test)

		#Tree things
		# print()
		# print('Feature imoportances')
		# print()
		# print(reg.feature_importances_)
		dot_data = tree.export_graphviz(reg, out_file='depth8SMAPE.dot', max_depth = 8, feature_names = featuressave, class_names = None,
							 label ='all', filled = False, leaves_parallel = False, impurity = True, node_ids = False,
							 proportion = False, rotate = False, rounded = False, special_characters = False, precision = 3)


		#NB things
		# prediction_proba = reg.predict_proba(X_test)
		# params = reg.get_params(deep=True)
		# print(params)
		# print()
		# print(reg.coefs_)
		# print('Prediction Probability')
		# print()
		# print(prediction_proba)
		# print('Class Prior')
		# print()
		# print(reg.class_prior_)
		# print('Sigma')
		# print()
		# print(reg.sigma_)


		# print('Model: Y = ' + pretty_print_linear(reg.coef_, features) + ' + ' + str(reg.intercept_) )
		# print('accuracy (R^2) :' + str(accuracy))
		# mserror = mse(y_test, prediction_set)
		# print('MSE: ' + str(mserror))
		# print('coefficients: ' + str(reg.coef_))
		# pearson = pn(y_test, prediction_set)
		# print('Pearson: ' + str(pearson))
		# maxerror = max(abs(y_test - prediction_set))
		# print('max error: ' + str(maxerror))
		# print()

		return ('placeholder',# pd.DataFrame({'feature': features[0], 'target': features[1], 'coef':reg.coef_[0], 'intercept': reg.intercept_, 'r2': accuracy, 'mse' : mserror, 'pearson': pearson[0] , 'max_error' : maxerror}, index = [0]),
				prediction_set, y_test)



# prediction_set = reg.predict(X_test)

# print(prediction_set, accuracy, prediction_out)

# df_test['Prediction'] = prediction_set


# plt.legend(loc = 4)
# plt.xlabel('Date')
# plt.ylabel('Quantity')
# # plt.show()