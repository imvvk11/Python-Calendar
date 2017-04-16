import calendar
bc = calendar.TextCalendar(firstweekday=0)
year = input("Enter year: ")
def cal(year):
    return bc.formatyear(year, 2, 1, 6, 3)
print(cal(year))

print(input("click enter to exit_ " ))


    

