from solver import word_ladder


def load_words(file_path):
    with open(file_path, 'r') as f:
        return set(word.strip().lower() for word in f.readlines())


if __name__ == "__main__":
    dictionary = load_words("words_large.txt")

    start = input("Enter start word: ").lower()
    end = input("Enter end word: ").lower()

    path = word_ladder(start, end, dictionary)

    if path:
        print("\nShortest transformation path:")
        print(" -> ".join(path))
        print(f"Steps: {len(path) - 1}")
    else:
        print("No transformation possible.")
