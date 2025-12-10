# Advent of Code 2025 - Day 2
# Part 1 (not very efficient, but it works)

input = open("input.txt").read()
input = input.split(",")
sum1 = 0
for idrange in input:
    idrange = idrange.split("-")
    for id in range(int(idrange[0]), int(idrange[1])):
        strid = str(id)
        length = int(len(strid))
        if length % 2 == 0:
            half = int(length / 2)
            if strid[:half] == strid[half:]:
                sum1 += id
print("Part 1:", sum1)

# Part 2
import textwrap

sum2 = 0

def findpattern(s):
    for i in range(1, (len(s) // 2)+1):
        linelist = textwrap.wrap(s, i)
        if linelist.count(linelist[0]) == len(linelist):
            return True
    return False

for idrange in input:
    idrange = idrange.split("-")
    for id in range(int(idrange[0]), int(idrange[1]) + 1):
        strid = str(id)
        if findpattern(strid):
            sum2 += id

print("Part 2:", sum2)

