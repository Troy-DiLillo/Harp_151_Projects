#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Lab 9. Use some cleaning techniques. Commment some uses for the dataset. 
#Part 1: Use this CSV of AirBNB data from NYC [original source]
#Use some of the cleaning techniques we used this week: write in a comment what could be some uses for this dataset (1pt), 
#use a seaborn map to find all the NaN values (1pt), replace those NaN values (1pt), 
#isolate just the year from the last_review column (1pt), 
#and do one other thing with the dataset of your choosing (1pt)


import pandas as pd
import csv
import seaborn as sns
airbnb_df = pd.read_csv("AB_NYC_2019 - AB_NYC_2019.csv")
airbnb_df


# In[10]:


cols = airbnb_df.columns #creating a list of columns 
sns.heatmap(airbnb_df[cols].isnull()) #checking for null values


# In[13]:


airbnb_df["last_review"] = airbnb_df["last_review"].fillna("No Review Found")
airbnb_df["reviews_per_month"] = airbnb_df["reviews_per_month"].fillna("No Reviews per month Found")
airbnb_df


# In[14]:


airbnb_df2 = airbnb_df.copy()


# In[16]:


airbnb_df2.last_review = airbnb_df2.last_review.str[0:4]
airbnb_df2


# In[17]:


airbnb_df3 = airbnb_df2.copy()


# In[18]:


suites = airbnb_df3["neighbourhood_group"]
suite = {}

for i in suites:
  if i not in suite:
    suite[i] =1
  else:
    suite[i] += 1

print(suite)


# In[9]:


#Part 2: Try and create your own parser for an API. 
#If you are using an API for your project, build one for it; 
#if you are not, choose an API that makes sense to you or is related to your project in some way. 
#Include at least five functions for 1pt each.

#Using the wikipedia api parser that my group has investigated using for our project. Specifically found by Sharon and Rami. These were the functions we agreed may come up in our project.

import requests
import json
get_ipython().system('pip3 install wikipedia-api')
import wikipediaapi
#Used the Wikipedia API: 
#https://pypi.org/project/Wikipedia-API/


def get_data():  #gets the data we will be looking through in the english langUAGE/from the english wikipedia
    global response
    response = wikipediaapi.Wikipedia('en')
    return response

def single_page(response, wiki_page): 
    page = response.page(wiki_page)
    return page

def page_exist(response, wiki_page): #Checks to see if the page exists
    exist = response.page(wiki_page).exists()
    return exist

def page_url(response, wiki_page): #the URL of the page we are searching on wikipedia
    url = response.page(wiki_page).fullurl
    return url

def page_sum(response, wiki_page): #a portion of the summary section of our chosen page
    title = response.page(wiki_page).title
    summ = response.page(wiki_page).summary[0:100]
    return title, summ
   
def sect_title(response, wiki_page, section): #can enter the title of a section to get a little chunk of that. Simmilar to our summary
    page = response.page(wiki_page)
    sect = page.section_by_title(section)
    return sect.title, sect.text[0:100]

    
   
get_data() #choose our page in the strings below
print(single_page(response, "Citations"))
print(page_exist(response, "Citations"))
print(page_url(response, "Citations"))
print(page_sum(response, "Citations"))
print(sect_title(response, "Citations", "Systems"))


# In[ ]:





# In[ ]:




