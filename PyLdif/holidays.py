from pandas.tseries.holiday import get_calendar, Holiday, AbstractHolidayCalendar, HolidayCalendarFactory, GoodFriday
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from pandas import read_csv, bdate_range
from datetime import date
from pprint import PrettyPrinter
from pandas.tseries.holiday import (USFederalHolidayCalendar, USMemorialDay,
                                    USThanksgivingDay, nearest_workday,
                                    next_monday_or_tuesday, next_monday,
                                    previous_friday, sunday_to_monday, Holiday,
                                    DateOffset, MO, SA, Timestamp,
                                    AbstractHolidayCalendar, get_calendar,
                                    HolidayCalendarFactory, next_workday,
                                    previous_workday, before_nearest_workday,
                                    EasterMonday, GoodFriday,
                                    after_nearest_workday, weekend_to_monday,
                                    USLaborDay, USColumbusDay,
                                    USMartinLutherKingJr, USPresidentsDay)


pp = PrettyPrinter(indent=4).pprint

def get_timeoff():
    days = [ Holiday("Paid Time Off 1", year=2022, month=12, day=9),
             Holiday("Paid Time Off 2", year=2022, month=12, day=16),
             Holiday("Paid Time Off 3", year=2022, month=12, day=20),
             Holiday("Paid Time Off 4", year=2022, month=12, day=21),
             Holiday("Paid Time Off 5", year=2022, month=12, day=22),
             Holiday("Paid Time Off 6", year=2022, month=12, day=23),
             Holiday("Paid Time Off 7", year=2022, month=12, day=27),
             Holiday("Paid Time Off 8", year=2022, month=12, day=28),
             Holiday("Paid Time Off 9", year=2022, month=12, day=29),
             Holiday("Paid Time Off 10", year=2022, month=12, day=30),
             Holiday("Paid Time Off 11", year=2023, month=3, day=6),
             Holiday("Terminal Leave 1", year=2023, month=3, day=13),
             Holiday("Terminal Leave 2", year=2023, month=3, day=14),
             Holiday("Terminal Leave 3", year=2023, month=3, day=15),
             Holiday("Terminal Leave 4", year=2023, month=3, day=16),
             Holiday("Terminal Leave 5", year=2023, month=3, day=17),
             Holiday("Terminal Leave 6", year=2023, month=3, day=20),
             Holiday("Terminal Leave 7", year=2023, month=3, day=21),
             Holiday("Terminal Leave 8", year=2023, month=3, day=22),
             Holiday("Terminal Leave 9", year=2023, month=3, day=23),
             Holiday("Terminal Leave 10", year=2023, month=3, day=24),
           ]
    return days

def get_cyber_monday():
    return  Holiday("Cyber Monday", month=11, day=1,
                    offset=[DateOffset(weekday=SA(4))],
                    observance=next_monday)


def main():
    cal = get_calendar("USFederalHolidayCalendar")
    
    '''
    # this seems to be the answer
    timeoff = get_timeoff()
    tcal = HolidayCalendarFactory('TimeOff', cal, timeoff)
    new_cal = tcal()
    #pp(new_cal.rules)
    
    start = date.today()
    end = date(2023, 3, 24)
    work_days = CustomBusinessDay(calendar=new_cal)
    pp(bdate_range(start, end, freq=work_days))
    '''

    # can we go backwards in time -- no
    #pp(bdate_range(start, date(2022, 9, 1), freq="C"))

    #print(cal.days)
    print(get_cyber_monday())


if __name__ == "__main__":
    main()
