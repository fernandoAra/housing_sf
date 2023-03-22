import requests
from bs4 import BeautifulSoup

def fetch_housing_bills():
    url = "https://www.example.com/san_francisco_housing_bills"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    bills = [bill.text for bill in soup.select(".bill")]
    return bills