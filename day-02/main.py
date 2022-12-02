"""Advent of Code 2022, 2nd Dec."""
from typing import List, Tuple


def part1(game_data: List[Tuple[str,str]]) -> int:
    # define the win/draw conditions. Don't need loss, it has zero points
    win = [('A','Y'),('B','Z'),('C','X')]
    draw = [('A','X'),('B','Y'),('C','Z')]

    scores = {'X': 1, 'Y':2, 'Z': 3}

    master_total = 0

    for game in game_data:
        game_total = 0
        _,my_play = game
        if game in win:
            game_total += 6
        elif game in draw:
            game_total += 3
        game_total += scores[my_play]

        master_total += game_total

    return master_total


def part2(game_data) -> int:
    # define win/loss combinations.
    win = [('A','B'),('B','C'),('C','A')]
    lose = [('A','C'),('B','A'),('C','B')]

    scores = {'A': 1, 'B':2, 'C': 3}

    master_total = 0

    for game in game_data:
        game_total = 0
        opponent,outcome = game
        if outcome == 'X':
            # I need to lose.
            _,my_play = [item for item in lose if opponent == item[0]][0]
            game_total += scores[my_play]
        elif outcome == 'Y':
            # in this case a draw, so my play == opponent play.
            game_total += scores[opponent] +3
        else:
            # I need to win.
            _,my_play = [item for item in win if opponent == item[0]][0]
            game_total += scores[my_play] +6

        master_total += game_total

    return master_total

# get the data into a list of tuples
with open("input-data.txt") as f:
    game_data = [
        tuple(game.split(" ")) for game in f.read().splitlines()
    ]

print(f"The total points (Part 1 rules) is {part1(game_data)}")
print(f"The total points (Part 2 rules) is {part2(game_data)}")
