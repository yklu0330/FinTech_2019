import sys
import numpy as np
import pandas as pd
import talib as ta
from talib import abstract
import matplotlib.pyplot as plt

def myStrategy(dailyOhlcvFile,minutelyOhlcvFile,openPricev):
	
	action = 0

	temp1 = ta.SMA(dailyOhlcvFile['close'], 7)
	longMA = temp1.iloc[-1]

	temp2 = ta.SMA(dailyOhlcvFile['close'], 3)
	shortMA = temp2.iloc[-1]

	rsi = ta.RSI(dailyOhlcvFile['close'], 3)
	curRSI = rsi.iloc[-1]
	prevRSI = rsi.iloc[-2]

	if (longMA < shortMA) & (openPricev > shortMA) & (curRSI > 85) & (prevRSI < 80):
		action = -1
	elif (longMA > shortMA) & (openPricev < shortMA) & (curRSI > 25) & (prevRSI < 20):
		action = 1
	else:
		action = 0

	# print("%f %f" %(curK, curD))
	# print("%s %f %f %d" %(dailyOhlcvFile.iloc[-1, 0], prevRSI, curRSI, action))

	# if dailyOhlcvFile.iloc[-1]['trading_point'] == '2019-12-13':
	# 	# longMAplot = temp1.iloc[-30:-1].values.tolist()
	# 	# shortMAplot = temp2.iloc[-30:-1].values.tolist()
	# 	rsiPlot = rsi.iloc[-30:-1].values.tolist()
	# 	day = np.array(dailyOhlcvFile.iloc[-30:-1]['trading_point']).tolist()
	# 	# plt.plot(day, longMAplot, color = 'r', label="7MA", linewidth = 1)
	# 	# plt.plot(day, shortMAplot, color = 'b', label="3MA", linewidth = 1)
	# 	# plt.xlabel("day", fontsize=12)
	# 	# plt.ylabel("MA", fontsize=12)
	# 	# plt.xticks(rotation='vertical')
		
	# 	# plt.legend(loc = "best", fontsize=12)
	# 	# plt.show()
	# 	plt.plot(day, rsiPlot, color = 'r', label="RSI", linewidth = 1)
	# 	plt.xlabel("day", fontsize=12)
	# 	plt.ylabel("RSI", fontsize=12)
	# 	plt.xticks(rotation='vertical')
		
	# 	plt.legend(loc = "best", fontsize=12)
	# 	plt.show()


	return action



