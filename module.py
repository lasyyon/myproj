from database import load_data, save_data

def play_guessing_game():
    secret_number = load_data()
    attempts = 0

    while True:
        user_guess = int(input("Вгадайте число від 1 до 100: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб.")
            break
        elif user_guess < secret_number:
            print("Спробуйте більше.")
        else:
            print("Спробуйте менше.")

    save_data(secret_number)

def run_program():
    play_guessing_game()
