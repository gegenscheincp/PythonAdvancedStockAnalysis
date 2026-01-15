import yfinance as yf

def get_stock_data(ticker, period="1y", interval="1d"):
    df = yf.Ticker(ticker).history(period=period, interval=interval)
    return df