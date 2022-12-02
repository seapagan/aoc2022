"""Advent of Code 2022, 1st Dec."""
from itertools import groupby

cal_list = []

# get every line into a list, without the newlines.
with open("cal-data.txt") as f:
    lines = f.read().splitlines()

# group each block into a sub list in the list.
chunks = (list(g) for k,g in groupby(lines, key=lambda x:x !="") if k)

# convert to list of sum of each sublist
for chunk in chunks:
    cal_list.append(sum(map(int,chunk)))

# get the top 3 Calorie carriers
top_3 = sorted(cal_list, reverse=True)[:3]


print(f"Max calories carried by ONE Elf is {top_3[0]}")
total_top_3 = sum(top_3)
print(f"The total calories carried by the top 3 Elves is {total_top_3} ")
