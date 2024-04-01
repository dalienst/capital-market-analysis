import pandas as pd

data = pd.read_csv("python_files/cbk/cbkrates.csv")

# display the first rows
print("Rows")
print(data.head())

# check datatypes
print("Data Types")
print(data.dtypes)

# check for missing values
print("Missing Values")
print(data.isnull().sum())

# rename columns
new_columns = [
    "YEAR",
    "MONTH",
    "Repo",
    "Reverse Repo",
    "Interbank Rate",
    "91-Day Tbill",
    "182-days Tbill",
    "364-days Tbill",
    "Cash Reserve Requirement",
    "Central Bank Rate",
]
data.columns = new_columns

# Drop the first row as it contains invalid data
data = data.drop(index=0).reset_index(drop=True)

# Convert numeric columns to float, replacing '-' with NaN
numeric_columns = [
    "Repo",
    "Reverse Repo",
    "Interbank Rate",
    "91-Day Tbill",
    "182-days Tbill",
    "364-days Tbill",
]
data[numeric_columns] = data[numeric_columns].replace("-", float("nan"))
# handle missing values in other columns
data["Cash Reserve Requirement"] = data["Cash Reserve Requirement"].replace(
    "-", float("nan")
)
data["Central Bank Rate"] = data["Central Bank Rate"].replace("-", float("nan"))

# Check for missing values again
print("Missing Values:")
print(data.isnull().sum())

# Drop unnecessary columns
data = data[["YEAR", "MONTH", "91-Day Tbill", "182-days Tbill", "364-days Tbill"]]

# Check the resulting dataset
print("Updated Dataset:")
print(data.head())

print("Missing Values:")
print(data.isnull().sum())

# Save the cleaned dataset
# data.to_csv("python_files/cbk/clean_cbkrates.csv", index=False)
