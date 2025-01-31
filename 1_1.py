import numpy as np

with open("i1.txt") as f:
    lines = f.readlines()

data = np.array([line.split("   ") for line in lines], dtype=int)

left = np.sort(data.T[0])
right = np.sort(data.T[1])

diffs = np.sum(np.abs(left - right))

print (diffs)

# part2 

right_bins = np.bincount(right)

sim_score = np.sum(left * right_bins[left])
print(sim_score)