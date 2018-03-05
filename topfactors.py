# Recursive Feature Elimination
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import pandas
# load the iris datasets

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

dataframe = pandas.read_csv(url)
array=dataframe.values
X = array[:,0:8]
Y = array[:,8]

# create a base classifier used to evaluate a subset of attributes
model = LogisticRegression()
# create the RFE model and select 3 attributes
rfe = RFE(model, 3)
rfe = rfe.fit(X, Y)
# summarize the selection of the attributes
print(rfe.support_)
