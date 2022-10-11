import ccxt 
import pandas as pd 
import tradingview_ta
import scipy as sc 
import pandas_ta as ta 

exchange = ccxt.binance()
since = exchange.parse8601 ('2022-10-10T03:00:00Z')
bar = exchange.fetch_ohlcv("BTC/BUSD",timeframe="5m",since=since,limit=174)
df = pd.DataFrame(bar[:-1],columns=["timestep","open","high","low","close","volume"])
df["timestep"] = pd.to_datetime(df["timestep"],unit="ms")

print(df)
