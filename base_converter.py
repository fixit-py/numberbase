# converts from base 10 integer to any other base

def base_converter(number,  fin_base):  # accepts two input the number ,  the final base
    # Checks if the input number is negative
    if number < 0:
        is_negative = True
        # Make the number positive for processing
        number = abs(number)
    else:
        is_negative = False

    # Separates the integer and fractional parts of the number
    int_part = int(number)
    fraction_part = number - int_part
    final_value = ""  # initializes an empty string

    # Converts integer part to the desired base
    while int_part > 0:  # performs a command while the integer part is greater than 0
        remainder = int_part % fin_base
        final_value = str(remainder) + final_value
        int_part //= fin_base

    # Handles the case when the integer part is 0
    if final_value == "":
        final_value = "0"

    # Adds a decimal point if there is a fractional part
    if fraction_part > 0:
        final_value += "."

    # Converts fractional part to the desired base (limited to a certain number of digits)
    # max_fraction_digits = 10  # You can adjust this based on your needs
    current_fraction_digits = 0
    while fraction_part > 0:  # and current_fraction_digits < max_fraction_digits:
        fraction_part *= fin_base
        digit = int(fraction_part)
        final_value += str(digit)
        fraction_part -= digit
        current_fraction_digits += 1
    # Convert the final result back to a float and apply a negative sign if necessary
    if is_negative:
        return -1 * float(final_value)
    else:
        return float(final_value)
