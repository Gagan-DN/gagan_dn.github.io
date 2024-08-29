from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
def get_Product_title(soap):
  try:
    Product_title=new_soap.find("span", attrs={'class':'VU-ZEz'}).text.strip()
  except AttributeError:
    Product_title=''
  return Product_title
def get_Product_Rating(soap):
  try:
    Product_Rating=new_soap.find("div", attrs={'class':'ipqd2A'}).text.strip()
  except AttributeError:
    Product_Rating=''
  return Product_Rating
def get_Product_Price(soap):
  try:
    Product_Price=new_soap.find("div", attrs={'class':'Nx9bqj CxhGGd'}).text.strip()
  except AttributeError:
    Product_Price=''
  return Product_Price
    
if __name__ == '__main__':
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    Headers = {
     'User-Agent': user_agent,
     'Accept-Language': 'en-us,en;q=0.5'
    }
    #flipkart.com
    url='https://www.flipkart.com/mobile-phones-store'
    web_page=requests.get(url,headers=Headers)
    #soap object containing all data
    soap=BeautifulSoup(web_page.content,'html.parser')
    #fetch links as list of tag object
    links=soap.find_all("a", attrs={'class':'wjcEIp'})
    #store links
    Links_list=[]
    #loops for extracting links from tag Object
    for link in links:
        Links_list.append(link.get('href'))
    d={'title':[],'rating':[],'price':[]}
    #loop for extracting product detailes from each link
    for link in Links_list:
        product_list='https://www.flipkart.com/mobile-phones-store/'+link
        new_webpage=requests.get(product_list,headers=Headers)
        new_soap=BeautifulSoup(new_webpage.content,'html.parser')
        #Fuction calls to display all necessary product information
        d['title'].append(get_Product_title(new_soap))
        d['rating'].append(get_Product_Rating(new_soap))
        d['price'].append(get_Product_Price(new_soap))
    fliplart_df=pd.DataFrame.from_dict(d)
    fliplart_df['title'].replace('',np.nan,inplace=True)
    fliplart_df=fliplart_df.dropna(subset={'title'})
    #fliplart_df.to_csv('scraped_data.csv', index=False)
    fliplart_df.to_csv('scraped_data.csv', header=True , index=False)