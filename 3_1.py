import re
import numpy as np

with open("i3.txt") as f:
    lines = f.readlines()

memory = "".join(lines).replace("\n","")
sum_out = 0

groups = re.findall(r"mul\((\d*,\d*)\)",memory)
sum_out += np.sum([np.prod([int(x) for x in group.split(",")]) for group in groups])

print(sum_out)

sum_out = 0
    # find do() and don't() groups
dos = re.finditer(r"do\(\)",memory)
valid_starts = [0] + [m.start() for m in dos]

donts = re.finditer(r"don't\(\)",memory)
valid_ends = [m.start() for m in donts]

substrings = ["do:" + s for s in memory.split("do()")]
substrings = [s.split("don't()")[0] for s in substrings]

for string in substrings:
    if string.startswith("do"):
        groups = re.findall(r"mul\((\d*,\d*)\)",string)
        sum_out += np.sum([np.prod([int(x) for x in group.split(",")]) for group in groups])

# groups = re.findall(r"mul\((\d*,\d*)\)",memory)
# sum_out += np.sum([np.prod([int(x) for x in group.split(",")]) for group in groups])

print(sum_out)