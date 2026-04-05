import os
import sys


def ft_tqdm(lst: range) -> any:
    """
    A tqdm-like progress bar implementation using yield.
    
    Args:
        lst: A range object to iterate over
        
    Yields:
        Each element from the range
    """
    total = len(lst)
    term_width = os.get_terminal_size().columns
    bar_width = term_width - 30

    for i, elem in enumerate(lst, 1):
        percentage = (i / total) * 100
        filled = int((i / total) * bar_width)
        bar = "=" * filled + ">"
        bar = bar.ljust(bar_width)

        sys.stdout.write(f"\r{percentage:.0f}%|[{bar}]| {i}/{total}")
        sys.stdout.flush()
        yield elem

    sys.stdout.write("\n")
    sys.stdout.flush()
