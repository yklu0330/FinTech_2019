## When to Buy or Sell?
- [Homework website](http://mirlab.org/jang/courses/fintech/homework/2019/whenToBuyAndSell/?count=3&dueDate=20191124%2023:59:59)
- Allow the "buy" and "sell" of several stocks of which the price is known in advance.
- Identify the best timings for "buy what" and "sell what", such that the overall return is maximized.
#### Input file
- priceMat: An m×n matrix which holds n stocks' price over m days. That is, each of the n columns is the price vector of m days for a specific stock.
- transFeeRate: Rate for transaction fee, which is usually 1/100.
#### How to run
``python rrEstimateOpen.py priceMat.txt 0.01``
#### Output
- return rate
<img src="https://i.imgur.com/5w5g3CY.jpg" width=20%>