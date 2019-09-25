"""Generate pig latin words according to given words."""
// Sosis ve salam

def main():
    """Take words from user to generate and print pig latin words."""
    while True:
        word = input("Please enter the word for turning to pig latin: ")
        print("\n\n")
        vowel = ['a', 'e', 'i', 'o', 'u']
        if word[0].lower() in vowel:
            word = word + 'yay'
            print(word)
        else:
            word = word[1:] + word[0] + "ay"
            print(word)

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")

        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
