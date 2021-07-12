"""
Create passrods with different configurations
"""
import secrets
import string


def main():
    lenght = 8

    password = create_password_char(lenght)
    print("Password with only letters: ", password)

    password = create_password_num(lenght)
    print("Password with only numbers: ", password)

    password = create_password_char_num(lenght)
    print("Password with charecters and numbers: ", password)

    password = create_password_char_num_sym(lenght)
    print("Password with charecters, numbers and symbols: ", password)

    password = create_password_at_least_one(lenght)
    print("Password with at least one charecter, number and symbol: ", password)

def create_password_char(lenght, case_sensive="both"):
    """Create a password with only letters, with informed lenght
    : parameters:
            lenght: Lenght of password
            case_sensive:
                both(default): Create a password with random upper and lower characters
                lower: Create password with only lowercase characters
                upper: Create password with only uppercase characters
    : return: Created passord
    """
    if case_sensive == "both":
        characters = string.ascii_letters
    elif case_sensive == "lower":
        characters = string.ascii_lowercase
    elif case_sensive == "upper":
        characters = string.ascii_uppercase
    else:
        return 1
    password = ''.join(secrets.choice(characters) for i in range(lenght))
    return password


def create_password_num(lenght):
    """Create a password with numbers, with informed lenght
    :param: lenght: Lenght of password
    :return: Created passord
    """
    characters = string.digits
    password = ''.join(secrets.choice(characters) for i in range(lenght))
    return password


def create_password_char_num(lenght):
    """Create a password with numbers and/or letters case sensive, with informed lenght
    :param: lenght: Lenght of password
    :return: Created passord
    """
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for i in range(lenght))
    return password


def create_password_char_num_sym(lenght):
    """Create a password with numbers, letters and/or symbols, with informed lenght
    :param: lenght: Lenght of password
    :return: Created passord
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(lenght))
    return password

def create_password_at_least_one(lenght):
    """Create a password with numbers, letters and/or symbols, with informed lenght
    :param: lenght: Lenght of password
    :return: Created passord
    """
    n_upper = n_lower = n_digits = n_punctuation = 0
    while n_upper < 1 or n_lower < 1 or n_digits < 1 or n_punctuation < 1:
        n_upper = n_lower = n_digits = n_punctuation = 0
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for i in range(lenght))
        for i in password:
            if i in string.ascii_uppercase:
                n_upper += 1
            if i in string.ascii_lowercase:
                n_lower += 1
            elif i in string.digits:
                n_digits += 1
            elif i in string.punctuation:
                n_punctuation += 1
    return password


if __name__ == '__main__':
    main()