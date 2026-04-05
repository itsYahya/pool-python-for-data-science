import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def main():
    """Encode a string argument into Morse Code."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]

        if not isinstance(text, str):
            raise AssertionError("the arguments are bad")

        bad_characters = [c for c in text.upper() if c not in NESTED_MORSE]
        if bad_characters:
            raise AssertionError("the arguments are bad")
        result = "".join(NESTED_MORSE[c] for c in text.upper())
        print(result.rstrip())
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
