from sqlalchemy import *
import numpy as np
from matplotlib import pyplot as plt

engine = create_engine('postgresql://public-udd-mirror:\
public-udd-mirror@public-udd-mirror.xvm.mit.edu:5432/udd')
conn = engine.connect()

#retrieve all distribution values from all_packages
result = conn.execute("select distribution from all_packages")
distribution = {}

#count number of packages in each distribution
for row in result:
    if (row['distribution'] not in distribution.keys()):
        distribution[row['distribution']] = 1
    else:
        distribution[row['distribution']] += 1

#plot a pie chart
plt.pie(distribution.values(), labels = distribution.keys())
plt.title("No. of packages in each distribution:")
plt.axis('equal')
plt.show()


#retrieve last_modified and severity values for all bugs in all_bugs
result = conn.execute("select id, last_modified, severity from all_bugs")
i = 0
last_modified = {}
severity = {}

for row in result:
    temp1 = str(row['last_modified'].year)
    temp2 = str(row['severity'])
    #count number of packages with last_modified in each year
    if temp1 not in last_modified.keys():
        last_modified[temp1] = 1
    else:
        last_modified[temp1] += 1
    #count number of packages under each severity type
    if temp2 not in severity.keys():
        severity[temp2] = 1
    else:
        severity[temp2] += 1

#plot pie chart for severity values
plt.pie(severity.values(), labels = severity.keys())
plt.title("No. of bugs in each kind of severity")
plt.axis('equal')
plt.show()

#sort values according to years
x = []    # x-axis 
y = []
for i in last_modified.keys():
    x.append(int(i))
y = last_modified.values()
y = [Y for (X,Y) in sorted(zip(x,y))]
x.sort()

#plot bar chart
plt.bar(x,y)
plt.ylabel('Number of Bugs')
plt.xlabel('Year')
plt.xticks(range(min(x),max(x)+1),range(min(x),max(x)+1), horizontalalignment = 'left')
plt.title("Number of Bugs vs Modified date (Year)")
plt.show()
