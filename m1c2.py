import pandas as pd

data=pd.read_csv("sales_subset.csv")

print(data.info())
# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())
