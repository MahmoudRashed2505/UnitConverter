import requests
from bs4 import BeautifulSoup

def get_shorted():
    url = "https://tinyurl.com/create.php?url="
    long_url = input("Enter long url: ")
    response = requests.get(url+long_url)

    soup = BeautifulSoup(response.content,'html.parser')

    link = soup.find_all('b')
    print("Original url: {}\nShorten url: {}".format(long_url,str(link[1])[3:-4]))