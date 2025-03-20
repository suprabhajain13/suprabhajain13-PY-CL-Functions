# app.py

from lab import count_vowels

def main():
    text = input("Enter a string: ")
    num_vowels = count_vowels(text)
    print("Number of vowels in the text:", num_vowels)

if __name__ == "__main__":
    main()
