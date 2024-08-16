import random
import string

def generate_password(length=12):

    Lowercase = string.ascii_lowercase
    Uppercase = string.ascii_uppercase
    Digits = string.digits
    Special_chars = string.punctuation


    all_chars = Lowercase + Uppercase + Digits + Special_chars

    password = [
        random.choice(Lowercase),
        random.choice(Uppercase),
        random.choice(Digits),
        random.choice(Special_chars)
    ]

    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    print("Generated Password:", generate_password(12))
