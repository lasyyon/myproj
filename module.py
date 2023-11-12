from database import load_data, save_data

class GuessingGame:
    def __init__(self):
        self.secret_number = load_data()
        self.attempts = 0

    def play(self, user_guess):
        self.attempts += 1

        if user_guess == self.secret_number:
            print(f"Вітаємо! Ви вгадали число {self.secret_number} за {self.attempts} спроб.")
            return True
        elif user_guess < self.secret_number:
            print("Спробуйте більше.")
        else:
            print("Спробуйте менше.")
        return False

def run_program():
    game = GuessingGame()
    while True:
        user_guess = int(input("Вгадайте число від 1 до 100: "))
        if game.play(user_guess):
            break
    save_data(game.secret_number)
