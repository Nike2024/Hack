import random
import requests
import json
from colorama import Fore


def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    return "UNKNOWN"


def get_hint(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and 'meanings' in data[0]:
            definition = data[0]['meanings'][0]['definitions'][0]['definition']
            return f"Hint: {definition}"
    return "Hint: No definition available."


def get_category_hint(category):
    url = f"https://api.api-ninjas.com/v1/{category}?limit=1"
    headers = {"X-Api-Key": "YOUR_API_KEY"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return f"Hint: {data[0]}" if data else "Hint: No additional info."
    return "Hint: Unable to fetch category info."


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def vigenere_cipher(text, key, encrypt=True):
    key = key.lower()
    key_length = len(key)
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            if not encrypt:
                shift = -shift
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def challenge_mode():
    global score
    choice = input(Fore.CYAN + "Choose a category or type 'random' for any word: ").lower()

    if choice == 'random':
        word = get_random_word().upper()
        hint = get_hint(word)
    else:
        word = get_random_word().upper()
        hint = get_category_hint(choice)

    shift = random.randint(1, 25)
    encrypted = caesar_cipher(word, shift)
    print(Fore.YELLOW + f"Crack this code: {encrypted}")
    print(Fore.MAGENTA + hint)

    guess = input(Fore.CYAN + "Your answer: ").upper()
    if guess == word:
        print(Fore.GREEN + "Correct! You cracked the code!")
        score += 1
    else:
        print(Fore.RED + f"Wrong! The correct answer was {word}.")
        score -= 1

    print(Fore.BLUE + f"Your current score: {score}")


def main():
    global score
    score = 0
    while True:
        print(Fore.BLUE + "\nChoose a mode:")
        print("1. Encrypt with Vigenere Cipher")
        print("2. Decrypt with Vigenere Cipher")
        print("3. Encrypt with Caesar Cipher")
        print("4. Decrypt with Caesar Cipher")
        print("5. Challenge Mode")
        print("6. Exit")

        choice = input(Fore.CYAN + "Enter your choice: ")

        if choice == "1":
            text = input("Enter text: ")
            key = input("Enter key: ")
            print("Encrypted text:", vigenere_cipher(text, key, True))
        elif choice == "2":
            text = input("Enter encrypted text: ")
            key = input("Enter key: ")
            print("Decrypted text:", vigenere_cipher(text, key, False))
        elif choice == "3":
            text = input("Enter text: ")
            shift = int(input("Enter shift: "))
            print("Encrypted text:", caesar_cipher(text, shift))
        elif choice == "4":
            text = input("Enter encrypted text: ")
            shift = int(input("Enter shift: "))
            print("Decrypted text:", caesar_cipher(text, -shift))
        elif choice == "5":
            challenge_mode()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
