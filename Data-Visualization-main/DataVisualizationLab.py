#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Download house price data set from kaggle and map the value to aesthetics

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/91975/Downloads/archive (1)/House Price India.csv")
# print(df.head())
sns.scatterplot(x="living area",y="Price",data=df,hue=df["number of bedrooms"])
plt.show()


# In[12]:


#Use different color scale on a reainfall prediction data set
# Create a different bar plots for variables in any dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/91975/Downloads/archive (2)/India_rainfall_act_dep_1901_2016_1.csv")
sns.barplot(df)
plt.xticks(rotation=45)
plt.show()


# In[18]:


# Create a trend line with a confidence band as any suitable dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df1 = pd.read_csv("C:/Users/91975/Downloads/archive (3)/Automobile_data.csv")
sns.regplot(x='length', y='city-mpg', data=df1)
plt.show()


# In[36]:


# Illustrate partial transparent and jittering

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df1 = pd.read_csv("C:/Users/91975/Downloads/archive (4)/nba2k-full.csv")
plt.figure(figsize=(20, 15))
sns.stripplot(x="height", y="weight", data=df1, jitter=True, alpha=0.7)
plt.xticks(rotation=45)
plt.yticks(rotation=360)
plt.show()


# In[ ]:




