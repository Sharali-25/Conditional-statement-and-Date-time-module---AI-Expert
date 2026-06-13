name = input("What's ur name ? ")
print("Hi",name,"Welcome to the mood advisior")
mood= input("How are you feeling today ? " ).lower()
if mood == "happy":
    print("Glad to hear! ")
elif mood == "sad":
    print("Im so sorry to hear that! I hope you are doing okay!")
elif mood =="angry":
    print("Take a deep breath, and rethink what you just did/rethink ur life chocies AGAIN!")
else:
    print("Sorry, I didnt understand that mood")

import datetime
import calendar
now= datetime.datetime.now()
print("The time today is :",now)
print(calendar.calendar(now.year))