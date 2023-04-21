import requests
from bs4 import BeautifulSoup

def fetch_housing_bills(url):
    '''
    Input: website that the bill will be gotten from 
    Output: Bills from a website
    '''
    #url = "https://www.example.com/san_francisco_housing_bills"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #scrape the website for the bill.
    bills = [bill.text for bill in soup.select(".bill")]
    return bills
