def to_decimal(number: str):
    """Converts a string containing a roman numeral into a decimal integer"""

    assert is_valid_roman(number), "Invalid Roman numeral"
    lookrev = {v: k for k, v in lookup.items()}
    decimal = 0
    for i, rom in enumerate(number):
        try:
            if lookrev[number[i + 1]] <= lookrev[rom]:
                decimal += lookrev[rom]
            else:
                decimal -= lookrev[rom]
        except IndexError:
            decimal += lookrev[rom]
    return decimal


def to_roman(number: int):
    """Converts an integer to Roman numerals. Returns a string"""

    assert type(number) == int, "Input must be an integer between 1 and 3999"
    assert number > 0 and number < 4000, "Input must be an integer between 1 and 3999"

    roman = ""

    while number > 0:

        first_digit = str(number)[0]

        if first_digit == "9":
            min_digit = find_digit(
                9 * 10 ** (len(str(number)) - 1), reverse=True, dec=True
            )
            roman += lookup[min_digit]
            number += min_digit

        elif first_digit == "4":
            min_digit = find_digit(
                4 * 10 ** (len(str(number)) - 1), reverse=True, dec=True
            )
            roman += lookup[min_digit]
            number += min_digit

        max_digit = find_digit(number, reverse=not number == 9 or number == 4)
        roman += lookup[max_digit]
        number = number - max_digit

    return roman


def find_digit(digit, reverse, dec=False):
    for i in sorted(lookup.keys(), reverse=reverse):
        if reverse:
            if i <= digit and (str(i)[0] == "1" if dec else True):
                return i
        else:
            if i >= digit and (str(i)[0] == "1" if dec else True):
                return i


def is_valid_roman(number: str):
    """Returns True if number is a valid Roman numeral"""
    return number in valid_romans


lookup = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
valid_romans = [to_roman(i) for i in range(1, 4000)]
