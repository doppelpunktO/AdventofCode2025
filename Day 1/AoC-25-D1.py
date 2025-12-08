# Advent of Code 2025 - Day 1
import math

def LorR(input):
    if "L" in input:
        return int(input.removeprefix("L")) * -1
    if "R" in input:
        return int(input.removeprefix("R"))

input = open("input.txt", "r").read()
input = input.split("\n")

zero1 = 0
dial = 50

for i in range(len(input)-1):
    curr = LorR(input[i])

    dial = (dial + curr) % 100

    if dial == 0:
        zero1 += 1

print("Part 1:", zero1)

# Part 2

zero2 = 0
dial = 50
for i in range (len(input)-1):
    curr = LorR(input[i])
    while True:
        if curr < 0:
            dial -= 1
            curr += 1
            dial = dial % 100
            if dial == 0:
                zero2 += 1
            if curr == 0:
                break
        elif curr > 0:
            dial += 1
            curr -= 1
            dial = dial % 100
            if dial == 0:
                zero2 += 1
            if curr == 0:
                break

print("Part 2:", zero2)