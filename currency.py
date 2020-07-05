import json
import requests
import csv
from os import system as sys

token = "&compact=ultra&apiKey=52456c84f29257e83786"
url = "https://free.currconv.com/api/v7/convert?q="
def convert(baseCurrency,convertedCurrency,amount):
    sys("clear")
    api_url = url+baseCurrency+'_'+convertedCurrency+token
    response = requests.get(api_url)
    convert_rate = json.loads(response.content.decode('utf-8'))
    rate = 0
    for conversion,value in convert_rate.items():
        rate = value
    return float(amount)*float(rate)

def choose_currency():
    sys("clear")
    alphacode = []
    print("Please Choose the Base and Converted Currencies:\n")
    with open("codes-all_csv.csv",mode='r') as csv_file:
          csv_reader = csv.DictReader(csv_file)
          line_count = 0
          for row in csv_reader:
              if line_count==0:
                 print("Country Name:\t\t\tCurrency:\n")
                 line_count += 1
              print("{}- {}----> {}".format(line_count,row['Entity'],row["AlphabeticCode"]))
              alphacode.append(row["AlphabeticCode"])
              line_count += 1
    baseCurrency = input("\n\nEnter the Base Currency: ")
    convertedCurrency = input("Which Currency do you want to convert to: ")
    return baseCurrency,convertedCurrency

def convertCurrency():
    sys("clear")
    amountToBeConverted = input("Enter Amount: ")
    baseCurrency,convertedCurrency = choose_currency()
    convertedAmount=convert(baseCurrency,convertedCurrency,amountToBeConverted)
    print("{} {} = {:.3f} {} \n".format(amountToBeConverted,baseCurrency,convertedAmount,convertedCurrency))
