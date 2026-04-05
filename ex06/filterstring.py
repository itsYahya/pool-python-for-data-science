import sys


def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items that
    are true."""
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


def main():
    """Parse arguments and print filtered words with length greater than N."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        threshold = sys.argv[2]

        if not isinstance(text, str) or not isinstance(threshold, str):
            raise AssertionError("the arguments are bad")

        try:
            n = int(threshold)
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = text.split(" ")
        result = ft_filter(lambda word: len(word) > n, words)
        print(result)
    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
