# Jake Huggins  
# UWYO COSC 1010
# 11/4/2024 
# HW03
# Lab Section: 14
# Sources, people worked with, help given to: None


week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
num_days = {
    "January": 31,
    "February": 28,
    "FebruaryLeap": 29,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 30
}
date = ""
year = 0

def is_leap_year(year):
    return year % 4 == 0

def calc_elapse_days(month, day):
    month_index = months.index(month)
    total = round(day) - 1
    for i in range(month_index):
        if (month == months[i]):
            total += day
        else: 
            total += num_days[months[i]]
    return total

def convert_val(input):
    vals = input.split("/")
    for i in range(len(vals)):
        try:
            num = int(vals[i])
            vals[i] = num
        except:
            pass
    return vals
    
def is_valid(vals):
    try:
        if (vals[0] > len(months) or vals[0] < 1):
            return False
        month = months[vals[0] - 1]
        if (is_leap_year(vals[2]) and month == "February"):
            month += "Leap"
        if (vals[1] > num_days[month] or vals[1] < 0):
            return False
        return True
    except:
        return False

while (True):
    date = input("Please input a date in the format MM/DD/YYYY. E.g., 09/05/2004: ")
    if (not is_valid(convert_val(date))):
        print("Invalid Input!")
        continue
    break

data = convert_val(date)

month = months[data[0] - 1]
days = data[1]
year = data[2]
time = calc_elapse_days(month, days)

if is_leap_year(year):
    if (month == "February"):
        time -= 1

y = year - 1
#Jan first falls on day x where:
day = (36 + y +(y/4) - (y/100) + (y/400)) % 7

week_day = (round(day) + time) % 7
print(f"{date} is on a {week_days[week_day]}")

