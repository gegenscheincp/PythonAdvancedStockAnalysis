import yfinance as yf

def dividend_projection(ticker, shares):
    rate = yf.Ticker(ticker).info.get("dividendRate", 0)
    return rate * shares