import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('scraped_data.csv')
#print(data)
#graph plots
print(data.head(5))
phone=data['title'].values
rating=data['rating'].values
price=data['price'].values
#print(phone)
#print(rating)
#simple plot
plt.plot(phone,rating,marker="*",color='green',mec='r')
plt.xlabel('phone')
plt.ylabel('Rating')
plt.title('phone Vs Rating')
plt.show()
#horizontal bar graph
plt.barh(phone,rating,color='red')
plt.xlabel('phone')
plt.ylabel('Rating')
plt.title('phone Vs Rating')
plt.show()
#simple plot
plt.plot(rating,price,marker="*",color='pink',mec='green')
plt.xlabel('Rating')
plt.ylabel('Price')
plt.title('Rating Vs Price')
plt.show()
#horizontal bar graph
plt.barh(price,rating,color='green')
plt.xlabel('Rating')
plt.ylabel('Price')
plt.title('Rating Vs Price')
plt.show()
#simple plot
plt.plot(phone,price,marker="*",color='blue',mec='orange')
plt.xlabel('Phone')
plt.ylabel('Rating')
plt.title('Phone Vs Rating')
plt.show()
#horizontal bar graph
plt.barh(phone,price,color='green')
plt.xlabel('Phone')
plt.ylabel('Rating')
plt.title('Phone Vs Rating')
plt.show()