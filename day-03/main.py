"""Advent of Code 2022, 3rd Dec."""


def read_rucksack_data() -> list[str]:
    """Load the provided Rucksack data into a list."""
    with open("input-data.txt") as f:
        return f.read().splitlines()


def split_rucksack(contents: str) -> tuple[str, str]:
    """Split the provided rucksack into it's 2 compartments.

    Returns a tuple.
    """
    str_len = len(contents) // 2
    return contents[:str_len], contents[str_len:]


def get_common_items(rucksack: tuple) -> str:
    """Return a string with the common items between two sides of rucksack.

    Uses Python sets with the 'intersection' method (finds common values between
    two sets). Convert the resulting set to a string.
    """
    first, second = rucksack
    return "".join(set(first).intersection(second))


def get_item_priority(item: str) -> int:
    """Return an integer with the priority of the provided item.

    We can do this using the ASCII code.
    Upper case start at ASCII 65 though to 90
    Lower case start at ASCII 97 though to 122

    No error checking, assume the provided character is a letter.
    """
    value = ord(item)
    if value >= 97:
        # it's lowercase
        return value - 96
    # otherwise assume uppercase, and adjust to start at 27
    return value - 64 + 26


def group_by_3(data: list[str]) -> list[list[str, str, str]]:
    """Group the list of rucksacks by 3's in a new list."""
    return [data[i : i + 3] for i in range(0, len(data), 3)]


def get_common_in_group(group: list[str]) -> str:
    """Return common items in each group of 3 rucksacks.

    We use Python 'set' again then convert to a string.
    """
    return "".join(set.intersection(*map(set, group)))


def part1(raw_data: list[str]) -> None:
    """Calculate the result for part 1 of the challenge."""
    common: list[int] = []
    for rucksack in raw_data:
        common_value = get_common_items(split_rucksack(rucksack))
        common.append(get_item_priority(common_value))
    print(f"The sum of all priorities for Part 1 is {sum(common)}")


def part2(raw_data: list[str]) -> None:
    """Calculate the result for part 2 of the challenge."""
    priorities = []
    grouped_rucksacks = group_by_3(raw_data)
    for group in grouped_rucksacks:
        badge = get_common_in_group(group)
        priorities.append(get_item_priority(badge))
    print(f"The sum of all priorities for Part 2 is {sum(priorities)}")


raw_data = read_rucksack_data()
part1(raw_data)
part2(raw_data)
