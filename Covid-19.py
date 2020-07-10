from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np

def country_case(str):
	
	country = str #'US'
	request = requests.get('https://www.worldometers.info/coronavirus/country/' + country)
	soup = bs(request.content,'html5lib')
	div = soup.find_all('div',class_='maincounter-number')

	number=[]
	for i in range(3):
		number.append(div[i].span.text)

	result={}	
	result["total case"]=number[0]
	result["Death"]=number[1]
	result["recovered"]=number[2]
	#print(result)
	return result

test_coutry = ['US','brazil','india']    
s={}
for country in test_coutry:
	try:
		re = country_case(country)
		s[country]=re
	except:
		print("country name invalid")		

print(s)
# print result:
#{'US': {'total case': '3,285,506 ', 'Death': '136,556', 'recovered': '1,453,158'}, 
#'brazil': {'total case': '1,800,827 ', 'Death': '70,398', 'recovered': '1,185,596'}, 
#'india': {'total case': '822,570 ', 'Death': '22,144', 'recovered': '516,206'}}





