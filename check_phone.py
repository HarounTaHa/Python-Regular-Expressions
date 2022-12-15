import re


def is_phone_number(text):
    is_phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
    if is_phone:
        print(f'The {text} is valid phone number')
    else:
        print(f'The {text} is not a valid phone number')


is_phone_number('415-185-5466')  # valid
is_phone_number('a415-1a85-5466')  # not valid
