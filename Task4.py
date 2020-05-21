"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
telemarketers = {}

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        telemarketers[text[0]] = False
        telemarketers[text[1]] = False

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        telemarketers[text[1]] = False
        telemarketers[text[0]] = telemarketers.get(call[0], True)

for number, is_telemarketer in telemarketers.items():
    if is_telemarketer:
        print(number)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

