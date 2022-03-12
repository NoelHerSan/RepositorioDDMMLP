import re

message_error = "Check the inputs, should be only numbers or with fraction format"


# This function is needed for check if a input value can convert to float format
def isnoterror(valor):
    """
    Validate if the input value can convert to float format.

    :param valor: The parameter that can are a string with fraction format or a number
    :return: Boolean, True if the input value can convert to float format, False if the input value can not
    convert to float format

    >>> isnoterror('3/4')
    False
    >>> isnoterror(2.5)
    True
    """
    try:
        float(valor)
        return True
    except ValueError:
        return False


# Function that convert the input value in fraction format to float format.
def get_fractions(valor):
    """
    Convert a fraction or numeric format to float format

    :param valor:
    :return: the input value as float number

    >>> get_fractions("1/2")
    0.5
    >>> get_fractions("3")
    3
    """
    mystring = str(valor)
    verifyfraction = re.search(r"(?:[1-9][0-9]*|0)\/[1-9][0-9]*", mystring)
    if verifyfraction:
        split_string = valor.split('/')
        decimal = int(split_string[0]) / int(split_string[1])
        return decimal
    elif isnoterror(valor):
        return float(valor)
    else:
        return 0


# Sum function
def calc_sum(a,
             b):
    """
    Calculate the sum between a and b

    :param a: The first sumand
    :param b: The second sumand
    :return: the sum of the elements

    >>> calc_sum(1,2)
    3
    """
    if isinstance(a, float) and isinstance(b, float):
        return a + b
    else:
        sum_a = get_fractions(a)
        sum_b = get_fractions(b)
        if isinstance(sum_a, float) and isinstance(sum_b, float):
            return sum_a + sum_b
        else:
            return message_error


# res function
def calc_res(a,
             b):
    """
    Calculate the rest between a and b

    :param a: The minuend
    :param b: The subtracting
    :return: the rest of the elements

    >>> calc_res(1,2)
    -1
    """
    if isinstance(a, float) and isinstance(b, float):
        return a - b
    else:
        minuend = get_fractions(a)
        subtracting = get_fractions(b)
        if isinstance(minuend, float) and isinstance(subtracting, float):
            return minuend - subtracting
        else:
            return message_error


# multiplication function
def calc_multiplication(a,
                        b):
    """
    Calculate the multiplication between a and b

    :param a: The multiplier
    :param b: The multiplying
    :return: the multiplication of the elements

    >>> calc_multiplication(1,2)
    2
    """
    if isinstance(a, float) and isinstance(b, float):
        return a * b
    else:
        multiplier = get_fractions(a)
        multiplying = get_fractions(b)
        if isinstance(multiplier, float) and isinstance(multiplying, float):
            return multiplier * multiplying
        else:
            return message_error


# division function
def calc_division(a,
                  b):
    """
    Calculate the division between a and b

    :param a: The dividend
    :param b: The divisor
    :return: the division of the elements

    >>> calc_division(1,2)
    0.5
    """
    if isinstance(a, float) and isinstance(b, float):
        return a / b
    else:
        dividend = get_fractions(a)
        divisor = get_fractions(b)
        if isinstance(dividend, float) and isinstance(divisor, float):
            return dividend / divisor
        else:
            return message_error
