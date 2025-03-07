import pandas as pd

fname = "Cartwheeldata.csv"
data = pd.read_csv(fname)

print(data)
print(data.head())
print(data.head(10))
#column names
print(data.columns)

#these two are the same
print(data.loc[:,["CWDistance", "Height", "Wingspan"]])
print(data[["CWDistance", "Height", "Wingspan"]])

print(data.loc[10:15])

#for position based slicing
print(data.iloc[1:5, 2:4])

# List unique values in the data['Gender'] column
print(data["Gender"].unique())

print(pd.crosstab(data["Gender"], data["GenderGroup"])) #cross tabulation
