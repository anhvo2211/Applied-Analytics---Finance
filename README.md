# Which assets hold up when the e-commerce markets fall?
**Team:** Team 1 · **Topic:** Finance · **Tier:** Beginner

## TL;DR
Fill this in last.
- The answer to your question, in one sentence
- The strongest piece of evidence for it
- One thing that surprised you

## Question
- The shared question for your topic: How far did each asset fall in 2008, 2020, and 2022?
- Your specific question, in one sentence: How far did stock prices and ETFs fall in the e-commerce market in 2008, 2020, and 2022?
- Why it's worth answering: E-commerce is often seen as the future of retail, but it is unclear whether online retailers are a safe place to hold money when markets crash, or whether they fall harder than store retailers, bonds, and gold. Measuring how far each asset fell in during the market crash specifically in 2008, 2020, and 2022 shows how much risk an investor takes on and which assets could cushion a portfolio in the next downturn.

## Data
- Daily prices: Yahoo Finance via the `yfinance` library (`get_data.py`).
- Macro data: FRED, Federal Reserve Bank of St. Louis (`get_fred.py`), https://fred.stlouisfed.org
  - `DGS10`: 10-year Treasury yield (https://fred.stlouisfed.org/series/DGS10)
  - `CPIAUCSL`: Consumer Price Index, all urban consumers (https://fred.stlouisfed.org/series/CPIAUCSL)
  - `ECOMPCTSA`: e-commerce share of total retail sales (https://fred.stlouisfed.org/series/ECOMPCTSA)

**Time range and size**
- `prices.csv`: 2007-2023, 4,029 rows x 8 columns.
- `DGS10.csv`: 1962-01-02 to 2026-11-16, 16,925 rows x 2 columns.
- `CPIAUCSL.csv`: 1947-01-01 to 2026-10-01, 958 rows x 2 columns.
- `ECOMPCTSA.csv`: 1999-10-01 to 2026-04-01, 107 rows x 2 columns.
- Our analysis uses 2008 onward so the FRED data lines up with the prices.

**What one row represents**
- `prices.csv`: the adjusted closing price of each asset on one trading day.
- `DGS10.csv`: the 10-year yield on one day.
- `CPIAUCSL.csv`: the CPI index value for one month.
- `ECOMPCTSA.csv`: e-commerce's share of retail sales for one quarter.

**Key columns we use**
- `prices.csv`: all columns: `Date`, `AGG` (bond ETF), `AMZN`, `EBAY`, `GLD` (gold ETF), `SPY` (S&P 500 ETF), `TGT`, `WMT`.
- Each FRED file has two columns: the date (`observation_date`) and the value, named after the series. We use both columns of all three files.
- What you cleaned and why (dropped rows, filled missing values, merges): n/a

## Approach
- **How we explored the data first (EDA):** We first checked that the data sources are legitimate: prices come from Yahoo Finance (via `yfinance`), and the macro series come from FRED at the Federal Reserve Bank of St. Louis, which republishes official U.S. government data (Federal Reserve, Bureau of Labor Statistics, Census Bureau). We then checked the dates in each file: the start and end date, how many rows each has, and how often it is recorded (daily, monthly or quarterly). We confirmed they cover all three crashes (2008, 2020 and 2022).

- **Where and how we used SQL:** n/a (we have not started the analysis yet).

- **The method we used to answer the question, and why it fits:** The idea is to compare how far each asset fell, and how quickly it recovered, during the 2008, 2020 and 2022 market crashes, using the same crash dates for every asset so the comparison is fair. We then use the FRED data (interest rates, inflation and e-commerce share) to help explain why the crashes affected the assets differently. This fits the question because it directly measures the loss an investor would have faced in each crash and shows which assets held up best.

## Findings
- **Finding 1**
- Amazon grew far more than every other asset from 2007 to 2022, while the bond ETF grew the least.
- The figure that shows it (from figures/)
<img width="1800" height="900" alt="image" src="https://github.com/user-attachments/assets/0f61ab98-c448-4ae5-91bb-2cb3b2fc6422" />
- By the end of 2022, Amazon was worth roughly 40 times its 2007 starting level, while SPY, EBAY, TGT and WMT ended at roughly 3 to 4 times and the bond ETF (AGG) ended lowest. Amazon's growth came with larger swings: its line drops sharply inside the 2008 window and again in 2022, while AGG and GLD move much more steadily. This shows growth, not protection, so the drawdown analysis will measure how far each asset fell in each crash and how fast it recovered

End with a short answer to your question.

## How to Run
1. Install: `pip install -r requirements.txt`
2. Get the data (link or command, if it's not in the repo)
3. Run the cleaning code (name the file)
4. Run the analysis code (name the file)

