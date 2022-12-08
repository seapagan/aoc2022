"""Advent of Code 2022, 8th Dec."""


# ------------------------------- load the data ------------------------------ #
def get_data() -> list[list[int]]:
    with open("input-data.txt") as f:
        return [list(map(int, line)) for line in f.read().splitlines()]


# -------------------------- calculations for part 2 ------------------------- #
def check_up(row, column: int, tree_grid: list[list[int]]) -> int:
    up = 0
    this_tree = tree_grid[row][column]
    for i in range(row - 1, -1, -1):
        up += 1
        if tree_grid[i][column] >= this_tree:
            break
    return up


def check_down(row, column: int, tree_grid: list[list[int]]) -> int:
    down = 0
    this_tree = tree_grid[row][column]
    for i in range(row + 1, len(tree_grid)):
        down += 1
        if tree_grid[i][column] >= this_tree:
            break
    return down


def check_left(row, column: int, tree_grid: list[list[int]]) -> int:
    left = 0
    this_tree = tree_grid[row][column]
    for i in range(column - 1, -1, -1):
        left += 1
        if tree_grid[row][i] >= this_tree:
            break
    return left


def check_right(row, column: int, tree_grid: list[list[int]]) -> int:
    right = 0
    this_tree = tree_grid[row][column]
    for i in range(column + 1, len(tree_grid[row])):
        right += 1
        if tree_grid[row][i] >= this_tree:
            break
    return right


# -------------------------- find answer for part 1 -------------------------- #
def part_1(tree_grid: list[list[int]]) -> int:
    total = 0
    for row in range(len(tree_grid)):
        for column in range(len(tree_grid[row])):
            this_tree = tree_grid[row][column]
            if (
                all(tree_grid[row][i] < this_tree for i in range(column))
                or all(tree_grid[row][i] < this_tree for i in range(column + 1, len(tree_grid[row])))
                or all(tree_grid[i][column] < this_tree for i in range(row))
                or all(tree_grid[i][column] < this_tree for i in range(row + 1, len(tree_grid)))
            ):

                total += 1
    return total


# -------------------------- find answer for part 2 -------------------------- #
def part_2(tree_grid: list[list[int]]) -> int:
    best = 0
    for row in range(len(tree_grid)):
        for column in range(len(tree_grid[row])):
            up = check_up(row, column, tree_grid)
            down = check_down(row, column, tree_grid)
            left = check_left(row, column, tree_grid)
            right = check_right(row, column, tree_grid)
            best = max(best, up * down * left * right)
    return best


data = get_data()

print(f"The number of visible trees is : {part_1(data)}")
print(f"The highest Scenic score is : {part_2(data)}")
