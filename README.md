# Beautifulsoup
Two simple examples to show how to use beautifulsoup library to extract data from web.

First example, getting income information by entering ZIP code. The data extract from https://www.incomebyzipcode.com/
Second example, getting covid-19 real-time data by entering country name. The data extract from https://www.worldometers.info/coronavirus/country/

# Install beautiful soup
```bash
$ pip install beautifulsoup4
```
# Install html5lib 
pure-Python html5lib, which parses HTML the way a wed browser does.
```bash
$ pip install html5lib
```
# Making the soup
```python
from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>a web page</html>")
```
# Navigating using tag names
```python
soup.head
# <head><title>...........</title></head>
soup.title
# <title>............</title>

soup.find_all('table')
#<table class="table">
#              <tbody><tr>
#                <th>84057</th>
#                  <th class="text-right">Lindon</th>
#                  <th class="text-right">Orem</th>
#                  <th class="text-right">Vineyard</th>
#                  <th class="text-right">Utah County</th>
#              </tr>
#              <tr>
#                <td class="hilite">$56,668</td>
#                  <td class="text-right">$85,671</td>
#                  <td class="text-right">$61,373</td>
#                  <td class="text-right">$80,461</td>
#                  <td class="text-right">$70,408</td>
#              </tr>
#            </tbody></table>, <table class="table">
```
# Content
```python
median_info = table_content[0]
avg_info = table_content[1]
```
# Create a dictionary to store data
```python
salary_info={}
salary_info['median_salary']=median_info.td.string
salary_info['avg_salary']=avg_info.td.string
```
# Run function and print result
```python
test_code=['90210','92199','90221']
result = {}
for code in test_code:
    try:
        s=zipScraper(code)
    except:
        s={code:'zip_code_DNF!'}   
    result[code]=s
    
print(result)
```
{'90210': {'median_salary': '$143,542', 'avg_salary': '$285,015'}, '92199': {'92199': 'zip_code_DNF!'}, '90221': {'median_salary': '$48,762', 'avg_salary': '$59,127'}}



