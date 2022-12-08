#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


Car=pd.read_csv(r'C:\Users\Hp\Desktop\Python Project\Car_Sales_data_analysis\Cars_sales_Data1.csv')


# In[13]:


Car.head()


# In[6]:


Car.shape


# In[ ]:


#Instruction for data Cleaning 
#Find all the null values in dataset. If there is any null value in any coloumn then fill the 
column with the mean of that coloumn 


# In[16]:


Car.isnull().sum()


# In[18]:


Car['Cylinders'].fillna(Car['Cylinders'].mean())


# In[ ]:


# Based on Value count function
What are the different type of maker are there in dataset and what is the count (occurance) of each make in the data


# In[22]:


Car.head(2)


# In[24]:


Car['Make'].value_counts()


# In[ ]:


# fitering 
Show all the records rigin of asia or europe


# In[27]:


Car[Car['Origin'].isin(['Asia', 'Europe'])]


# In[ ]:


#Remove all  the record where weight is above 4000


# In[28]:


Car.head(2)


# In[31]:


Car[~(Car['Weight'] > 4000)]


# In[ ]:


#5. Instruction applying function
Increase all the values of MPG_City by 3


# In[33]:


Car.head(2)


# In[34]:


Car['MPG_City'].apply(lambda x:x+3)


# In[ ]:




