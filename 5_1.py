import numpy as np
from collections import deque

with open("i5.txt") as f:
    lines = f.readlines()

# lines = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47""".split("\n")

rules = list()

line = lines.pop(0).strip()
while line != "":
    rules.append(tuple([int(x) for x in line.split("|")]))
    line = lines.pop(0).strip()

solution = 0
i=0
printable = np.ones(len(lines), dtype=bool)

updates = np.array([[int(x) for x in line.strip().split(",")] for line in lines], dtype=object)
for update in updates:
    update = np.asarray(update)
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if np.argwhere(update == rule[0]) >= np.argwhere(update == rule[1]):
                printable[i] = False
                break
    i+=1 

solution = np.sum([u[len(u)//2] for u in updates[printable]])
print(solution)


# part2 

order = list()
dict_order = dict()
for num in np.unique(np.asarray(rules).ravel()):
    cur_order = deque()
    cur_order.append(num)
    for rule in rules:
        idx = np.argwhere(rule == num).squeeze()
        if idx.size > 0:
            if idx == 0:
                cur_order.append(rule[1])
            else:
                cur_order.appendleft(rule[0])
    order.append(cur_order)
    if num not in dict_order:
        # this doesnt work as the numbers are alwys in the center!
        dict_order[num] = np.argwhere(cur_order==num).squeeze()[0]#
    else: 
        print("Error: Non unique index")


solution = 0
for update in updates[~ printable]:
    sorted_update = sorted(update, key=lambda x: dict_order[x])
    solution += sorted_update[len(sorted_update)//2]
print(solution)