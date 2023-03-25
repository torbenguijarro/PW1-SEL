import os
import csv
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


class Complex:
    def __init__(self, selectors):
        self.selectors = selectors
        self.p = None # probability of covering a positive example
        self.n = None # probability of covering a negative example
        self.cov_pos = None # number of covered positive examples
        self.cov_neg = None # number of covered negative examples
        self.laplace = None # Laplace estimate of probability

class Rule:
    def __init__(self, CPX, C):
        self.CPX = CPX
        self.C = C

def CN2(E, SELECTORS):
    RULE_LIST = []
    while True:
        BEST_CPX = Find_Best_Complex(E, SELECTORS)
        if BEST_CPX is None or not E:
            break
        E_ = Examples_covered_by_CPX(BEST_CPX, E)
        E = E - E_
        C = Most_Common_Class(E_)
        RULE_LIST.append(Rule(BEST_CPX, C))
    return RULE_LIST

def Find_Best_Complex(E, SELECTORS):
    STAR = {Complex({()})}
    BEST_CPX = None
    while STAR:
        NEWSTAR = {x.selectors | {y} for x in STAR for y in SELECTORS}
        NEWSTAR = {c for c in NEWSTAR if c not in STAR and not c.selectors.isdisjoint(cov.selectors)}
        for Ci in NEWSTAR:
            Ci.cov_pos = len([e for e in E if Ci.selectors.issubset(e.attributes) and e.class_ == 'pos'])
            Ci.cov_neg = len([e for e in E if Ci.selectors.issubset(e.attributes) and e.class_ == 'neg'])
            Ci.p = Ci.cov_pos / len([e for e in E if e.class_ == 'pos'])
            Ci.n = Ci.cov_neg / len([e for e in E if e.class_ == 'neg'])
            Ci.laplace = (Ci.cov_pos + 1) / (Ci.cov_pos + Ci.cov_neg + 2)
            if Ci.is_statistically_significant(E) and Ci.is_better_than(BEST_CPX, E):
                BEST_CPX = Ci
        while len(NEWSTAR) > user_defined_maximum_size:
            Worst_complex = Worst(NEWSTAR)
            NEWSTAR -= {Worst_complex}
        STAR = NEWSTAR
    return BEST_CPX

def Examples_covered_by_CPX(CPX, E):
    return {example for example in E if CPX.selectors.issubset(example.attributes)}

def Most_Common_Class(E):
    return max(set([example.class_ for example in E]), key=[example.class_ for example in E].count)
