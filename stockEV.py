import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import math
from datetime import datetime, timedelta


def main():
    ticker = input("Enter a stock ticker (e.g. TSLA): ")

    END_DATE = datetime.today()
    START_DATE = END_DATE - timedelta(days=1825)

    data = yf.download(ticker, start=START_DATE.strftime("%Y-%m-%d"),
                       end=END_DATE.strftime("%Y-%m-%d"))

    prices = data["Close"]

    if isinstance(prices, pd.DataFrame):
        prices = prices.squeeze()

    returns = prices.pct_change().dropna()
    total_returns = ((prices.iloc[-1] / prices.iloc[0]) - 1).squeeze()
    ev = returns.mean()
    vol = returns.std()

    sharpe = ev / vol * math.sqrt(252)

    print("Metrics:\n")
    print(f"Start date: {START_DATE.strftime("%Y-%m-%d")}")
    print(f"End date: {END_DATE.strftime("%Y-%m-%d")}")
    print(f"EV: {ev:.6f}")
    print(f"Total return: {total_returns:.6f}")
    print(f"Sharpe Ratio: {sharpe:.6f}")

    plt.plot(returns)
    plt.title("Stock Returns over time")
    plt.xlabel("Time")
    plt.ylabel("Return Percentage")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
