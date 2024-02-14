from cryptography.fernet import Fernet


def write_key():
    """
    Function to generate a key using Fernet and write it to a file.
    No parameters.
    No return type.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Function to load the key from a file.
    No parameters.
    Returns the key.
    """
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

pass_input = input("Please input your password? ")
key = load_key()
fer = Fernet(key)


def view():
    """
    Define the purpose of the 'view' function, its parameters, and its return types.
    """
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    """
    A function that takes user input for account name and password, then appends them to a file called "passwords.txt".
    """
    Account_name = input("What is the name of your account? ")
    Account_password = input("What is the password of your account? ")

    with open ("passwords.txt", "a") as f:
        f.write(Account_name + "|" + str(fer.encrypt(Account_password.encode())) + "\n")

while True:
    options = input("""Would you like to add a new password
     or view existing one(view, add) q to quit: """).lower()
    if options == "q":
        break

    elif options == "view":
        view()

    elif options == "add":
        add()

    else:
        print("Invalid option")
        continue

