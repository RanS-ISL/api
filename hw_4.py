import math
import math


class Date:
 def __init__(self, day:int, month: int, year: int):
     if isinstance(day, int) and 0 < day < 32:
       self._day = day
     else:
        raise TypeError('Day must be between 1-31')

     if isinstance(month, int) and 0 < month < 13:
         self._month = month
     else:
         raise TypeError('Month must be between 1-13')

     if isinstance(year, int) and 999 < year < 10000:
         self._year = year
     else:
         raise TypeError('Year must be 4 digits long')

 def __str__(self) -> str:
     """
     return a nice detailed string of the object
     for example: 3.2.2003
     :return: string
     """""
     return f"Date is: {self._day}.{self._month}.{self._year}"

 def __eq__(self, other) -> bool:
     """
     check if two dates are the same date.
     for example: (5.8.1990)(6.8.1991) --> False
                  (1.1.2260)(1.1.2260) --> True
     :param other: object from class Date
     :return: bool
     """
     result = False
     if isinstance(other, Date):
         if self._year == other._year and self._day == other._day and self._month == other._month:
             result = True
     return result

 #def test___eq__():


 def __lt__(self, other) -> bool:
     """
     check if the object is earlier date than the other.
     for example: (10.12.2005)(15.11.2006) --> True
     :param other: object from class Date
     :return: bool
     """
     result = False
     if isinstance(other, Date):
         if self._year < other._year:
             result = True
         elif self._year == other._year:
             if self._month < other._month:
                 result = True
             elif self._month == other._month and self._day < other._day:
                 result = True
     return result

 def __gt__(self, other):
     """
     check if the object is later date than the other
     for example: (14.7.2000)(1.7.2000) --> True
                  (14.7.2000)(14.8.2000) --> False
     :param other: object from class Date
     :return: bool
     """
     result = False
     if isinstance(other, Date):
         if self._year > other._year:
             result = True
         elif self._year == other._year:
             if self._month > other._month:
                 result = True
             elif self._month == other._month and self._day > other._day:
                 result = True
     return result

 def __sub__(self, other) -> int:
     """
     calculate the difference between two dates in days count
     for example: (2.2.2002)(10.2.2002) --> 8
                  (10.2.2002)(2.2.2002) --> 8
     :param other: object from class Date
     :return: int
     """
     result = 0
     if isinstance(other, Date):
         if self.__lt__(other):
             temp_date = Date(self._day, self._month, self._year)
             for i in range(8999):
                 temp_date = temp_date.get_next_day()
                 result = result + 1
                 if temp_date.__eq__(other):
                     break
         elif self.__gt__(other):
             temp_date = Date(other._day, other._month, other._year)
             for i in range(8999):
                 temp_date = temp_date.getNextDay()
                 result = result +1
                 if temp_date.__eq__(self):
                     break
     return result

 def isValid(self) -> bool:
     """
     check if the date is a valid real date.
     for example: 31.11.2000 -> not valid (Nov' ends on 30)
                  31.10.2000 -> valid, there is 31 days in Oct'.
     :return: bool
     """
     result = False
     if self._day < 29:
         result = True
     elif self._day == 29:
         if self._month == 2 and self._year%4 != 0:
             result = False
         else: result = True
     elif self._day == 30:
         if self._month == 2:
             result = False
         else: result = True
     elif self._day == 31:
         if self._month != 2 and self._month != 4 and self._month != 6 and self._month != 9 and self._month != 11:
             result = True
         else:
             result = False
     return result

 def getNextDay(self):
     """
     calculate the date one day ahead
     for example: if 3.2.2004 so return will be 4.2.2004
                  if 31.12.2004 so return will be 1.1.2005
     :return: Date object
     """
     temp_date = Date(self._day, self._month, self._year)
     if temp_date._day < 28:
         temp_date._day = temp_date._day+1
     elif temp_date._day == 28:
         if temp_date._month == 2 and temp_date._year % 4 != 0:
                 temp_date._day = 1
                 temp_date._month = temp_date._month+1
         else:
             temp_date._day = temp_date._day + 1
     elif temp_date._day == 29:
         if self._month == 2:
             temp_date._day = 1
             temp_date._month = temp_date._month + 1
         else:
             temp_date._day = temp_date._day + 1
     elif temp_date._day == 30:
         if temp_date._month == 2 or temp_date._month == 4 or temp_date._month == 6 or temp_date._month == 9 \
                 or temp_date._month == 11:
             temp_date._day = 1
             temp_date._month = temp_date._month + 1
         else:
             temp_date._day = temp_date._day + 1
     else:
         if temp_date._month == 12:
             temp_date._year = temp_date._year + 1
             temp_date._month = 1
             temp_date._day = 1
         else:
             temp_date._day = 1
             temp_date._month = temp_date._month + 1
     return temp_date

 def getNextDays(self, daysToadd: int):
     """
     calculate the date n(daysToadd) days ahead
     for example: (1.1.2000, 5) -> 6.1.2000
                  (28.12.2000, 10) -> 7.1.2001
     :param daysToadd: the numbers of days you want to calculate ahead
     :return: Date object
     """
     temp_date = Date(self._day, self._month, self._year)
     for i in range(daysToadd):
         temp_date = temp_date.getNextDay()
     return temp_date


def __main__():
    d1 = Date(30, 5, 2051)
    d2 = Date(5, 5, 2051)
    print(d1)
    print(d2)
    print(d1.isValid())
    print(d2.isValid())
    print(d1.getNextDay())
    print(d1.getNextDays(15))
    print(d1.__eq__(d2))
    print(d1.__lt__(d2))
    print(d1.__gt__(d2))
    print(d1.__sub__(d2))


if __name__ == "__main__":
    __main__()
