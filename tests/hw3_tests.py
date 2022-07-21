import logging
import math
import hw_3


def test_print_dict(capsys):
    logging.info("print_dict() - Test")
    temp_dict = {
         1: {"name": "Bar", "sex": "female", "age": 28},
         2: {"name": "Ran", "sex": "male", "age": 33}
    }
    hw_3.print_dict(temp_dict)
    captures = capsys.readouterr()
    assert captures.out == "{'name': 'Bar', 'sex': 'female', 'age': 28}\n{'name': 'Ran', 'sex': 'male', 'age': 33}\n"


def test_print_values_above(capsys):
    logging.info("print_values_above() - Test")
    temp_dict = {
        1: {"name": "Bar", "sex": "female", "age": 28},
        2: {"name": "Ran", "sex": "male", "age": 33}
    }
    hw_3.print_values_above(temp_dict, 30)
    captured = capsys.readouterr()
    assert captured.out == "---All people older then 30 are:\n{'name': 'Ran', 'sex': 'male', 'age': 33}\n"


def test_find_median_average(capsys):
    logging.info("test_find_median_average() - Test")
    temp_dict = {
     3: {"name": "Eli", "id": 305484511, "sex": "male", "age": 50},
     4: {"name": "Lotem", "id": 304484511, "sex": "female", "age": 20},
     5: {"name": "Shir", "id": 366684511, "sex": "female", "age": 40}
     }
    hw_3.find_median_average(temp_dict)
    captured = capsys.readouterr()
    assert captured.out == "---The average age is: 36.666666666666664\n---The median age is: 40\n"


def test_split_male_female():
    logging.info("test_split_male_female() - Test")

    temp_dict = {
        3: {"name": "Eli", "id": 305484511, "sex": "male", "age": 50},
        4: {"name": "Lotem", "id": 304484511, "sex": "female", "age": 20},
        5: {"name": "Shir", "id": 366684511, "sex": "female", "age": 40}
    }
    df, dm = hw_3.split_male_female(temp_dict)
    dmm = {3: {"name": "Eli", "id": 305484511, "sex": "male", "age": 50}}
    dff = {
        4: {"name": "Lotem", "id": 304484511, "sex": "female", "age": 20},
        5: {"name": "Shir", "id": 366684511, "sex": "female", "age": 40}
    }
    assert df == dff and dm == dmm

