import requests

from bs4 import BeautifulSoup

# requests
query = "MSFT"
response = requests.get(f"https://finance.yahoo.com/gainers")

# beautiful soup
soup = BeautifulSoup(response.text, 'html.parser')
stocks_ticker = []
# print(f"{soup}")
for result in soup.select('a'):
    ticker_symbol = str(result.string)
    stocks_ticker.append(ticker_symbol)
stocks_ticker.remove("All Screeners")
stocks_ticker.remove("Yahoo")
# stocks_ticker.remove(str("None"))
# list(filter(None, stocks_ticker))
print(f"{stocks_ticker[18:118]}")
# print(type(stocks_ticker[1]))
# print(type(stocks_ticker))