## Profit Optimization for SPY Trading

- Design trading strategies such that the total return of 4 stocks over a given period of time can be maximized

### My strategy
1. Technical indicator used: RSI  
2. if RSI > 80 => sell  
if 80 > RSI > alpha => buy  
if alpha > RSI > beta => hold  
if beta > RSI > 20 => sell  
if 20 > RSI > 0 => buy  
3. Modifiable parameters: alpha, beta, and window size for RSI  
4. Use exhaustive search to obtain these parameter values  

#### Input file
- 4 stocks for evaluation
    - [SPY](https://finance.yahoo.com/quote/SPY/history?period1=1104508800&period2=1569859200&interval=1d&filter=history&frequency=1d)
    - [IAU](https://finance.yahoo.com/quote/IAU/history?period1=1104508800&period2=1569859200&interval=1d&filter=history&frequency=1d)
    - [LQD](https://finance.yahoo.com/quote/LQD/history?period1=1104508800&period2=1569859200&interval=1d&filter=history&frequency=1d)
    - [DSI](https://finance.yahoo.com/quote/DSI/history?period1=1104508800&period2=1569859200&interval=1d&filter=history&frequency=1d)
#### How to run
``python rrEstimateAll.py``
#### Output format
- Input file name and its return rate by my strategy
<img src="https://i.imgur.com/NUHbOz6.jpg" width=20%>

