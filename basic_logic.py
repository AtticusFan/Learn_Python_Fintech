#基本進出場邏輯與紀錄回測交易明細
from Data import getDataFM
import pandas as pd
import BackTest as bt
prod = '0050'
data = getDataFM(prod, '2022-01-01', '2022-10-31')
position = 0
trade = pd.DataFrame()
'''語法
data.shape[0] --> rows
data.loc[] --> 取出特定資料
ignore_index = True --> 可以忽略合併時舊的 index 欄位，改採用自動產生的 index
'''
#print(data.index[1], 'low')
for i in range(data.shape[0]-1):
    c_time = data.index[i]
    c_low = data.loc[c_time, 'low']
    c_high = data.loc[c_time, 'high']
    c_close = data.loc[c_time, 'close']
    c_open = data.loc[c_time, 'open']
    #取下一期資料作為進場資料
    n_time = data.index[i+1]
    n_open = data.loc[n_time, 'open']

    #進場時機：紅K、下引線為實體紅K的兩倍
    if position == 0:
        if c_close > c_open and (c_close-c_open)*2 < (c_open-c_low):
            position = 1
            order_i = 1 #持有天數
            order_time = n_time
            order_price = n_open
            order_unit = 1
            #print(c_time, '觸發進場訊號，隔日進場', order_time, '進場價：', order_price, '買入單位：', order_unit, '單位')
    #出場時機：至少持有三日、三日過後遇當日紅K即出場
    elif position == 1 :
        if c_close > c_open and i > order_i+3:
            position = 0
            cover_time = n_time
            cover_price = n_open
            #print(c_time, '觸發出場訊號，隔日出場', cover_time, '出場價：', cover_price)
            trade = trade.append(pd.Series([prod, 'Buy', order_time, order_price, cover_time, cover_price]), ignore_index=True)
print(trade)
bt.ChartTrade(data, trade)           