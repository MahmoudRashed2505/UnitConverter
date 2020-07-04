sys("clear")
  print("Please Choose the Base and Converted Currencies:\n")
  with open("codes-all_csv.csv",mode='r') as csv_file:

      csv_reader = csv.DictReader(csv_file)
      line_count = 0
      for row in csv_reader:
          if line_count==0:
              print("Country Name:\t\t\tCurrency:\t\t\tAlphanetical Code:\n")
              line_count += 1
          elif line_count == 5:
              baseCurrency1 = row["AlphabeticCode"]
          elif line_count == 51:
               convertedCurrency1 = row["AlphabeticCode"]
          print("{}- {}".format(line_count,row["AlphabeticCode"]))
          line_count += 1
  with open("codes-all_csv.csv",mode='r') as csv_file:
      baseCurrency = input("Choose the Base Country: ")
      convertedCurrency = input("Which Currency to convert: ")
      line_count1 = 1
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
          if line_count1==int(baseCurrency):
             baseCurrency_word = row["AlphabeticCode"]
             print(baseCurrency)
             sys("pause")
          elif line_count1 == convertedCurrency:
             convertedCurrency_word = row["AlphabeticCode"]
             print(convertedCurrency)
             sys("pause")
          line_count1 += 1
  return baseCurrency_word,convertedCurrency_word
