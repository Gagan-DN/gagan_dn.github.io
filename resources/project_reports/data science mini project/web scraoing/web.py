from bs4 import BeautifulSoup
import requests
import pandas

#flipkart.com

url='https://www.flipkart.com/mobile-phones-store'

user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
Headers = {
  'User-Agent': user_agent,
  'Accept-Language': 'en-us,en;q=0.5'
}
web_page=requests.get(url,headers=Headers)
#print(web_page.content)
print(type(web_page.content))
#soap object containing all data
soap=BeautifulSoup(web_page.content,'html.parser')
print(soap)
links=soap.find_all("a", attrs={'class':'wjcEIp'})
#print(links)
#print(links[0].get('href'))
link=links[0].get('href')
product_list='https://www.flipkart.com/mobile-phones-store/'+link
product_list
new_webpage=requests.get(product_list,headers=Headers)
#print(new_webpage)
new_soap=BeautifulSoup(new_webpage.content,'html.parser')
#print(new_soap)
Product_title=new_soap.find("span", attrs={'class':'VU-ZEz'}).text.strip()
print(Product_title)
Product_Rating=new_soap.find("div", attrs={'class':'ipqd2A'}).text.strip()
print(Product_Rating)
Product_Price=new_soap.find("div", attrs={'class':'Nx9bqj CxhGGd'}).text.strip()
print(Product_Price)
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
    

