import pandas as pd 
from Data import getDataYF, getDataFM
from BackTest import ChartCandle
data = getDataFM('0050', '2021-01-01', '2021-08-31')
ChartCandle(data)