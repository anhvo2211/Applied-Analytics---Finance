import pandas as pd
import matplotlib.pyplot as plt

prices = pd.read_csv("prices.csv", index_col="Date", parse_dates=True)
indexed = prices / prices.iloc[0] * 100      # start = 100

fig, ax = plt.subplots(figsize=(12, 6))

for ticker in indexed.columns:
    ax.plot(indexed.index, indexed[ticker], label=ticker)

# Shade the three crash windows
windows = [("2007-10-01", "2009-03-31"),
           ("2020-02-01", "2020-04-30"),
           ("2022-01-01", "2022-12-30")]
for start, end in windows:
    ax.axvspan(pd.Timestamp(start), pd.Timestamp(end), color="gray", alpha=0.15)

# Only show the 3 major years on the x-axis
ax.set_xticks(pd.to_datetime(["2008-01-01", "2020-01-01", "2022-01-01"]))
ax.set_xticklabels(["2008", "2020", "2022"])

ax.set_yscale("log")
ax.set_title("Growth of 100 invested in each asset (2007-2022)")
ax.set_xlabel("Year")
ax.set_ylabel("Index (start = 100, log scale)")
ax.legend(title="Ticker")

plt.tight_layout()
plt.savefig("prices_plot.png", dpi=150)
plt.show()