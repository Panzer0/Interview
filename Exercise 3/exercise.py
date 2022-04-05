#!/usr/bin/env python3

DAY_COUNT = 80
FIRST_CYCLE = 6
USUAL_CYCLE = 8
CYCLE_FINISHED = 0


def progress_day(data):
    data += [USUAL_CYCLE + 1 for _ in range(data.count(CYCLE_FINISHED))]
    return [FIRST_CYCLE if x == CYCLE_FINISHED else x - 1 for x in data]


def lanternfish(filename):
    with open(filename, 'r') as file:
        data = [int(x) for x in file.read().split(',')]
        for _ in range(DAY_COUNT):
            data = progress_day(data)
    return len(data)


def main():
    with open("output.txt") as f:
        output = [int(x.strip()) for x in f.readlines()]
    for i, expected in enumerate(output):
        filename = f"input/input_{i + 1:02}.txt"
        result = lanternfish(filename)
        if result == expected:
            print(f"Correct result for case {i + 1}: {result}")
        else:
            print(f"Incorrect result for case {i + 1}: {expected} is " \
                  f"expected, but {result} is returned")


if __name__ == "__main__":
    main()
