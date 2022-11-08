# Advent of Code 2020

# Input Getter
with open("input.txt") as f:
    progInput = [line.rstrip() for line in f]

# Variables
validPw = 0


# Functions
def splitDash(dashStr):
    dslen = len(dashStr)
    if dslen == 3:
        return [int(dashStr[0]), int(dashStr[2])]
    elif dslen == 5:
        return [int(f"{dashStr[0]}{dashStr[1]}"), int(f"{dashStr[3]}{dashStr[4]}")]
    elif dslen == 4:
        if dashStr[1] == '-':
            return [int(dashStr[0]), int(f"{dashStr[2]}{dashStr[3]}")]
        else:
            return [int(f"{dashStr[0]}{dashStr[1]}"), int(dashStr[3])]
        
def getLetter(letterStr):
    return letterStr[0]


# Main Code
for i in progInput:
    i = i.split()
    i[0] = splitDash(i[0])
    i[1] = getLetter(i[1])
    minAmt = i[0][0]
    maxAmt = i[0][1]
    actualAmt = 0
    letter = i[1]
    for char in i[2]:
        if char == letter:
            actualAmt += 1
    if actualAmt >= minAmt and actualAmt <= maxAmt:
        validPw += 1
print(validPw)


