
import csv

# Open the CSV file and read its contents into a list of dictionaries
with open('orange.iris.data', 'r') as file:
	reader = csv.DictReader(file)
	data = list(reader)

# Define the set of comparison operators
operators = {'=', '>', '<=', '!='}

# Create an empty list to store the selectors
selectors = []

# Loop through each row in the data
for row in data:
	# Loop through each column in the row
	for col_name in row.keys():
		# Skip the 'class' column
		if col_name == 'class':
			continue
		# Loop through each comparison operator
	for op in operators:
		# Create the selector string
        selector = f"{col_name} {op} {row[col_name]}"
		# Append the selector to the list
        selectors.append(selector)

# Print the list of selectors
print(selectors)


