import string
import random

def Random_password_gen():
    
    length = int(input("Enter the lenght of the password? : ").strip())

    if length < 4:
        print("password length should be above '4' ")
        return

    uppercase = input("Do you need uppercase characters(yes/no)? : ").strip().lower()
    special = input("Do you need Special characters(yes/no)? : ").strip().lower()
    numbers = input("Do you need digits(yes/no)? : ").strip().lower()

    lower_case =string.ascii_lowercase
    upper_case_char = string.ascii_uppercase if uppercase == "yes" else ""
    special_char = string.punctuation if special == "yes" else ""
    digits = string.digits if numbers == "yes" else ""

    all_characters = lower_case + upper_case_char + special_char + digits


    required_characters = []
    if uppercase == "yes":
        required_characters.append(random.choice(upper_case_char))
    if special == "yes":
        required_characters.append(random.choice(special_char))
    if numbers == "yes":
        required_characters.append(random.choice(digits))

    remaining_password = length - len(required_characters)

    for _ in range(remaining_password):
        required_characters.append(random.choice(all_characters))

    random.shuffle(required_characters)

    passcode = "".join(required_characters)
    return passcode

password = Random_password_gen()

print(password)
     