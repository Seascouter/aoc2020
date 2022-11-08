# Advent of Code 2020

# Input Getter
with open("input.txt") as f:
    progInput = [line.rstrip() for line in f]

# Variables
position = {
    "x": 0,
    "y": 0
}

velocity = {
    "x": 1,
    "y": 2
}

# 3, 1: 240
# 1, 1: 70
# 5, 1: 68
# 7, 1: 67
# 1, 2: 37


treeCount = 0

# Functions



# Main Code
while (position["y"] < 323):
    while len(progInput[position["y"]]) <= position["x"]:
        progInput[position["y"]] = f"{progInput[position['y']]}{progInput[position['y']]}"
    if progInput[position["y"]][position["x"]] == '#':
        treeCount += 1
    position["x"] += velocity["x"]
    position["y"] += velocity["y"]

print(f"Multiplied Count: {240*70*68*67*37}")
