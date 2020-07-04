#! /usr/bin/env python3
import json
import requests
import csv
from os import system as sys
token = "&compact=ultra&apiKey=52456c84f29257e83786"
url = "https://free.currconv.com/api/v7/convert?q="
#headers =
def convert(baseCurrency,convertedCurrency,amount):
    sys("clear")
    api_url = url+baseCurrency+'_'+convertedCurrency+token
    print(api_url)
    response = requests.get(api_url)
    convert_rate = json.loads(response.content.decode('utf-8'))
    rate = 0
    for conversion,value in convert_rate.items():
        rate = value
    return float(amount)*float(rate)

def get_currencies():


sys("clear")
get_currencies()
#amountToBeConverted = input("Enter Amount: ")
#baseCurrency,convertedCurrency = get_currencies()
#convertedAmount=convert(baseCurrency,convertedCurrency,amountToBeConverted)
#print("{} From {} To {} = {}\n".format(amountToBeConverted,baseCurrency,convertedCurrency,convertedAmount))
