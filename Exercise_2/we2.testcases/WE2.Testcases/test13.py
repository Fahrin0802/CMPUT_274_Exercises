# Modified by Paul Lu, 2021
# Copyright By Ali Gharari, Paul Lu, 2020
# Assumes unfairDice.py is in current working directory.

import unfairDice
import sys


if __name__ == "__main__":
    print("*************************************************", file=sys.stderr)
    print("test13", file=sys.stderr)
    rolls = [2, 1, 2, 1, 2, 2, 3, 3, 1, 3, 2, 1, 3, 1, 3, 3, 2, 3, 3, 1, 2, 2, 3, 2, 2, 3, 2, 3, 1, 1, 2, 2, 3, 2, 2, 2, 1, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3, 2, 2, 1, 3, 1, 1, 3, 3, 3, 1, 1, 2, 2, 3, 3, 3, 1, 2, 3, 3, 2, 2, 3, 2, 2, 2, 3, 3, 2, 2, 1, 2, 2, 2, 2, 1, 3, 3, 2, 3, 2, 1, 2, 2, 3, 3, 2, 1, 1, 3, 1, 3, 1, 2, 3, 3, 3, 3, 3, 1, 3, 2, 3, 3, 2, 1, 1, 1, 3, 2, 1, 1, 3, 3, 2, 1, 2, 1, 2, 3, 2, 1, 1, 2, 2, 2, 3, 1, 2, 1, 3, 2, 3, 2, 1, 2, 2, 1, 3, 3, 3, 2, 3, 2, 1, 2, 1, 2, 2, 2, 3, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 3, 1, 1, 1, 3, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 3, 1, 1, 2, 3, 1, 2, 1, 3, 2, 2, 1, 1, 2, 1, 1, 2, 3, 2, 2, 2, 2, 3, 3, 2, 2, 1, 2, 3, 3, 3, 3, 3, 2, 2, 1, 2, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 3, 1, 1, 1, 2, 3, 2, 3, 3, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 3, 1, 1, 1, 3, 2, 2, 1, 1, 2, 2, 3, 1, 1, 1, 2, 2, 1, 2, 3, 1, 3, 2, 1, 1, 2, 2, 1, 2, 3, 3, 3, 2, 2, 1, 2, 3, 3, 3, 3, 1, 3, 1, 2, 3, 3, 3, 3, 3, 2, 3, 1, 1, 1, 2, 3, 1, 3, 1, 1, 1, 1, 3, 1, 2, 2, 3, 1, 1, 1, 3, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3, 2, 3, 1, 3, 3, 2, 2, 3, 3, 1, 2, 3, 3, 3, 1, 2, 3, 3, 2, 3, 1, 2, 1, 2, 3, 1, 2, 1, 3, 1, 2, 2, 1, 3, 3, 3, 1, 1, 1, 2, 1, 2, 3, 2, 1, 2, 2, 3, 3, 3, 1, 1, 3, 2, 3, 2, 2, 1, 1, 2, 1, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 2, 1, 1, 3, 2, 2, 1, 3, 3, 3, 1, 1, 3, 1, 1, 2, 1, 1, 3, 1, 2, 1, 1, 3, 2, 3, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 3, 3, 2, 2, 1, 2, 1, 3, 1, 2, 1, 3, 1, 1, 1, 3, 2, 2, 2, 2, 2, 1, 1, 3, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 3, 1, 1, 3, 2, 1, 3, 1, 3, 1, 3, 3, 3, 3, 1, 2, 2, 1, 1, 3, 2, 1, 3, 3, 1, 2, 3, 1, 2, 1, 3, 2, 2, 1, 1, 2, 3, 3, 3, 1, 3, 3, 2, 2, 2, 3, 3, 3, 3, 1, 2, 3, 2, 2, 3, 1, 1, 2, 3, 3, 3, 2, 2, 1, 1, 2, 2, 2, 3, 2, 1, 3, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 1, 3, 3, 1, 3, 3, 3, 3, 1, 1, 1, 2, 3, 1, 1, 2, 1, 1, 1, 3, 3, 1, 1, 2, 2, 3, 1, 1, 2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 3, 1, 2, 1, 2, 2, 1, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 2, 1, 2, 1, 3, 2, 3, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 3, 2, 2, 2, 1, 3, 1, 1, 1, 3, 2, 3, 3, 2, 3, 2, 3, 3, 3, 2, 1, 3, 1, 1, 1, 3, 3, 1, 1, 3, 1, 2, 2, 2, 2, 2, 3, 1, 2, 2, 1, 1, 1, 3, 3, 3, 3, 2, 1, 3, 1, 1, 2, 3, 1, 2, 1, 3, 2, 2, 1, 3, 3, 2, 2, 1, 2, 2, 3, 3, 1, 2, 2, 3, 1, 1, 3, 3, 3, 2, 2, 2, 2, 1, 3, 2, 1, 2, 3, 2, 1, 1, 1, 3, 2, 2, 3, 2, 1, 3, 1, 1, 3, 1, 1, 2, 1, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 3, 2, 3, 3, 2, 1, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 1, 1, 2, 3, 2, 2, 1, 3, 2, 1, 3, 2, 2, 1, 1, 3, 1, 2, 1, 2, 2, 2, 3, 1, 1, 3, 1, 1, 2, 1, 1, 2, 1, 2, 3, 3, 1, 3, 3, 2, 3, 2, 1, 1, 3, 3, 1, 1, 2, 3, 2, 1, 1, 3, 2, 2, 1, 1, 3, 2, 2, 1, 1, 1, 3, 2, 2, 1, 1, 3, 3, 1, 3, 2, 3, 3, 2, 3, 1, 3, 2, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 2, 1, 3, 2, 1, 1, 3, 2, 2, 3, 2, 2, 2, 1, 1, 2, 2, 3, 1, 2, 2, 1, 3, 1, 2, 2, 1, 1, 1, 3, 1, 2, 1, 3, 1, 3, 2, 1, 1, 1, 3, 1, 2, 2, 1, 3, 3, 1, 3, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 3, 3, 2, 3, 1, 3, 2, 3, 1, 2, 3, 1, 1, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 3, 3, 2, 2, 3, 1, 3, 2, 1, 2, 2, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 2, 2, 3, 1]
    unfairDice.draw_histogram(3, rolls, 10)