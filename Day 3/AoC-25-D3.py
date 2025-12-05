# Advent of Code 2025 - Day 3
input = open("input.txt", "r").readlines()

banklist = []
for bank in input:
    bank = bank.strip("\n")
    banklist.append(int(bank))

# Part 1
def highestjoltagep1(bank):
    current1 = 0
    current2 = 0
    index1 = 0

    for index, joltage in enumerate(bank):
        if index == len(bank)-1:
            break
        joltage = int(joltage)
        if joltage > current1:
            current1 = joltage
            index1 = index
            if current1 == 9:
                    break

    for i in range(index1 +1, len(bank)):
        if int(bank[i]) > current2:
            current2 = int(bank[i])
            if current2 == 9:
                break

    return current1, current2

sum1 = 0
for bank in banklist:
    jolt1, jolt2 = highestjoltagep1(str(bank))
    joltage = (str(jolt1) + str(jolt2))
    joltage = int(joltage)
    sum1 += joltage

print("Part 1:", sum1)

# Part 2

def highestjoltagep2():



