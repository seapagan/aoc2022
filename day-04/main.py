"""Advent of Code 2022, 4th Dec."""


def load_data() -> list[list[tuple[int, int]]]:
    """Load the provided data and return as a nested list of tuples."""
    with open("input-data.txt") as f:
        lines = f.read().splitlines()

    result: list[list[tuple[int, int]]] = []
    for line in lines:
        temp: list[tuple[int, int]] = []
        for elf in line.split(","):
            start, end = elf.split("-")
            temp.append((int(start), int(end)))
        result.append(temp)
    return result


def part_1(data: list[list[tuple[int, int]]]) -> int:
    """Part 1 : Find complete overlaps in each group of 2 Elves.

    Return the total number of overlaps.
    """
    overlap_count: int = 0
    for pair in data:
        if ((pair[0][0] <= pair[1][0]) and (pair[0][1] >= pair[1][1])) or (
            (pair[1][0] <= pair[0][0]) and (pair[1][1] >= pair[0][1])
        ):
            overlap_count += 1

    return overlap_count


def part_2(data: list[list[tuple[int, int]]]) -> int:
    """Part 2 : Find ANY overlap in each group of 2 Elves.

    Return the total number of overlaps.
    This uses set intersection which could be quite slow for huge data sets, but
    works ok here.
    """
    overlap_count: int = 0
    for first, second in data:
        first_range = range(first[0], first[1] + 1)
        second_range = range(second[0], second[1] + 1)
        intersection = set(first_range).intersection(second_range)
        if len(intersection) != 0:
            overlap_count += 1

    return overlap_count


data = load_data()


print(f"Part 1: {part_1(data)} pairs fully contain the other.")
print(f"Part 2: {part_2(data)} pairs have some sort of overlap.")
