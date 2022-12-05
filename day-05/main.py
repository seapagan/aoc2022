"""Advent of Code 2022, 5th Dec.

For this challenge, the starting stacks and the operation plan are in the same
data file. Instead of just hard-coding the starting stack, I want to decode it
automatically, without any external libraries. This way the solution will work
unmodified for any users own input, and it's extra practice :D
"""

from copy import deepcopy
from itertools import groupby


def get_raw_data() -> list[list[str]]:
    """Return the raw data, but split the starting stack off the instructions.

    Return a nested list containing both parts.
    """
    with open("input-data.txt") as f:
        all_data = f.read().splitlines()
        grouped_data = [
            list(x)
            for key, x in groupby(all_data, lambda e: e == "")
            if not key
        ]
        return grouped_data


def decode_stacks(stacks) -> list[list[str]]:
    """Decode the incoming stack data into a format we can manipulate.

    This returns a list of lists, the sublists each being one stack with the top
    of the stack at the start of the list.
    """
    rows: list[list[str]] = []
    # create our list of lists with the stack data
    for line in stacks:
        rows.append([line[i : i + 4] for i in range(0, len(line), 4)])

    number_of_stacks = len(rows[0])

    # create empty list of lists to hold the formatted data
    stack_list: list[list[str]] = [[] for _ in range(number_of_stacks)]
    # fill it
    for row in rows[:-1]:
        for index, item in enumerate(row):
            stack_list[index].append(item.strip()[1:-1])
    # remove the empty items
    clean_list = [[s for s in sub_list if s] for sub_list in stack_list]

    return clean_list


def decode_procedure(procedure) -> list[tuple[int, int, int]]:
    """Decode the procedure into a list of tuples.

    Each tuple will be (number_to_move, start_stack, end_stack) as integers
    """
    result: list = []
    for line in procedure:
        temp = line.split()
        result.append((int(temp[1]), int(temp[3]), int(temp[5])))
    return result


def perform_procedure_part1(
    stack_list: list[list[str]], procedure: list[tuple[int, int, int]]
) -> str:
    """Actually do the stack movements."""
    stack_list = deepcopy(stack_list)  # deepcopy as lists are mutable
    for line in procedure:
        count, start, end = line
        for _ in range(count):
            crate = stack_list[start - 1].pop(0)
            stack_list[end - 1][:0] = crate

    top_list = [stack[0] for stack in stack_list]

    # return this as a combined string
    return "".join(top_list)


def perform_procedure_part2(
    stack_list: list[list[str]], procedure: list[tuple[int, int, int]]
) -> str:
    """Do the stack movements with the CrateMover 9001."""
    stack_list = deepcopy(stack_list)  # deepcopy as lists are mutable
    for line in procedure:
        count, start, end = line
        print(count, start, end)
        crates = stack_list[start - 1][:count]
        print(crates)
        stack_list[start - 1] = stack_list[start - 1][count:]
        stack_list[end - 1] = crates + stack_list[end - 1]

    top_list = [stack[0] for stack in stack_list if stack]

    # # return this as a combined string
    return "".join(top_list)


# get the raw data, split the list it into 2 new lists.
raw_stacks, raw_procedure = get_raw_data()

stacks = decode_stacks(raw_stacks)
procedure = decode_procedure(raw_procedure)

part1_result = perform_procedure_part1(stacks, procedure)
part2_result = perform_procedure_part2(stacks, procedure)

print(f"Result for part 1 is '{part1_result}'")
print(f"Result for part 2 is '{part2_result}'")
