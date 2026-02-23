import random

def play():
    number = random.randint(1, 200)
    attempts = 0
    print("🎮 Guess The Number (1-200)")

    while True:
        guess = int(input("Enter guess: "))
        attempts += 1
        if guess == number:
            print(f"🎉 You won in {attempts} attempts!")
            break
        elif guess < number:
            print("Too Low")
        else:
            print("Too High")

if __name__ == "__main__":
    play()
