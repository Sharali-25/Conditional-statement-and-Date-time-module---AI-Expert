city = input("Enter the city name : ")
temp = float(input("Enter the temp : "))
if temp > 35 :
    print("The weather is very HOT today")

if temp > 25 :
    print("Great day, go outside")
else :
    print("Grab a light jacket when you go outside")

# part 4 if elif else
if temp > 35 :
    print("Weather is too hot")
elif temp > 25 :
    print("Weather is cool and breezy")
else :
    print("Weather is cold - stay warm!")

# part 5 datetime and calendar
import datetime
import calendar
now= datetime.datetime.now()
print("City :",city)
print("Time now :", now)
print(calendar.calendar(now.year))