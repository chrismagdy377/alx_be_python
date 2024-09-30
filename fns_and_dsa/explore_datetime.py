from datetime import datetime
from datetime import timedelta

def display_current_datetime(current_date = datetime.now()):
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: {0}".format(current_date))
    pass

display_current_datetime()

current_date = datetime.now()
def calculate_future_date(future_date = 0):
    future_date = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=future_date)
    future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Future date: {0}".format(future_date))
    pass

calculate_future_date()



