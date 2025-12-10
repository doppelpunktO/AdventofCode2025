# Advent of Code 2025 - Day 4

import numpy as np

def surroundings(row, col):
    surround= []
    if row != 0 and col != 0:
        if map[row-1][col-1] == "@":
            surround.append(map[row-1][col-1]) # upper left
    if row != 0:
        if map[row-1][col] == "@":
            surround.append(map[row-1][col]) # upper
    if row != len(map) - 1:
        if map[row + 1][col] == "@":
            surround.append(map[row+1][col]) # under
    if col != 0:
        if map[row][col-1] == "@":
            surround.append(map[row][col-1]) # left
    if col != len(map) - 1:
        if map[row][col+1] == "@":
            surround.append(map[row][col+1]) # right
    if row != len(map) - 1 and col != len(map) - 1:
        if map[row + 1][col + 1] == "@":
            surround.append(map[row+1][col+1]) # under right
    if row != 0 and col != len(map) - 1:
        if map[row - 1][col + 1] == "@":
            surround.append(map[row-1][col+1]) # upper right
    if row != len(map) - 1 and col != 0:
        if map[row + 1][col - 1] == "@":
            surround.append(map[row+1][col-1]) # under left

    return surround


input = np.loadtxt("input.txt", dtype=str)
map = np.array([list(line) for line in input])

sum1 = 0
for row in range(len(map)):
    for col in range(len(map)):
        if map[row][col] == "@":
            sur = surroundings(row,col)
            count = sur.count("@")
            if count < 4:
                sum1 += 1
print("Part 1:", sum1)

count = 0
sum2 = 0
for r in range(41):
    for row in range(len(map)):
        for col in range(len(map)):
            if map[row][col] == "@":
                sur = surroundings(row, col)
                count = sur.count("@")
                if count < 4:
                    sum2 += 1
                    map[row][col] = "."
print("Part 2:", sum2)

