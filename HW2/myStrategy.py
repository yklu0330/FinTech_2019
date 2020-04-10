def myStrategy(pastPriceVec, currentPrice, stockType):
	# Explanation of my approach:
	# 1. Technical indicator used: RSI
	# 2. if RSI > 80 ==> sell
	# 	 if 80 > RSI > alpha ==> buy
	#    if alpha > RSI > beta ==> hold
	#    if beta > RSI > 20 ==> sell
	#    if 20 > RSI > 0 ==> buy
	# 3. Modifiable parameters: alpha, beta, and window size for RSI
	# 4. Use exhaustive search to obtain these parameter values (as shown in bestParamByExhaustiveSearch.py)
	
	import numpy as np
	# stockType='SPY', 'IAU', 'LQD', 'DSI'
	# Set parameters for different stocks
	paramSetting={'SPY': {'alpha':69, 'beta':23, 'windowSize':19},
					'IAU': {'alpha':50, 'beta':42, 'windowSize':7},
					'LQD': {'alpha':50, 'beta':20, 'windowSize':7},
					'DSI': {'alpha':74, 'beta':21, 'windowSize':19}}
	windowSize=paramSetting[stockType]['windowSize']
	alpha=paramSetting[stockType]['alpha']
	beta=paramSetting[stockType]['beta']
	
	action=0		# action=1(buy), -1(sell), 0(hold), with 0 as the default action
	dataLen=len(pastPriceVec)		# Length of the data vector

	SMAu = 0
	SMAd = 0
	RSI = 0
	
	if dataLen == 0:
		return action
	elif dataLen == 1:
		return action
	elif dataLen < windowSize:
		for i in range(dataLen-1):
			if i + 1 < dataLen:
				dif = pastPriceVec[i+1] - pastPriceVec[i]
				if dif >= 0:
					SMAu = SMAu + dif
				else:
					SMAd = SMAd + dif
	else:
		windowedData=pastPriceVec[-windowSize:]
		for i in range(windowSize):
			if i + 1 < windowSize:
				dif = windowedData[i+1] - windowedData[i]
				if dif >= 0:
					SMAu = SMAu + dif
				else:
					SMAd = SMAd + dif
	SMAu = SMAu / (dataLen - 1)
	SMAd = -SMAd / (dataLen - 1)
	if SMAu + SMAd != 0:
		RSI = SMAu / (SMAu + SMAd) * 100
	else:
		RSI = 0	

	if RSI > 80:
		action = -1
	elif RSI > alpha:
		action = 1
	elif RSI > beta:
		action = 0
	elif RSI > 20:
		action = -1
	else:
		action = 1
	return action
