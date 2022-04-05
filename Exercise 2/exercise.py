#!/usr/bin/env python3


def sonar(filename):
    with open(filename, 'r') as file:
        data = [int(x) for x in file.read().split()]
        sums = [sum([a, b, c]) for a, b, c
                in zip(data[:-2], data[1:-1], data[2:])]
        return sum(former < latter for former, latter
                   in zip(sums[:-1], sums[1:]))


def main():
    with open("output.txt") as f:
        output = [int(x.strip()) for x in f.readlines()]
    for i, expected in enumerate(output):
        filename = f"input/input_{i + 1:02}.txt"
        result = sonar(filename)
        if result == expected:
            print(f"Correct result for case {i + 1}: {result}")
        else:
            print(f"Incorrect result for case {i + 1}: {expected} is " \
                  f"expected, but {result} is returned")


if __name__ == "__main__":
    main()
