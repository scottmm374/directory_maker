import os
from pathlib import Path

# parent_dir = '/Users/michellescott/Documents/Lambda/code_challenges/Advent-Of-Code/'

years = 2015

while years <= 2020:

    directory = str(years)
    os.mkdir(directory)

    for days in range(1, 26):
        sub_dir = f'day_{days}'
        os.mkdir(os.path.join(directory, sub_dir))
        Path(os.path.join(directory, sub_dir, "instructions.md")).touch()
        Path(os.path.join(directory, sub_dir, "input.txt")).touch()
        Path(os.path.join(directory, sub_dir, "day"+str(days)+".py")).touch()
    years += 1
