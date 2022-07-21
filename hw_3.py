import math


def split_male_female(param: dict):
    """
    get a dictionary of people, divide them by gender to 2 dictionaries and print them.
    :param param: dictionary of people
    :return: dictionary(of males), dictionary(of females)
    """
    male_dict = {}
    female_dict = {}
    temp_dict = {}
    m_id = 1
    fm_id = 1
    for k in param:
        temp_dict = param.get(k)
        if temp_dict.get("sex") == "male":
           male_dict[k]= temp_dict
        else:
           female_dict[k] = temp_dict
    print(f"Males:")
    print_dict(male_dict)
    print(f"Females:")
    print_dict(female_dict)
    return female_dict, male_dict


def find_median_average(param: dict):
    """
    example: ages (15,30,60)-> avg-35/med-30 | ages(15,30,60,80)->avg-46.25/med-30
    print what is the average age and the median age, out of a dictionary of people
    :param param: dictionary of people
    :return: none
    """
    temp_dict = {}
    temp_lst = []
    avg_age = 0
    median_age = 0
    for k in param:
        temp_dict = param.get(k)
        avg_age = avg_age + temp_dict.get("age")
        temp_lst.append(temp_dict.get("age"))
    avg_age = avg_age/len(param)
    temp_lst.sort()
    median_age = temp_lst[int(len(temp_lst)/2)]
    print(f"---The average age is: {avg_age}")
    print(f"---The median age is: {median_age}")


def print_values_above(param: dict, num: int = 0):
    """
    print all people from a dictionary which are older from a specific age
    :param param: the dictionary we want to work on
    :param num: will show people above this age, if not sent - o is default
    :return: none
    """
    temp_dict = {}
    dict_res = {}
    for k in param:
        temp_dict = param.get(k)
        if temp_dict.get("age") > num:
            dict_res[k] = temp_dict
    print(f"---All people older then {num} are:")
    print_dict(dict_res)


def print_dict(param: dict):
    """
    print the dictionary by rows.
    :param param: dictionary we print
    :return: none
    """
    for k in param:
        print(param.get(k))


def __main__():
    """
    declare data_set(dict in dict) and call other functions.
    :return:none
    """
    data_set = {
        1: {"name": "Bar", "sex": "female", "age": 28},
        2: {"name": "Ran", "sex": "male", "age": 33},
        3: {"name": "Eli", "id": 305484511, "sex": "male", "age": 50},
        4: {"name": "Lotem", "id": 304484511, "sex": "female", "age": 20},
        5: {"name": "Shir", "id": 366684511, "sex": "female", "age": 40}
    }
    split_male_female(data_set)
    find_median_average(data_set)
    print_values_above(data_set, 30)


if __name__ == "__main__":
    __main__()