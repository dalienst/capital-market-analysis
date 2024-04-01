import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

eabl_data = pd.read_csv("python_files/companies/eabl.csv")

print(eabl_data.head())

# convert date columns to datetime format
eabl_data["Date"] = pd.to_datetime(eabl_data["Date"])

print(eabl_data.dtypes)

# check for missing values
print(eabl_data.isnull().sum())

# Display summary statistics
print("Summary Statistics")
print(eabl_data.describe())

# Visualize the distributions
# generate histograms

# eabl_data.hist(figsize=(10, 8))
# plt.tight_layout()
# plt.savefig("eabl_distributions.png")
# plt.close()

# MARKET RETURNS
# sort by date in ascending order
eabl_data = eabl_data.sort_values(by="Date")

# strip leading white spaces
eabl_data.columns = eabl_data.columns.str.strip()

# calculate daily returns
eabl_data["EABL_Returns"] = eabl_data["Close"].pct_change() * 100

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
merged_data = pd.merge(eabl_data, nse_data, on="Date", how="inner")

# calculate the correlation between the two datasets
correlation = merged_data["EABL_Returns"].corr(merged_data["NSE_Returns"])

print("EABL Returns:")
print(merged_data[["Date", "EABL_Returns"]])

print("\nNSE Returns:")
print(merged_data[["Date", "NSE_Returns"]])

print("Correlation:", correlation)

# # VISUALIZATIONS
# # Line Plot of eabl and NSE Returns Over Time
# plt.figure(figsize=(10, 6))
# plt.plot(merged_data["Date"], merged_data["EABL_Returns"], label="EABL Returns")
# plt.plot(merged_data["Date"], merged_data["NSE_Returns"], label="NSE Returns")
# plt.xlabel("Date")
# plt.ylabel("Returns")
# plt.title("EABL and NSE Returns Over Time")
# plt.legend()
# plt.savefig("eabl_nse_returns_lineplot.png")  # Save the plot as PNG file
# plt.close()

# # Scatter Plot of eabl and NSE Returns
# plt.figure(figsize=(8, 6))
# plt.scatter(merged_data["EABL_Returns"], merged_data["NSE_Returns"])
# plt.xlabel("EABL Returns")
# plt.ylabel("NSE Returns")
# plt.title("Scatter Plot of EABL and NSE Returns")
# plt.savefig("eabl_nse_returns_scatterplot.png")
# plt.close()

# # Histograms of eabl and NSE Returns
# plt.figure(figsize=(12, 6))
# plt.hist(merged_data["EABL_Returns"], bins=30, alpha=0.5, label="EABL Returns")
# plt.hist(merged_data["NSE_Returns"], bins=30, alpha=0.5, label="NSE Returns")
# plt.xlabel("Returns")
# plt.ylabel("Frequency")
# plt.title("Histograms of EABL and NSE Returns")
# plt.legend()
# plt.savefig("eabl_nse_returns_histograms.png")
# plt.close()


# BETA COEFFICIENTS
merged_eabl_nse_data = pd.merge(eabl_data, nse_data, on="Date", how="inner")

merged_eabl_nse_data.dropna(inplace=True)

# Define independent variable X and dependent variable y
X = merged_eabl_nse_data["NSE_Returns"]
Y = merged_eabl_nse_data["EABL_Returns"]

# add constant to independent variable X for the intercept term
X = sm.add_constant(X)

# fit the linear regression model
model = sm.OLS(Y, X).fit()

# get the summary of the regression model
print(model.summary())

# Beta coefficient is the independent variable (NSE_Returns)
beta = model.params["NSE_Returns"]
print("Beta Coefficient:", beta)
