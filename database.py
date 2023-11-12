# database.py
import os
import random  # Додайте імпорт

DATA_FILE = "data.txt"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return int(file.read())
    else:
        return generate_secret_number()

def save_data(secret_number):
    with open(DATA_FILE, "w") as file:
        file.write(str(secret_number))

def generate_secret_number():
    secret_number = random.randint(1, 100)  # Змінено генерацію на випадкове число
    save_data(secret_number)
    return secret_number
