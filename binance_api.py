import ccxt
import schedule 
import pandas as pd 
pd.set_option("display.max_rows", None)

import numpy as np 
from datetime import datetime

exchange = ccxt.binance()

bars = exchange.fetch_ohlcv("BTC/BUSD",timeframe="5m",limit=1000)
df = pd.DataFrame(bars[:-1],columns=["timestamp","open","high","low","close","volume"])
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
print(df)


