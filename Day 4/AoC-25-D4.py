# Advent of Code 2025 - Day 4

import numpy as np


input = np.loadtxt("input.txt", dtype=str)
map = np.array([list(line) for line in input])

counter = 0

for line in map:
    for i in range (len(line)-1):
        c = 0
        for j in range (len(line)-1):
            if line[j] == "@":
                if (i-1) >= 0:
                    if (j-1) >= 0 and map[i-1][j-1] == "@":
                        c += 1
                    if  map[i-1][j] == "@":
                        c += 1
                    if (j+1) < len(line)-1 and map[i-1][j+1] == "@":
                        c += 1
                if (j-1) >= 0 and map[i][j-1] == "@":
                    c += 1
                if (j+i) <= len(line)-1 and map[i][j+1] == "@":
                    c += 1
                if (i+1) <= len(line)-1:
                    if (j-1) >= 0 and map[i+1][j-1] == "@":
                        c += 1
                    if map[i+1][j] == "@":
                        c += 1
                    if (j+1) <= len(line)-1 and map[i+1][j+1] == "@":
                        c += 1
                if c < 4:
                    counter += 1

print(counter)

# j = line num
# i = row num
