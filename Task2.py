"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
telephone_durations = {}
max_time = 0
max_telephone = None

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        # note: can make this into a function to remove duplicates
        telephone_durations[call[0]] = int(call[3]) + int(telephone_durations.get(call[0], 0))
        if telephone_durations[call[0]] > max_time:
            max_time = telephone_durations[call[0]]
            max_telephone = call[0]
        telephone_durations[call[1]] = int(call[3]) + int(telephone_durations.get(call[1], 0))
        if telephone_durations[call[0]] > max_time:
            max_time = telephone_durations[call[0]]
            max_telephone = call[0]
        
        

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_telephone, max_time))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

