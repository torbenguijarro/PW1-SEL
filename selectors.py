import os
import pandas as pd


# IRIS DATASET (iris.data to dataframe)
file_name = './datasets/iris.data'
df = pd.read_csv(file_name, header=None)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df_X = df.drop('class', axis = 1)

# Print the first 5 rows of the data frame
print(df_X.head())

# Define the set of comparison operators
operators = {'=', '>', '<=', '!='}

# Create an empty set to store the selectors
selectors = set()

# Loop through each column in the data frame
for col_name in df_X.columns:
    # Loop through each value in the column
    for value in df_X[col_name].unique():
        # Loop through each comparison operator
        for op in operators:
            # Create the selector string
            selector = f"{col_name} {op} {value}"
            # Add the selector to the set
            selectors.add(selector)

# Convert the set to a list and print it
selectors_list = list(selectors)
print(selectors_list)
print(len(selectors_list))




