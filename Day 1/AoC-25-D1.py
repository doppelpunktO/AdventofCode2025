def LorR(input):
    if "L" in input:
        return int(input.removeprefix("L")) * -1
    if "R" in input:
        return int(input.removeprefix("R"))

input = open("input.txt", "r").read()
input = input.split("\n")

zero1 = 0
zero2 = 0
dial = 50

for i in range(len(input)-1):
    curr = LorR(input[i])
    zero2 += abs((dial + curr) // 100) # for Part 2
    dial = (dial + curr) % 100

    if dial == 0:
        zero1 += 1
        zero2 += 1

print("Part 1:", zero1)
print("Part 2:", zero2)
