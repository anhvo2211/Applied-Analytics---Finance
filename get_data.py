import yfinance as yf

# Amazon, eBay, Walmart, Target, S&P 500 ETF, bond ETF, gold ETF
tickers = ["AMZN", "EBAY", "WMT", "TGT", "SPY", "AGG", "GLD"]

prices = yf.download(
    tickers,
    start="2007-01-01",
    end="2023-01-01",
    auto_adjust=True,
)["Close"]

# Quick checks
print(prices.head())
print(prices.tail())
print("Missing values per ticker:")
print(prices.isna().sum())

prices.to_csv("prices.csv")
print("Saved prices.csv with", len(prices), "rows")