# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:24:10 2023

@author: SONIA
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#how to read an excel or xlsx file
data= pd.read_excel('articles.xlsx')

#get sumary of the data
data.describe()

#get the summary of the columns
data.info()

#how to sceck the numbr of articles written per source
#format of groupby- dataframe.groupby(["column to group"])["column to count"].count()
data.groupby(["source_id"])["article_id"].count()

#number of reactions per publisher
data.groupby(["source_id"])["engagement_reaction_count"].sum()

#how to remove or drop an entire column
data=data.drop('engagement_comment_plugin_count',axis=1)

#working eith functions in python
def Thisfunction():
    print ("This is my first function")
Thisfunction()

#creating a function with variables

def Aboutme(name , surname , location ):
    print("This is " + name + 'My Surname is ' + surname + 'I am from '+ location )
    return name, surname, location

a= Aboutme("Sonia ", 'Njoku ', 'Nigeria')

#using for loops in functions
def Favfood(food):
    for x in food:
        print('top foood is '+ x)
        
Fastfood= ['burgers' , 'pizza', 'pie']
Favfood(Fastfood)
           
# creating a key word flag using for loops
# keyword = 'crash'
# keyword_flag= []
# for x in range(0,10):
#     heading = data['title'] [x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag= 0
#     keyword_flag.append(flag)    
        
#creating a function to flag the entire data of title row
def keywordflag(keyword):
    length = len(data)    
    keyword_flag= []
    for x in range(0,length):
        heading = data['title'] [x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag= 0
        except:
            flag= 0
        keyword_flag.append(flag) 
    return keyword_flag     
k= keywordflag('murder')
           
#creating a new column in the dataframe
data['keyword_flag']= pd.Series(k)           
           
# SentimentIntensityAnalyzer
sent_int =  SentimentIntensityAnalyzer()
           
text = data['title'][16]
sent = sent_int.polarity_scores(text)           
#in other to make it separate variables on its own           
neg = sent['neg']           
pos = sent['pos']
neu = sent['neu']           
           
#using a for loop to extract sentiment 
title_neg_sentiment= []
title_pos_sentiment= []
title_neu_sentiment= []

lenth = len(data)

for x in range(0,lenth):
    try:
        sent_int =  SentimentIntensityAnalyzer()
        text = data['title'][x]
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']           
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
#transforming the list to series so we can add it to the dataframe as a column    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_pos_sentiment = pd.Series(title_neu_sentiment)   
    
data['title_neg_sentiment']= title_neg_sentiment
data['title_pos_sentiment']= title_pos_sentiment
data['title_neu_sentiment']= title_neu_sentiment      
           
#transforming the data to an excell file           
data.to_excel('blogme_clean.xlsx', sheet_name= 'blogmedata', index=False)        
        
        
        
        
        
        
        












