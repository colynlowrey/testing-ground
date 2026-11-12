"""Hello from my first repo!

Run it with:  python scripts/hello.py [name]
"""
import sys
from datetime import datetime


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(f"Hello, {name}!")
    print(f"Committed from a local agent on {datetime.now():%Y-%m-%d at %H:%M}.")


if __name__ == "__main__":
    main()
