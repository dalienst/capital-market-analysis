import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv("python_files/companies/absa.csv")

print(data.head())

print(data.dtypes)

# convert date columns to datetime format
data["Date"] = pd.to_datetime(data["Date"])

print(data.dtypes)

# check for missing values
print(data.isnull().sum())

# Display summary statistics
print("Summary Statistics")
print(data.describe())

# Visualize the distributions
# code below generates an image with the summaries

# data.hist(figsize=(10, 8))
# plt.tight_layout()
# plt.savefig("absa_distributions.png")
# plt.close()

# MARKET RETURNS
# convert date to datetime
data["Date"] = pd.to_datetime(data["Date"])

# sorting by date in ascending order
absa_data = data.sort_values(by="Date")

# Strip leading and trailing spaces from column names
absa_data.columns = absa_data.columns.str.strip()

# calculate daily returns
absa_data["Absa_Returns"] = absa_data["Close"].pct_change() * 100

# NSE Data
nse_data = pd.read_csv("python_files/nse/nse_processed.csv")

# convert date to datetime
nse_data["Date"] = pd.to_datetime(nse_data["Date"])

# sort by date in ascending order
nse_data = nse_data.sort_values(by="Date")

# Strip leading and trailing spaces from column names
nse_data.columns = nse_data.columns.str.strip()

# calculate daily returns
nse_data["NSE_Returns"] = nse_data["Close"].pct_change() * 100

# Merge the two datasets
merged_data = pd.merge(absa_data, nse_data, on="Date", how="inner")

# calculate the correlation between the two datasets
correlation = merged_data["Absa_Returns"].corr(merged_data["NSE_Returns"])


print("ABSA Returns:")
print(merged_data[["Date", "Absa_Returns"]])

print("\nNSE Returns:")
print(merged_data[["Date", "NSE_Returns"]])
print("Correlation:", correlation)

# VISUALIZATIONS

# # Scatter Plot of ABSA and NSE Returns
# plt.figure(figsize=(8, 6))
# plt.scatter(merged_data["Absa_Returns"], merged_data["NSE_Returns"])
# plt.xlabel("ABSA Returns")
# plt.ylabel("NSE Returns")
# plt.title("Scatter Plot of ABSA and NSE Returns")
# plt.savefig("absa_nse_returns_scatterplot.png")  # Save the plot as PNG file
# plt.close()

# # Histograms of ABSA and NSE Returns
# plt.figure(figsize=(12, 6))
# plt.hist(merged_data["Absa_Returns"], bins=30, alpha=0.5, label="ABSA Returns")
# plt.hist(merged_data["NSE_Returns"], bins=30, alpha=0.5, label="NSE Returns")
# plt.xlabel("Returns")
# plt.ylabel("Frequency")
# plt.title("Histograms of ABSA and NSE Returns")
# plt.legend()
# plt.savefig("absa_nse_returns_histograms.png")  # Save the plot as PNG file
# plt.close()

# # Line Plot of ABSA and NSE Returns Over Time
# plt.figure(figsize=(10, 6))
# plt.plot(merged_data["Date"], merged_data["Absa_Returns"], label="ABSA Returns")
# plt.plot(merged_data["Date"], merged_data["NSE_Returns"], label="NSE Returns")
# plt.xlabel("Date")
# plt.ylabel("Returns")
# plt.title("ABSA and NSE Returns Over Time")
# plt.legend()
# plt.savefig("absa_nse_returns_lineplot.png")
# plt.close()

# BETA COEFFICIENTS
merged_absa_nse_data = pd.merge(absa_data, nse_data, on="Date", how="inner")

merged_absa_nse_data.dropna(inplace=True)

# Define independent variable X and dependent variable y
X = merged_absa_nse_data["NSE_Returns"]
Y = merged_absa_nse_data["Absa_Returns"]

# add constant to independent variable X for the intercept term
X = sm.add_constant(X)

# fit the linear regression model
model = sm.OLS(Y, X).fit()

# get the summary of the regression model
print(model.summary())

# Beta coefficient is the independent variable (NSE_Returns)
beta = model.params["NSE_Returns"]
print("Beta Coefficient:", beta)
