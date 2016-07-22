import random

def larger_random():
    """Return random number higher than last one"""
    lowest = 0
    while True:
        candidate = random.uniform(lowest, 1)
        if candidate <= lowest:
            continue
        else:
            lowest = candidate
            yield candidate

