import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

saf_data = pd.read_csv("python_files/companies/safaricom.csv")

print(saf_data.head())

# convert date columns to datetime format
saf_data["Date"] = pd.to_datetime(saf_data["Date"])

print(saf_data.dtypes)

# check for missing values
print(saf_data.isnull().sum())

# Display summary statistics
print("Summary Statistics")
print(saf_data.describe())

# Visualize the distributions
# generate histograms

# saf_data.hist(figsize=(10, 8))
# plt.tight_layout()
# plt.savefig("saf_distributions.png")
# plt.close()

# MARKET RETURNS
# sort by date in ascending order
saf_data = saf_data.sort_values(by="Date")

# strip leading white spaces
saf_data.columns = saf_data.columns.str.strip()

# calculate daily returns
saf_data["Safaricom_Returns"] = saf_data["Close"].pct_change() * 100

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
merged_data = pd.merge(saf_data, nse_data, on="Date", how="inner")

# calculate the correlation between the two datasets
correlation = merged_data["Safaricom_Returns"].corr(merged_data["NSE_Returns"])

print("Safaricom Returns:")
print(merged_data[["Date", "Safaricom_Returns"]])

print("\nNSE Returns:")
print(merged_data[["Date", "NSE_Returns"]])

print("Correlation:", correlation)

# # VISUALIZATIONS
# # Line Plot of safaricom and NSE Returns Over Time
# plt.figure(figsize=(10, 6))
# plt.plot(
#     merged_data["Date"], merged_data["Safaricom_Returns"], label="Safaricom Returns"
# )
# plt.plot(merged_data["Date"], merged_data["NSE_Returns"], label="NSE Returns")
# plt.xlabel("Date")
# plt.ylabel("Returns")
# plt.title("Safaricom and NSE Returns Over Time")
# plt.legend()
# plt.savefig("safaricom_nse_returns_lineplot.png")  # Save the plot as PNG file
# plt.close()

# # Scatter Plot of Safaricom and NSE Returns
# plt.figure(figsize=(8, 6))
# plt.scatter(merged_data["Safaricom_Returns"], merged_data["NSE_Returns"])
# plt.xlabel("Safaricom Returns")
# plt.ylabel("NSE Returns")
# plt.title("Scatter Plot of Safaricom and NSE Returns")
# plt.savefig("safaricom_nse_returns_scatterplot.png")
# plt.close()

# # Histograms of Safaricom and NSE Returns
# plt.figure(figsize=(12, 6))
# plt.hist(
#     merged_data["Safaricom_Returns"], bins=30, alpha=0.5, label="Safaricom Returns"
# )
# plt.hist(merged_data["NSE_Returns"], bins=30, alpha=0.5, label="NSE Returns")
# plt.xlabel("Returns")
# plt.ylabel("Frequency")
# plt.title("Histograms of Safaricom and NSE Returns")
# plt.legend()
# plt.savefig("safaricom_nse_returns_histograms.png")
# plt.close()


# BETA COEFFICIENTS
merged_saf_nse_data = pd.merge(saf_data, nse_data, on="Date", how="inner")

merged_saf_nse_data.dropna(inplace=True)

# Define independent variable X and dependent variable y
X = merged_saf_nse_data["NSE_Returns"]
Y = merged_saf_nse_data["Safaricom_Returns"]

# add constant to independent variable X for the intercept term
X = sm.add_constant(X)

# fit the linear regression model
model = sm.OLS(Y, X).fit()

# get the summary of the regression model
print(model.summary())

# Beta coefficient is the independent variable (NSE_Returns)
beta = model.params["NSE_Returns"]
print("Beta Coefficient:", beta)
