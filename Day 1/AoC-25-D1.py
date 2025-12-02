def LorR(input):
    if "L" in input:
        return int(input.removeprefix("L")) * -1
    if "R" in input:
        return int(input.removeprefix("R"))

input = open("input.txt", "r").read()
input = input.split("\n")

zero = 0
dial = int(input[0].removeprefix("R"))
for i in range(1, len(input)-1):

    curr = LorR(input[i])
    dial = (dial + curr) % 100


    if dial == 0:
        zero += 1
print(zero)
