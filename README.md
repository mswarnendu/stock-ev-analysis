# Stock EV Analyzer

## What this project does

- Downloads historical data over 5 years (based on the date the program is run) using yfinance
- Computes daily returns
- Calculates total returns, volatility, and Sharpe ratio
- Plots returns over time

## Assumptions

- Risk-free rate is assumed to be 0
- Uses 252 trading days for annualization

## Before Running

Type the following command into a new terminal in stockEV.py

pip install yfinance matplotlib yfinance
