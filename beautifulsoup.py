from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np


def zipScraper(strng):
    testzip=strng
    request=requests.get('http://www.incomebyzipcode.com/utah/'+testzip)
    soup=bs(request.content,'html5lib')
    table_content=soup.find_all('table')
    #print(table_content)
    median_info=table_content[0]
    avg_info=table_content[1]

    salary_info={}
    salary_info['median_salary']=median_info.td.string
    salary_info['avg_salary']=avg_info.td.string
    
    ###catch exception with '-1$'
    if salary_info['median_salary']=='-$1':
       salary_info['median_salary']='DNF'
    if salary_info['avg_salary']=='-$1':
       salary_info['avg_salary']='DNF'   
       
    return salary_info

test_code=['90210','92199','90221']
ss={}
for code in test_code:
    try:
        s=zipScraper(code)
    except:
        s={code:'zip_code_DNF!'}   
    ss[code]=s
    
print(ss)