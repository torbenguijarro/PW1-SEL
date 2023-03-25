# Import required libraries
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler



def preprocess_iris():
    file_name = './datasets/iris.data'
    df = pd.read_csv(file_name, header=None)
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

    # # Numerical variables
    # numeric_vbles = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    # for c in numeric_vbles:
    #     df[c] = StandardScaler().fit_transform(df[c].values.reshape(-1, 1))

    # Discretize categorical variables
    df['class'] = df['class'].replace({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})
    df = df.sort_values('class')

    Y = df['class']
    X = df.drop('class', axis = 1)
    return X, Y


## Testing
# Print Y and X
X, Y = preprocess_iris()
print(Y)
print(X)


