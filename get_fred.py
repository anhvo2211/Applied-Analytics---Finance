import pandas as pd

for s in ["DGS10", "CPIAUCSL", "ECOMPCTSA"]:
    df = pd.read_csv(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}",
                     index_col=0, parse_dates=True, na_values=".")
    df.to_csv(f"{s}.csv")
    print(s, df.index.min().date(), df.index.max().date(), len(df))
