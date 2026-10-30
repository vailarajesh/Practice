import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
df = pd.read_csv('iris_dataset.csv',sep=',')
#print(df)
#sns.histplot(data = df, x= 'petal length (cm)', bins = 30, hue ='target')
#plt.show()
#sns.scatterplot(data = df, x = 'petal length (cm)', y = 'petal width (cm)',hue = 'target')
#plt.show()
#sns.boxplot(data = df,orient = 'h')
#plt.show()
#sns.barplot(x='target',y='sepal width (cm)',data = df)
#plt.show()
#sns.regplot(x='petal length (cm)',y = 'petal width (cm)',data = df)
#plt.show()
tips = sns.load_dataset('tips')
#print(tips)
#sns.stripplot(x='day',y='total_bill',data =tips,jitter = True)
#plt.show()
ft = sns.load_dataset('flights')
#print(ft)
'''
sns.lineplot(x="year",y='passengers',data=ft,hue='month',marker ='o')
plt.title("time")
plt.xlabel('year')
plt.ylabel('no of passangers')
plt.show()
'''
#sns.pairplot(data = df,hue='target',diag_kind='kde')
#plt.show()
sns.kdeplot(data = df)
plt.show()