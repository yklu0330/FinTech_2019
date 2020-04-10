## OHLC Extraction
- [Homework website](http://mirlab.org/jang/courses/fintech/homework/2019/ohlc/?count=1&dueDate=20190929%2023:59:59)
- Compute the OHLC (open, high, low, close) prices of 台指期 within a given date based on minute-based trading record
#### Input file
- A csv file recording minute-based trading data, which can be download from [前30個交易日期貨每筆成交資料](https://https://www.taifex.com.tw/cht/3/dlFutPrevious30DaysSalesData)
#### How to run
``python ohlcExtract.py input.csv``
#### Output format
- The vector of OHLC in a line
<img src="https://i.imgur.com/lvvp29l.jpg" width=30%>
