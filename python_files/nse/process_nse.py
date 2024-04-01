import pandas as pd

nse_data = pd.read_csv("python_files/nse/nse.csv")

print(nse_data.head())

print(nse_data.dtypes)

# converting strings to numerics
nse_data["Price"] = nse_data["Price"].str.replace(",", "").astype(float)
nse_data["Open"] = nse_data["Open"].str.replace(",", "").astype(float)
nse_data["High"] = nse_data["High"].str.replace(",", "").astype(float)
nse_data["Low"] = nse_data["Low"].str.replace(",", "").astype(float)

# Replace 'B' with '000M' and 'M' with an empty string, then convert to numeric
nse_data["Vol."] = (
    nse_data["Vol."].str.replace("B", "000M").str.replace("M", "").astype(float)
)

# Remove '%' from Change % column and convert to numeric
nse_data["Change %"] = nse_data["Change %"].str.replace("%", "").astype(float)

# Display the updated data types
print(nse_data.dtypes)

# Check for missing values
print(nse_data.isnull().sum())

# drop rows with missing values
nse_data.dropna(subset=["Vol."], inplace=True)

# reset the index
nse_data.reset_index(drop=True, inplace=True)

print("Updated Data")
print(nse_data)
print(nse_data.isnull().sum())
# nse_data.to_csv("processed_nse.csv", index=False)
