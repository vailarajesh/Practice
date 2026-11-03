import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('Zomato.csv',encoding='latin-1')
#print(df.shape)
#print(df.columns)
#print(df.isnull().sum())
#print([i for i in df.columns if df[i].isnull().sum()>0])
import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
#sns.heatmap(df.isnull())
#sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#plt.show()
df_c = pd.read_excel('Country_Code.xlsx')
#print(df_c.head())
f_df = pd.merge(df,df_c,on ='Country Code',how='left')
#print(f_df.head(5))
c_names=f_df.Country.value_counts().index
#print(c_names)
c_val = f_df.Country.value_counts().values
#print(c_val)
'''plt.pie(c_val[:4],labels=c_names[:4],autopct='%1.2f%%')
plt.show()'''
#print(f_df.groupby(['Aggregate rating','Rating color','Rating text']).size())
ratings = f_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})
#print(ratings)
'''plt.figure(figsize=(8,4))
sns.barplot(x='Aggregate rating',y='Rating Count',hue ='Rating color',data=ratings)
plt.show()'''
'''plt.figure(figsize=(8,4))
sns.countplot(x='Rating color',data=ratings,palette = ['blue','red','orange','yellow','green','green'])
plt.show()'''
#print(f_df[f_df['Rating color']=='White'].groupby('Country').size().reset_index())
#print(f_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5))      
#print(f_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index())
#print(f_df[f_df['Has Online delivery']== 'Yes'].Country.value_counts())
city_v= f_df.City.value_counts().values
city_lb=f_df.City.value_counts().index
'''plt.figure(figsize=(8,5))
plt.pie(city_v[:5],labels=city_lb[:5],autopct='%1.2f%%')
plt.show()'''
loc_cus_counts = df.groupby(['City','Cuisines']).size().reset_index(name='Count')
#print(loc_cus_counts)
top_cus_loc = loc_cus_counts.groupby('City').apply(lambda x : x.nlargest(5,'Count')).reset_index(drop = True)
#print(top_cus_loc)
pop_items = df['Cuisines'].value_counts().head(5)
'''plt.figure(figsize=(8,6))
sns.barplot(x=pop_items.values,y=pop_items.index)
plt.title('Most popular items',fontsize=14)
plt.xlabel('Count')
plt.ylabel('Item Name')
plt.show()'''
top_rest = f_df[(f_df['Aggregate rating'] >= 4.5)& (f_df['Votes']> 250)]
top_rest = top_rest.sort_values(by = 'Votes',ascending=False)
#print(top_rest[['Restaurant Name','City','Country','Aggregate rating','Votes']].head(5))
city_rest_counts= f_df['City'].value_counts().head(5)
'''sns.barplot(x=city_rest_counts.values,y=city_rest_counts.index,palette='crest')
plt.title("top cities most rest")
plt.xlabel('no of rest')
plt.ylabel('City')
plt.show()'''
#print(f_df['Has Table booking'].value_counts())
tb_book_c = f_df[f_df['Has Table booking'] == 'Yes'].Country.value_counts()
#print(tb_book_c.head(5))
'''plt.figure(figsize = (8,6))
sns.scatterplot(x='Average Cost for two',y = 'Votes',data = f_df,alpha = 0.5)
plt.title(" votes vs cost for two")
plt.xlabel('avg cost for two')
plt.ylabel('no of votes')
plt.show()'''
'''top_cus_rt = f_df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending = False).head(5)
plt.figure(figsize=(8,6))
sns.barplot(x=top_cus_rt.values,y=top_cus_rt.index,palette = 'mako')
plt.title('Top 10 cus')
plt.xlabel('avg rate')
plt.ylabel('cuisines')
plt.show()'''
'''cus_costs = f_df.groupby('Cuisines')['Average Cost for two'].mean().sort_values(ascending = False).head(5)
plt.figure(figsize=(8,6))
sns.barplot(x=cus_costs.values,y = cus_costs.index,palette='flare')
plt.title('10 most expensive')
plt.xlabel('avg cost fro two')
plt.ylabel('cusinne')
plt.show()'''
