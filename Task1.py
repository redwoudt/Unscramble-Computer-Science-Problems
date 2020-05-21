"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

all_telephone_numbers = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        all_telephone_numbers.add(text[0])
        all_telephone_numbers.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        all_telephone_numbers.add(call[0])
        all_telephone_numbers.add(call[1])

print("There are {} different telephone numbers in the records.".format(len(all_telephone_numbers)))


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
