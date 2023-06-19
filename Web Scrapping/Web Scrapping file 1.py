import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

l = "https://mtcbus.tn.gov.in/Home/routewiseinfo"

r = requests.get(l)

soup = BeautifulSoup(r.content,'html.parser')
routes = ''
r_fil = []

print(soup.get_text())

for i in soup.get_text().split("Select Routes"):
    routes += i
print(routes)
#%%
f_index = routes.find('--Route--')
f_index
t_index = routes.find('V51')
r_fil = routes[f_index:t_index+3]
r_fil = r_fil.split("\n")
r_fil.remove('--Route--')
r_fil
#%%
f = open('data_miniproj1.csv','w')
writer = csv.writer(f)  
#%%
for i in r_fil:
    URL = "https://mtcbus.tn.gov.in/Home/routewiseinfo?csrf_test_name=e1ee48d9825cb906af5ba817b3e1d808&selroute={}&submit=".format(i)
    #print(URL)
    
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,'html.parser')
    
    s = []
    x = soup.get_text()[soup.get_text().index("Routes"):soup.get_text().index("Route No.")]
    
    x = x.replace("Routes","")
    #print(x)
    s = x.split()
    places = []
   # print(s)
    temp = ' ' 
    for j in range(len(s)):
        
        if s[j].isdigit():
            places += [temp]
            temp = ' '
        else:
            temp += ' ' + s[j]
   
    
    
    writer.writerow(places)
#%%
f.close()