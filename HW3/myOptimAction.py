import numpy as np

def myOptimAction(priceMat, transFeeRate):
    # Explanation of my approach:
	# 1. Technical indicator used: Dynamic Programming
	# 2. p: stock price of each stock at each stage
    #    s: max stockholdings of each stock at each stage 
    #    c: max cash at each stage
    # 3. Compute s and c by recurrence
    #    Initialization:
    #     c[0] = 1000, p = priceMat(the input data: "priceMat.txt"), s[0][i] = c[0] / p[0][i] * (1-fee)
    #    Recurrence:
    #     c[i] = max{s[i-1]*p[i][0]*(1-fee), s[i-1]*p[i][1]*(1-fee), ..., s[i-1]*p[i][n-1]*(1-fee), c[i-1]},
    #           where i is the index of day, n is the number of stock
    #     s[i][j] = max{c[i]/p[i][j], s[i-1][j]},
    #           where i is the index of day, j is the index of each stock
    # 4. I also record the track of each c and s during the recurrence, to know how to get the optimal solution of c and s.
    #    Backtracking: From the final cash, find out which stock to sell to have the final cash,
    #           what time to buy the stock, ..., and so on until day0, i.e. the first day.
    # 5. By backtracking, I can know what time to buy and sell the stocks, which help me to get high return rate.
    cash = 1000
    
    dataLen, stockCount = priceMat.shape  # day size & stock count
    actionMat = []  # An k-by-4 action matrix which holds k transaction records.
    s = np.zeros((dataLen, stockCount))
    c = np.zeros((dataLen, 1))
    p = priceMat

    c[0] = cash
    for i in range(stockCount):
        s[0][i] = c[0] / p[0][i]

    trackMat = np.ones([dataLen, stockCount+1])
    trackMat[0][stockCount] = -1
    
    for i in range(1, dataLen):
        # update cash
        maxCash = 0
        maxCashIdx = 0 # -1: from previous cash (hold)
        
        for j in range(stockCount):
            if s[i-1][j] * p[i][j] * (1-transFeeRate) > maxCash:
                maxCash = s[i-1][j] * p[i][j] * (1-transFeeRate)
                maxCashIdx = j
        if c[i-1] > maxCash: # hold, no action
            maxCash = c[i-1]
            maxCashIdx = -1
        
        c[i] = maxCash
        trackMat[i][stockCount] = maxCashIdx

        # update stock
        for j in range(stockCount):
            maxStock = 0
            maxStockIdx = 0
            if c[i] / p[i][j] * (1-transFeeRate) > maxStock:
                maxStock = c[i] / p[i][j] * (1-transFeeRate)
                maxStockIdx = 1

            if s[i-1][j] > maxStock: # hold, no action
                maxStock = s[i-1][j]
                maxStockIdx = -1

            s[i][j] = maxStock
            trackMat[i][j] = maxStockIdx

    # backtracking
    searchCash = 1
    searchStock = 0
    buyStock = 0
    for i in range(trackMat.shape[0]-1, 0, -1):
        if searchCash == 1:
            if trackMat[i][stockCount] == -1:
                continue;
            else:
                buyStock = int(trackMat[i][stockCount])
                actionMat.append([i, int(buyStock), -1, s[i][int(buyStock)] * p[i][int(buyStock)] / (1-transFeeRate)])
                searchStock = 1
                searchCash = 0
        elif searchStock == 1:
            if trackMat[i][int(buyStock)] == 1:
                actionMat.append([i, -1, int(buyStock), s[i][int(buyStock)] * p[i][int(buyStock)] / (1-transFeeRate)])
                if trackMat[i][stockCount] != -1:
                    buyStock = trackMat[i][stockCount]
                    actionMat.append([i, int(buyStock), -1, s[i][int(buyStock)] * p[i][int(buyStock)] / (1-transFeeRate)])
                else:
                    searchStock = 0
                    searchCash = 1
    
    actionMat.reverse()
    return actionMat

    