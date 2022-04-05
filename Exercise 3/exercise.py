#!/usr/bin/env python3

DAY_COUNT = 80
CYCLE_STANDARD = 6
CYCLE_LONG = 8
CYCLE_FINISHED = 0


def progress_day(data):
    new_fish = data[CYCLE_FINISHED]
    for i in range(CYCLE_LONG):             # Count down
        data[i] = data[i+1]
    data[CYCLE_LONG] = new_fish             # Add newly born fish
    data[CYCLE_STANDARD] += new_fish        # Reset the timer of ready fish
    return data


def progress_day_old(data):
    data += [CYCLE_LONG + 1 for _ in range(data.count(CYCLE_FINISHED))]
    return [CYCLE_STANDARD if x == CYCLE_FINISHED else x - 1 for x in data]


def lanternfish(filename):
    with open(filename, 'r') as file:
        data = [int(x) for x in file.read().split(',')]
        formatted_data = {n: data.count(n) for n in range(CYCLE_LONG + 1)}
        for i in range(DAY_COUNT):
            formatted_data = progress_day(formatted_data)
    return sum(formatted_data.values())


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
