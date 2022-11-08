# Advent of Code 2020

# Input Getter
with open("input.txt") as f:
    progInput = [line.rstrip() for line in f]

# Variables
inputInt = []


# Functions



# Main Code
for i in progInput:
    inputInt.append(int(i))

for i in inputInt:
    for j in inputInt:
        if i + j == 2020:
            print(i*j)
