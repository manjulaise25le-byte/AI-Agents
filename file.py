import time
import random

# List of simple words for memory game
words_list = [
    "apple", "ball", "cat", "dog", "fish", "hat", "ice", "jug", "kite", "lion"
]

def play_round(round_num, length=4):
    # Pick random words for this round
    words = random.sample(words_list, length)
    print(f"Round {round_num}: Remember these words in order:")
    print(words)
    time.sleep(4)  # Show words for 4 seconds

    print("\n" * 100)  # Clear screen

    correct = 0
    for i, word in enumerate(words):
        guess = input(f"Enter word {i + 1}: ").strip().lower()
        if guess == word:
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong, the correct word was '{word}'.")

    print(f"\nYou remembered {correct} out of {length} words correctly.\n")

    return correct == length

def memory_game():
    name = input("Enter your name: ").strip()
    print(f"\nWelcome {name}! Let's start the memory game.\n")
    time.sleep(1)

    rounds = random.randint(5, 8)
    print(f"You will play {rounds} rounds of the memory game.\n")
    time.sleep(2)
    full_success = 0

    for round_num in range(1, rounds + 1):
        success = play_round(round_num)
        if success:
            print(f"Great job, {name}! You won round {round_num}!\n")
            full_success += 1
        else:
            print(f"Round {round_num} completed. Keep practicing!\n")
        time.sleep(2)

    print(f"Game over, {name}! You perfectly remembered {full_success} rounds out of {rounds}.")

if __name__ == "__main__":
    memory_game()