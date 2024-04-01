import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("python_files/cbk/clean_cbkrates.csv")

# Fill missing values in the "YEAR" column with the preceding non-null value
data["YEAR"] = data["YEAR"].fillna(method="ffill")

print(data.head(50))

# Calculate basic statistics for Treasury bill rates
statistics = data[["91-Day Tbill", "182-days Tbill", "364-days Tbill"]].describe()

print("Basic Statistics for Treasury Bill Rates:")
print(statistics)

# Calculate risk free rate using the 91-day tbill
rf_rate = data["91-Day Tbill"].mean()
rf_rate_median = data["91-Day Tbill"].median()

print("Risk-free Rate (91-Day Tbill):", rf_rate)
print("Median Risk-free Rate (91-Day Tbill):", rf_rate_median)

# visualize the distribution of Treasury bill rates
# Plot histograms for each Treasury bill rate
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.hist(data["91-Day Tbill"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of 91-Day Tbill")
plt.xlabel("91-Day Tbill")
plt.ylabel("Frequency")

plt.subplot(1, 3, 2)
plt.hist(data["182-days Tbill"], bins=20, color="salmon", edgecolor="black")
plt.title("Distribution of 182-days Tbill")
plt.xlabel("182-days Tbill")
plt.ylabel("Frequency")

plt.subplot(1, 3, 3)
plt.hist(data["364-days Tbill"], bins=20, color="lightgreen", edgecolor="black")
plt.title("Distribution of 364-days Tbill")
plt.xlabel("364-days Tbill")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("treasury_bill_distributions.png")
plt.close()

# Plot line plots to check for trends over time
# The code below will generate line graphs comparing the three

# plt.figure(figsize=(12, 6))
# plt.plot(data["YEAR"], data["91-Day Tbill"], label="91-Day Tbill", marker="o")
# plt.plot(data["YEAR"], data["182-days Tbill"], label="182-days Tbill", marker="o")
# plt.plot(data["YEAR"], data["364-days Tbill"], label="364-days Tbill", marker="o")
# plt.title("Treasury Bill Rates Over Time")
# plt.xlabel("Year")
# plt.ylabel("Treasury Bill Rate")
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.savefig("treasury_bill_trends.png")
# plt.close()
