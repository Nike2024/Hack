import random
import time
import nltk
import tkinter as tk
from tkinter import messagebox, simpledialog
from nltk.corpus import words

nltk.download('words')  # Download word dataset
word_list = words.words()  # Load word list

# Predefined categories
categories = {
    "fruits": ["apple", "banana", "cherry", "date", "fig", "grape", "mango"],
    "books": ["harrypotter", "hobbit", "iliad", "odyssey", "gatsby"],
    "countries": ["india", "canada", "brazil", "germany", "japan", "france"],
    "colors": ["red", "blue", "green", "yellow", "purple", "orange"],
    "animals": ["lion", "tiger", "elephant", "giraffe", "zebra", "kangaroo"],
    "water bodies": ["ocean", "river", "lake", "pond", "stream", "sea"],
    "plants": ["rose", "tulip", "bamboo", "cactus", "fern", "maple"]
}

score = 0  # Score tracking


def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = shift if encrypt else -shift
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
    category = simpledialog.askstring("Challenge Mode", "Choose a category (or type 'random' for any word): ")

    if category in categories:
        word = random.choice(categories[category]).upper()
        hint = f"Category: {category.capitalize()}"
    else:
        word = random.choice(word_list).upper()
        hint = f"Hint: The word belongs to an unknown category."

    shift = random.randint(1, 25)
    encrypted = caesar_cipher(word, shift)
    guess = simpledialog.askstring("Crack the Code", f"Decrypted this: {encrypted}\n{hint}")

    if guess and guess.upper() == word:
        messagebox.showinfo("Correct!", "You cracked the code!")
        score += 1
    else:
        messagebox.showerror("Wrong!", f"The correct answer was {word}.")
        score -= 1

    messagebox.showinfo("Score", f"Your current score: {score}")


def encrypt_caesar():
    text = simpledialog.askstring("Caesar Cipher", "Enter text to encrypt:")
    shift = simpledialog.askinteger("Caesar Cipher", "Enter shift value:")
    if text and shift is not None:
        messagebox.showinfo("Result", f"Encrypted text: {caesar_cipher(text, shift)}")


def decrypt_caesar():
    text = simpledialog.askstring("Caesar Cipher", "Enter text to decrypt:")
    shift = simpledialog.askinteger("Caesar Cipher", "Enter shift value:")
    if text and shift is not None:
        messagebox.showinfo("Result", f"Decrypted text: {caesar_cipher(text, shift, encrypt=False)}")


def encrypt_vigenere():
    text = simpledialog.askstring("Vigenère Cipher", "Enter text to encrypt:")
    key = simpledialog.askstring("Vigenère Cipher", "Enter keyword:")
    if text and key:
        messagebox.showinfo("Result", f"Encrypted text: {vigenere_cipher(text, key)}")


def decrypt_vigenere():
    text = simpledialog.askstring("Vigenère Cipher", "Enter text to decrypt:")
    key = simpledialog.askstring("Vigenère Cipher", "Enter keyword:")
    if text and key:
        messagebox.showinfo("Result", f"Decrypted text: {vigenere_cipher(text, key, encrypt=False)}")


def main():
    root = tk.Tk()
    root.title("Cipher Master")
    root.geometry("400x500")

    tk.Label(root, text="Cipher Master", font=("Arial", 18, "bold")).pack(pady=10)
    tk.Button(root, text="Encrypt with Caesar Cipher", command=encrypt_caesar).pack(pady=5)
    tk.Button(root, text="Decrypt with Caesar Cipher", command=decrypt_caesar).pack(pady=5)
    tk.Button(root, text="Encrypt with Vigenère Cipher", command=encrypt_vigenere).pack(pady=5)
    tk.Button(root, text="Decrypt with Vigenère Cipher", command=decrypt_vigenere).pack(pady=5)
    tk.Button(root, text="Play Challenge Mode", command=challenge_mode, bg="yellow").pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, bg="red").pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
