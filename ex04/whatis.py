import sys

args = sys.argv[1:]
if len(args) == 0:
    pass  # do nothing
elif len(args) > 1:
    print("AssertionError: more than one argument is provided")
else:
    try:
        num = int(args[0])
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")