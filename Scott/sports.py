import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=3, ncols=1)

df_mlb = pd.read_csv("mlb_loc.csv")
print(df_mlb.head())
df_ECN_2002 = pd.read_csv("ECN_2002.csv")
print(df_ECN_2002.head())
df_ECN_2012 = pd.read_csv("ECN_2012.csv")
print(df_ECN_2012.head())

#---------------------------
print ("State and number of teams")
States = df_mlb.groupby('State')
TeamCount = States.Team.count()
x = df_mlb.State.unique()
print(list(df_mlb.State.unique()))
print(list(TeamCount))

plt.subplot(3,1,1)
plt.scatter(x,TeamCount,30, c='red', label='Number of teams per state')
plt.title("Number of teams per state (2018)")
plt.ylabel("Number of teams")
plt.xlabel("State")
plt.xticks(rotation=45)
#plt.show()

#---------------------------
#print("2002 - Number of business established, Annual Payroll & Number of Employees")
#States2002 = df_ECN_2002.groupby('State')
#x1 = df_ECN_2002.State.unique()
#y1 = States2002.EMP.sum()
#print(list(x1))
#print(list(y1))

#plt.subplot(3,1,2)
#plt.scatter(x1,y1,10, c='blue', label='2002 - EMPloyement per state')
#plt.title("2002 - EMPloyement per state")
#plt.ylabel("Employment")
#plt.xlabel("State")
#plt.show()

#-------------
print("2012 - Number of business established, Annual Payroll & Number of Employees")
States2012 = df_ECN_2012.groupby('State')
x2 = df_ECN_2012.State.unique()
y2 = States2012.EMP.sum()
print(list(x2))
print(list(y2))

plt.subplot(3,1,2)
plt.scatter(x2,y2,20, c='green', label='2012 - EMPloyement per State')
plt.title("2012 - EMPloyement per state ")
plt.ylabel("Employment")
plt.xlabel("State")
plt.xticks(rotation=45)
#plt.show()

#-----------

frames= [df_mlb, df_ECN_2012]
#result = pd.concat(frames, sort=False, on='State')
result = pd.merge (df_mlb, df_ECN_2012, on ='State')
myList = result.groupby('State').count().Team
myEmpList = df_ECN_2012.groupby('State').EMP.sum()
myEmploymentperTeamRatio=[]
for index in range (myList.count()):
    
    myEmploymentperTeamRatio.append(myEmpList[index]/myList[index])

x3 = result.State.unique()
y3 = myEmploymentperTeamRatio


plt.subplot(3,1,3)
plt.scatter(x3,y3,20, c='green', label='Employment/Team by State')
plt.title("Employment/Team by State")
plt.ylabel("Employment/Team")
plt.xlabel("State")
plt.xticks(rotation=45)
plt.show()
