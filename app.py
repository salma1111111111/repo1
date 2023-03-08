# fonction 1
def inc(x):
    return x + 1

#fonction 2
import datetime

def get_age(yyyy:int, mm:int, dd:int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age
 
#fonction 3
def deinc(x):
    return x - 1