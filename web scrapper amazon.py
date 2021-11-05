#!/usr/bin/env python
# coding: utf-8

# In[4]:


#importing libraries
from bs4 import BeautifulSoup
import requests
import time
import smtplib
import datetime


# In[29]:


#connecting to website
URL="https://www.amazon.in/dp/B016ZLKJSU/ref=s9_acsd_al_bw_c2_x_1_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-14&pf_rd_r=5R2ZTHXJY13B8GADKZEK&pf_rd_t=101&pf_rd_p=d9546384-745d-44b1-b62e-1a567194bddc&pf_rd_i=1380072031"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"}
page=requests.get(URL,headers=header)
soup_1=BeautifulSoup(page.content,"html.parser")
# print(soup_1)
soup_2=BeautifulSoup(soup_1.prettify(),"html.parser")
product_title=soup_2.find(id="productTitle").get_text().strip() #stripping the empty spaces
product_price=soup_2.find(id="priceblock_ourprice").get_text().strip()[1:]
print(f"product name:{product_title}")
print(f"product price:{product_price}")


# In[13]:


#creating a timestamp to keepa track of when the data was collected
import datetime
today=datetime.date.today()
print(today)
            


# In[19]:


import csv
header=['product','price','date']
Data=[product_title,product_price,today]
with open("AmazonWebscrapperProject.csv",'w',newline='',encoding='UTF-8') as f:
    writer=csv.writer(f)
    writer.writerow(header) #inserting header
    writer.writerow(Data)  #inserting data


# In[21]:


#cheacking our dataset that we created
import pandas as pd
df=pd.read_csv(r'C:\Users\KIIT\AmazonWebscrapperProject.csv')
print(df)


# In[ ]:


#we want to append data to this dataset
with open("AmazonWebscrapperProject.csv",'a+',newline='',encoding='UTF-8') as f:
    writer=csv.writer(f)
    #we don't need to header anymore as we are just appending data to the existing dataset
    writer.writerow(Data)


# In[26]:


def Check_Prices():
    URL="https://www.amazon.in/dp/B016ZLKJSU/ref=s9_acsd_al_bw_c2_x_1_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-14&pf_rd_r=5R2ZTHXJY13B8GADKZEK&pf_rd_t=101&pf_rd_p=d9546384-745d-44b1-b62e-1a567194bddc&pf_rd_i=1380072031"
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"}
    page=requests.get(URL,headers=header)
    soup_1=BeautifulSoup(page.content,"html.parser")
    # print(soup_1)
    soup_2=BeautifulSoup(soup_1.prettify(),"html.parser")
    product_title=soup_2.find(id="productTitle").get_text().strip() #stripping the empty spaces
    product_price=soup_2.find(id="priceblock_ourprice").get_text().strip().[1:]
    import datetime
    today=datetime.date.today()
    with open("AmazonWebscrapperProject.csv",'a+',newline='',encoding='UTF-8') as f:
        writer=csv.writer(f)
        writer.writerow(Data)
    if (price<11000):
         Send_Email()
        
    

    


# In[ ]:


#this will update the data automatically every 5 sec. we can adjust the time accordingly
while(True):
    Check_Prices()
    time.sleep(5000)
    


# In[28]:


import pandas as pd
df=pd.read_csv(r'C:\Users\KIIT\AmazonWebscrapperProject.csv')
print(df)


# In[ ]:


#sends an email when the price hits your desired price range
#lets first create a function
def Send_Email():
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server start
    server.ehlo()
    server.login('anoushka.mukherjee17@gmail.com','xxxxxxxxxxxxxx')
    subject="The price of the product is now below ₹11,000,grab it !"
    body="XYZ the product you have been wanting to buy is now at your desirable range.Don't miss the chance .Link here :https://www.amazon.in/dp/B016ZLKJSU/ref=s9_acsd_al_bw_c2_x_1_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-14&pf_rd_r=5R2ZTHXJY13B8GADKZEK&pf_rd_t=101&pf_rd_p=d9546384-745d-44b1-b62e-1a567194bddc&pf_rd_i=1380072031"
    msg= f"Subject: {subject}\n\n{body}"
    server.sendmail('anoushka.mukherjee17@gmail.com',msg)
        
    

