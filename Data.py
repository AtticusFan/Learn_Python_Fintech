import yfinance as yf
import pandas as pd
from FinMind.data import DataLoader
#yfinance
def getDataYF(prod, st, en):
    tmpdata = yf.download(prod, start = st, end = en)
    tmpdata.columns = [i.lower() for i in tmpdata.columns]
    return tmpdata
#FinMind
FM = DataLoader()
def getDataFM(prod, st, en):
    tmpdata = FM.taiwan_stock_daily_adj(stock_id = prod, start_date = st, end_date = en)
    tmpdata = tmpdata.rename(columns = {'max':'high', 'min':'low', 'Trading_Volume':'volume'})
    #將日期設定為索引
    tmpdata['date'] = pd.to_datetime(tmpdata['date'])
    tmpdata = tmpdata.set_index(tmpdata['date'])
    tmpdata = tmpdata[['open', 'high', 'low', 'close', 'volume']]
    return tmpdata
