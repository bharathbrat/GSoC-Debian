import csv
from sqlalchemy import *
import numpy as np
from matplotlib import pyplot as plt

engine = create_engine('postgresql://public-udd-mirror:\
public-udd-mirror@public-udd-mirror.xvm.mit.edu:5432/udd')
conn = engine.connect()

#retrieve all distribution values from all_packages
result = conn.execute("select last_modified from all_bugs")
last_modified = {}
print "Query done."
for row in result:
    temp1 = str(row['last_modified'].year)
    #count number of packages with last_modified in each year
    if temp1 not in last_modified.keys():
        last_modified[temp1] = 1
    else:
        last_modified[temp1] += 1


#sort values according to years
x = []    # x-axis 
y = []
for i in last_modified.keys():
    x.append(int(i))
y = last_modified.values()
data = [(str(X),Y) for (X,Y) in sorted(zip(x,y))]

myfile = open('data_csv.csv','wb')
wr = csv.writer(myfile)
for i in data:
    wr.writerow(i)
myfile.close()
