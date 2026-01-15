import pandas as pd

def allocation(holdings):
    df = pd.DataFrame(holdings)
    df["Value"] = df["Shares"] * df["Price"]
    df["Weight"] = df["Value"] / df["Value"].sum()
    return df