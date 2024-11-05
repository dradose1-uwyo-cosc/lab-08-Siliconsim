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
year = 0
string = "9/5/2023"

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
            print("Not a number!")
    return vals
    
def is_valid(vals):
    if (vals[0] > len(months) or vals[0] < 1):
        return False
    month = months[vals[0] - 1]
    if (is_leap_year(vals[2]) and month == "February"):
        month += "Leap"
    
    if (vals[1] > num_days[month] or vals[1] < 0):
        return False
    return True

time = 0
data = convert_val(string)

month = months[data[0] - 1]
days = data[1]
year = data[2]

print(is_leap_year(year))
if is_leap_year(year):
    time -= 1
    if (month == "February"):
        month += "Leap"

print(month)
time = calc_elapse_days(month, days)
num_week_days = (time // 7) * 7

y = year - 1
#Jan first falls on day x where:
day = (36 + y +(y/4) - (y/100) + (y/400)) % 7
print(round(day))
print(round(day) + ((time) - num_week_days))
print(((time) - num_week_days) + 2)

week_day = (round(day) + time) % 7
print(week_days[week_day])

#print(week_days[round(day) - 1])

