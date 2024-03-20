def word_counter(text):
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Return the count of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")

    # Check for empty input
    if not user_input.strip():
        print("Error: Empty input! Please enter some text.")
        return

    # Count the words in the input
    word_count = word_counter(user_input)

    # Display the word count
    print("Word Count:", word_count)

if __name__ == "__main__":
    main()
