import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt
'''語法：
drop_duplicates() --> 去除重複項
concat() --> 合併
''' 
def ChartCandle(data,addp=[]):
    #將K線改為"漲紅跌綠"
    mcolor = mpf.make_marketcolors(up='r', down='g', inherit=True)
    mstyle = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mcolor)
    mpf.plot(data,addplot=addp,style=mstyle,type='candle',volume=True)
#繪製交易記錄圖
def ChartTrade(data, trade=pd.DataFrame(), addp=[], v_enable=True):
    addp=addp.copy()
    copy_data=data.copy()
    if trade.shape[0] > 0:
        copy_trade =trade.copy()
        #取出進場資訊，透過時間索引進行合併
        buy_order_trade = copy_trade[[2, 3]]
        buy_order_trade = buy_order_trade.set_index(2)
        buy_order_trade.columns = ['buy_order']
        buy_order_trade = buy_order_trade.drop_duplicates()
        #取出出場資訊，透過時間索引進行合併
        buy_cover_trade = copy_trade[[4, 5]]
        buy_cover_trade = buy_cover_trade.set_index(4)
        buy_cover_trade.columns = ['buy_cover']
        buy_cover_trade =buy_cover_trade.drop_duplicates()
        #交易紀錄與K線彙整
        copy_data = pd.concat([copy_data, buy_order_trade, buy_cover_trade], axis=1)
        #副圖繪製
        addp.append(mpf.make_addplot(copy_data['buy_order'], type='scatter', color='#FF4500', marker='^', markersize=50))

        addp.append(mpf.make_addplot(copy_data['buy_cover'],type='scatter',color='#16982B',marker='v',markersize=50))
    #將K線改為"漲紅跌綠"
    mcolor = mpf.make_marketcolors(up='r', down='g', inherit=True)
    mstyle = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mcolor)
    mpf.plot(copy_data, addplot=addp, type='candle', style=mstyle, volume=v_enable)
