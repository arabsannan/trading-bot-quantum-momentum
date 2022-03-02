import numpy as np
import pandas as pd
import requests
import math
from scipy import stats
import xlsxwriter
from secrets import IEX_CLOUD_API_TOKEN

# importing stocks
stocks = pd.read_csv("sp_500_stocks.csv")
# print(stocks)

# Working with IEX Cloud API
symbol = "AAPL"
api_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/stats?token={IEX_CLOUD_API_TOKEN}"
data = requests.get(api_url).json()


def chunks(lst, n):
    # yield successive n-sized chunks from list
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


symbol_groups = list(chunks(stocks['Ticker'], 100))
symbol_strings = []

for i in range(0, len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))
    # print(symbol_strings[i])

my_columns = ['Ticker', 'Price', 'One-Year Price Return', 'Number of Shares to Buy']

# adding data to the DataFrame
final_dataframe = pd.DataFrame()
print("1")

for symbol_string in symbol_strings:
    print("2")
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=stats' \
                         f'&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    # print(data)
    print("3")
#
    for symbol in symbol_string.split(','):
        one_year_percentage = data[symbol]['stats']['year1ChangePercent']
        print("4")
        df1 = pd.DataFrame({
            "Ticker": [symbol],
            "Price": ["N/A"],
            "One-Year Price Return": [one_year_percentage],
            "Number of Shares to Buy": ["N?A"]
        })
        print("5")
#         final_dataframe = pd.concat([final_dataframe, df1], ignore_index=True, axis=0)
#     print("6")


print("8")
# print(final_dataframe)


