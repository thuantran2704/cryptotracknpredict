import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential

data_source = 'yahoo'
crypto_currency = 'BTC'
currency = 'USD'

start = dt.datetime(2019,1,1)
end = dt.datetime.now()

data = web.DataReader(f'{crypto_currency}-{currency}', 'yahoo', start, end)

print(data.head())
