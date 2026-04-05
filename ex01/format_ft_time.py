import datetime
import time


def format_unix_time(timestamp: float | None = None) -> tuple[str, str, str]:
    if timestamp is None:
        timestamp = time.time()

    decimal = f"{timestamp:,.4f}"
    scientific = f"{timestamp:.2e}"
    date_text = datetime.datetime.fromtimestamp(timestamp).strftime("%b %d %Y")
    return decimal, scientific, date_text


formatted, scientific, date_text = format_unix_time()
print(f"Seconds since January 1, 1970: {formatted} or {scientific} in scientific notation")
print(f"{date_text}")
