
from datetime import datetime

def find_day_of_week(date_str):
    # Convert the input string to a datetime object
    date_object = datetime.strptime(date_str, '%m %d %Y')
    
    # Get the day of the week and convert it to uppercase
    day_of_week = date_object.strftime('%A').upper()
    
    return day_of_week

# Sample Input
input_date = input()

# Find and print the day of the week
output_day = find_day_of_week(input_date)
print(output_day)
