"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
area_codes = set()
fixed_line_calls = 0
total_calls = 0

def extract_area_code(phone_number):
    if phone_number[0] == '(':
        return phone_number[1:].split(')')[0]
    elif phone_number[0] == '7' or phone_number[0] == '8' or phone_number[0] == '9':
        return phone_number[:5]
    elif phone_number[:4] =='140':
        return '140'
    else: 
        return None


def display_area_codes(codes):
    codes_in_list = list(codes)
    codes_in_list.sort()
    print("The numbers called by people in Bangalore have codes:")
    for code in codes_in_list:
        print(code)


def display_percentage_calls(nr_of_fixed_calls, total_calls):
    print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(100*nr_of_fixed_calls/total_calls))


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        if call[0][:5] == '(080)':
            total_calls += 1
            code_to_add = extract_area_code(call[1])
            if code_to_add is not None:
                area_codes.add(code_to_add)
            if call[1][:5] == '(080)':
                fixed_line_calls += 1

display_area_codes(area_codes)
            
display_percentage_calls(fixed_line_calls, total_calls)
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
