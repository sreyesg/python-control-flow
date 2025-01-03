months = [{"JAN": 1}, {"FEB": 2}, {"MAR": 3}, {"APR": 4},
          {"MAY": 5}, {"JUN": 6}, {"JUL": 7}, {"AUG": 8},
          {"SEP": 9}, {"OCT": 10}, {"NOV": 11}, {"DEC": 12}]
'''
for idx, obj in enumerate(months):
    if 'JAN' in obj:
        print(obj) 
'''

'''

months = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4,
          "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8,
          "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}

month = input("please enter a month ")

print(months[month.upper()])
'''
letters = ["a","b","c"]
def checker():
    if "a" in letters:
        print("popo")

checker()