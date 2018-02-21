# Example file for formatting time and date output
from datetime import datetime

def main():
    now = datetime.now()

    #### Date Formatting ####

    # %y/%Y - year, %a/%A - weekday, %b/%B - month, %d - day of month
    # print(now.strftime("%a, %d %b, %y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date : %x"))
    print(now.strftime("Locale time: %X"))

    #### Time Formatting ####
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-hour time: %H:%M:%S"))

main()
