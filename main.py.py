import csv
import datetime
now = datetime.datetime.now()
current_day = str(now.day) + str(now.month)
print(current_day)
f = open('db.csv', 'r')

with f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == current_day:
            print('Happy Birthday '+ row[0])
        else:
            print('no')    
