"""Your agent in one emoji.

The whole entry lives in entry.txt: one emoji that says what an agent
is -- on duty, at your service, no words needed. This script only
carries it to stdout, exactly as written.
"""

import os


def entry_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def load_entry():
    with open(entry_path(), encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    agent = load_entry()
    if agent:
        print(agent)


if __name__ == "__main__":
    main()
