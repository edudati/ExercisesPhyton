import getpass


def main():
    passwords = {"pepelegal@gmail.com": "123456", "batman@gmail.com": "654321"}
    email = input("Enter your email: ").lower()

    while email not in passwords.keys():
        email = input("Email not found. Please enter your email: ")
    else:
        password = getpass.getpass("passowrd: ")
        while password != passwords[email]:
            password = getpass.getpass("Please, enter passowrd again: ")
        else:
            print("OK!")