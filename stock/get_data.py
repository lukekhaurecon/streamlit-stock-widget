"""
Pull in stock data

mostly stolen from [here](https://medium.com/@wl8380/how-to-create-a-stock-chart-in-python-a-step-by-step-guide-with-aapl-6d6dd2eceb67)
"""
from datetime import datetime, timedelta
from typing import Optional
import yfinance as yf

def get_data(ticker_symbol: str, start: Optional[datetime] = None):
    """
    Given a ticker symbol, get the relevant data from start datetime to present

    It will also add a `50_MA` field which is the 50 day moving average
    """
    if start is None:
        start = datetime.now() - timedelta(days=365)

    stock_data = yf.download(ticker_symbol, start=start)

    stock_data[("50_MA", ticker_symbol)] = stock_data["Close"].rolling(window=50, min_periods=1).mean()

    stock_data.columns = stock_data.columns.droplevel(1)

    stock_data["Code"] = ticker_symbol

    return stock_data

if __name__ == "__main__":
    code = "^AXJO"
    d = get_data(code)
    print(d)
