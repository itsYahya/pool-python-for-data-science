import sys
import string


def main():
    """
    Main function to analyze a string and count its character types.
    Takes a single string argument or prompts for input if none provided.
    Counts upper-case letters, lower-case letters, punctuation marks,
    spaces, and digits.
    Raises AssertionError if more than one argument is provided.
    """
    try:
        if len(sys.argv) == 1:
            number_of_tries = 2
            index = 0
            while index < number_of_tries:
                try:
                    print("What is the text to count?")
                    text = sys.stdin.readline()
                    if len(text) > 0:
                        break
                    index += 1
                except KeyboardInterrupt:
                    sys.exit(0)
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("AssertionError: more than one argument is provided")
        total = len(text)
        if total == 0:
            print("The text contains 0 characters.")
            return
        upper = sum(1 for c in text if c.isupper())
        lower = sum(1 for c in text if c.islower())
        punct = sum(1 for c in text if c in string.punctuation)
        space = sum(1 for c in text if c.isspace())
        digit = sum(1 for c in text if c.isdigit())
        print(f"The text contains {total} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
