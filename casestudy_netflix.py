import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
netflix = pd.read_csv('netflix_titles.csv')
#print(netflix)
#print(netflix.info())
#print(netflix.describe())
#print(netflix.duplicated().sum())
#print(netflix.isna().sum())
import warnings 
warnings.filterwarnings('ignore')
netflix['director'] = netflix['director'].fillna('unknown')
#print(netflix.director)
netflix['cast'] = netflix['cast'].fillna('unknown')
#print(netflix.cast)
netflix['country'] = netflix['country'].fillna('unknown')
netflix['date_added'] = netflix['date_added'].fillna('unknown')
#print(netflix.country)
#print(netflix.date_added)
#print(netflix.isna().sum())
#print(netflix['type'].unique())
#print(netflix['type'].value_counts())
#print(netflix['type'].value_counts().index)
#print(netflix['type'].value_counts().values)
'''
plt.figure(figsize=(6,6))
sns.countplot(data = netflix,x='type')
plt.title('contest')
plt.xlabel("type")
plt.ylabel('count')
plt.show()
'''
'''plt.figure(figsize=(5,5))
plt.pie(netflix['type'].value_counts(),
        labels=netflix['type'].value_counts().index,
        autopct = '%.2f',textprops={'fontsize':10})
plt.legend()
plt.show()'''
ld = netflix[['type','release_year']]
ld = ld.rename(columns={'release_year':'Release Year'})
ld=ld[ld['Release Year']>=2013]
#print(ld)
ldf= ld.groupby('Release Year')['type'].size().reset_index()
ldf=pd.DataFrame(ldf)
ldf.rename(columns={'type':'Total Content'},inplace=True)
l=ld.groupby('Release Year')['type'].value_counts()
#print(l)
'''
plt.figure(figsize=(10,6))
cplt = sns.countplot(x='Release Year',data = ld,hue='type',palette='pastel')
cplt.set(title='Type of Content ')
#plt.show()'''
'''plt.figure(figsize=(10,6))
ptc=sns.lineplot(x='Release Year',y='Total Content',data =ldf,linewidth=1)
ptc.set(xlabel='Release Year',ylabel='Total Content',title='Trend of content')
plt.show()'''
'''
plt.figure(figsize=(10,8))
cbp=sns.barplot(x=netflix['country'].value_counts()[:5].values,
                y=netflix['country'].value_counts()[:5].index,palette='pastel')
for i in cbp.containers:
    cbp.bar_label(i)
plt.show()
'''
#print(netflix['rating'].unique())
#print(netflix['rating'].value_counts()<=1)
new_catg={ 'PG-13':'Teens', 'TV-MA':'Mature aud','PG':'Teens','TV-14':'Teens',
          'TV-PG':'Parental aud','TV-Y':'General aud','TV-Y7':'Teens',
          'R':'Mature aud','TV-G':'General aud','G':'General aud',
          'NC-17':'Mature aud','NR':'Mature aud','TV-Y7-FV':'Teens','UR':'Mature aud'}
netflix['rating']=netflix['rating'].replace(new_catg)
netflix['rating']=netflix['rating'][~netflix['rating'].isin(['74 min','84 min','66 min'])]
#print(netflix['rating'])
'''
plt.figure(figsize=(10,6))
sns.countplot(x='rating',data=netflix,palette='pastel')
plt.title('count od Rating')
plt.show()
plt.figure(figsize=(8,6))
sns.countplot(x='rating',hue='type',data=netflix)
plt.title('relp ptype and rating')
plt.show()
'''
#netflix['rating'].value_counts().plot.pie(autopct='%1.1f%%',shadow = True,figsize=(8,6),startangle=90)
#plt.show()
netflix['date_added']= pd.to_datetime(netflix['date_added'],errors='coerce')
#print(netflix['date_added'])
netflix['year_added']=netflix['date_added'].dt.year
#sns.countplot(y='year_added',data=netflix)
#plt.show()
from collections import Counter
topdir = netflix[netflix['director'] != 'unknown']['director'].value_counts().head(10)
#print(topdir)
#topdir.plot(kind='barh',figsize=(8,5),title='top 10 dir')
#plt.show()
'''
from wordcloud import WordCloud
text = " ".join(netflix['description'].dropna())
wc = WordCloud(width = 800,height=400,background_color='white').generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.title('wc of netflix')
plt.show()'''
netflix['duration'].value_counts()
nm = netflix[netflix['type']=='Movie']
#print(nm)
nm['duration_mins']= nm['duration'].str.extract('(\d+)').astype(float)
#print(nm['duration_mins'])
'''
plt.figure(figsize=(10,6))
sns.histplot(nm['duration_mins'],bins=30,kde=True)
plt.title('Distribution of movies')
plt.xlabel('Duration(min)')
plt.show()'''
netflix['date_added']=pd.to_datetime(netflix['date_added'],errors='coerce')
netflix['year_added']=netflix['date_added'].dt.year
netflix['month_added']=netflix['date_added'].dt.month_name()
#print(netflix['year_added'])
#print(netflix['month_added'])
'''plt.figure(figsize=(8,4))
#sns.countplot(x='year_added',data=netflix,palette='pastel')
#plt.title('num of titles added by year')
sns.countplot(x='month_added',data=netflix,order=pd.date_range('2023-01-01',periods=12,freq='ME').strftime('%B'),palette='pastel')
plt.title('no of titles added by month')
plt.xticks(rotation =45)
plt.show()'''
from collections import Counter
cast_list = netflix[netflix['cast']!='unknown']['cast'].str.split(',')
flat_cast = [actor for sublist in cast_list for actor in sublist]
top_a = pd.DataFrame(Counter(flat_cast).most_common(10),columns=['Actor','Count'])
#print(top_a.head(10))
'''plt.figure(figsize=(8,4))
sns.barplot(y='Actor',x='Count',data = top,palette='pastel')
plt.title('top 10 most freq actors')
plt.show()'''
c_typ=netflix.groupby(['country','type']).size().unstack().fillna(0)
top_c = netflix['country'].value_counts().head(5).index
c_typ = c_typ.loc[top_c]
c_typ.plot(kind='bar',figsize =(8,4),stacked=True,colormap='Pastel1')
plt.title('top 5 countries')
plt.xlabel("country")
plt.ylabel('no:of titles')
plt.xticks(rotation = 45)
plt.legend(title='Type')
plt.show()