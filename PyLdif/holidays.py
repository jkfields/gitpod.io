from pandas.tseries.holiday import get_calendar, Holiday, AbstractHolidayCalendar, HolidayCalendarFactory, GoodFriday
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from pandas import read_csv, bdate_range
from datetime import date
from pprint import PrettyPrinter


pp = PrinterPrinter(indent=4).pprint

def get_timeoff():
    days = [ Holiday("Paid Time Off", year=2022, month=12, day=9),
             Holiday("Paid Time Off", year=2022, month=12, day=16),
             Holiday("Paid Time Off", year=2022, month=12, day=20),
             Holiday("Paid Time Off", year=2022, month=12, day=21),
             Holiday("Paid Time Off", year=2022, month=12, day=22),
             Holiday("Paid Time Off", year=2022, month=12, day=23),
             Holiday("Paid Time Off", year=2022, month=12, day=27),
             Holiday("Paid Time Off", year=2022, month=12, day=28),
             Holiday("Paid Time Off", year=2022, month=12, day=29),
             Holiday("Paid Time Off", year=2022, month=12, day=30),
             Holiday("Paid Time Off", year=2023, month=3, day=6),
             Holiday("Terminal Leave", year=2023, month=3, day=13),
             Holiday("Terminal Leave", year=2023, month=3, day=14),
             Holiday("Terminal Leave", year=2023, month=3, day=15),
             Holiday("Terminal Leave", year=2023, month=3, day=16),
             Holiday("Terminal Leave", year=2023, month=3, day=17),
             Holiday("Terminal Leave", year=2023, month=3, day=20),
             Holiday("Terminal Leave", year=2023, month=3, day=21),
             Holiday("Terminal Leave", year=2023, month=3, day=22),
             Holiday("Terminal Leave", year=2023, month=3, day=23),
             Holiday("Terminal Leave", year=2023, month=3, day=24),
           ]
    return days


def main():
    cal = get_calendar("USFederalHolidayCalendar")
    timeoff = get_timeoff()
    tcal = HolidayCalendarFactory('TimeOff', cal, timeoff)
    new_cal = tcal()
    pp(new_cal.rules)
    
    start = date.today()
    end = date(2023, 3, 24)
    work_days = CustomBusinessDay(calendar=new_cal)
    #print(bdate_range(start, end, freq=work_days))


if __name__ == "__main__":
    main()
