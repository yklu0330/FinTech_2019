import csv
import sys


with open(sys.argv[1], newline='', encoding='Big5') as csvfile:
    dataList = csv.reader(csvfile)
    list = []
    for row in dataList:
        if row[3] >= '084500' and row[3] <= '134500' and row[1] == 'TX     ':
            list.append(row)
    list2 = []
    for i in range(len(list)):
        if list[i][2] == list[0][2]:
            list2.append(list[i])
    high = list2[0][4]
    low = list2[0][4]
    for i in range(len(list2)):
        if list2[i][4] < low:
            low = list2[i][4]
        if list2[i][4] > high:
            high = list2[i][4]
    print(list2[0][4], high, low, list2[len(list2)-1][4])
    
