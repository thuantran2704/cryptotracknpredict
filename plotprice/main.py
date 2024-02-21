import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

crypto_currency = 'BTC'
currency = 'USD'

start = dt.datetime(2015, 1, 1)
end = dt.datetime(2020, 1, 1)

# Correct usage of YahooDailyReader
yahoo_read = web.yahoo.daily.YahooDailyReader(f'{crypto_currency}-{currency}', start, end)

# Read data into a DataFrame
data = yahoo_read.read()

print(data.head())

