from calendar import monthcalendar, week
from datetime import datetime
from datetime import date
import calendar

month = date.today().day
monthDay = calendar.monthrange(datetime.now().year, datetime.now().month)[1]
monthPercentage = int(month)/int(monthDay)*100

weekDay = datetime.now().isoweekday()
weekPercentage = weekDay/7*100

monthNow = datetime.today().month
yearPercentage = int(monthNow)/12*100

print("------------------------------------------------")
print("Year Progress : ", round(yearPercentage),"%")

print("Month Progress : ", round(monthPercentage),"%")

print("Week Progress : ", round(weekPercentage),"%")
print("------------------------------------------------")