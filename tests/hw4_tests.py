import logging
import math
import hw_4


def test_getNextDays():
    d1 = hw_4.Date(5, 10, 2000)
    d2 = hw_4.Date(10, 10, 2000)
    d1 = d1.getNextDays(5)
    logging.info("getNextDays() - test")
    assert d1.__eq__(d2)


def test_getNextDay():
    d1 = hw_4.Date(12, 2, 1980)
    d2 = hw_4.Date(13, 2, 1980)
    d1 = d1.getNextDay()
    logging.info("getNextDay() - test")
    assert d1 == d2

def test_isValid():
    d1 = hw_4.Date(29, 2, 2000)
    logging.info("isValid() - test")
    assert d1.isValid()

def test___sub__():
    d1 = hw_4.Date(4, 11, 2008)
    d2 = hw_4.Date(5, 10, 2007)
    res = 396
    logging.info("__sub__(2-dates) - test")
    assert d1.__sub__(d2) == res


def test___gt__():
    d1 = hw_4.Date(4, 12, 2007)
    d2 = hw_4.Date(5, 10, 2007)
    logging.info("__gt__(2-dates) - test")
    assert d1.__gt__(d2)


def test___lt__():
    d1 = hw_4.Date(4, 2, 2008)
    d2 = hw_4.Date(5, 11, 2007)
    logging.info("__lt__(2-dates) - test")
    assert d2.__lt__(d1)

