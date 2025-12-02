# Part 1 (not very efficient, but it works)

input = open("input.txt").read()
input = input.split(",")
sum = 0
for idrange in input:
    idrange = idrange.split("-")
    for id in range(int(idrange[0]), int(idrange[1]) + 1):
        strid = str(id)
        length = int(len(strid))
        if length % 2 == 0:
            half = int(length / 2)
            if strid[:half] == strid[half:]:
                sum += id
print("Part 1:", sum)

# Part 2

import re

