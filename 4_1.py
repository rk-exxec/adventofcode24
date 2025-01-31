import numpy as np

with open("i4.txt") as f:
    lines = f.readlines()

# lines = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX""".split("\n")


data = np.array([list(line) for line in lines], dtype=str)
# data = data.reshape(data.size, len(lines[0]))

xses = np.argwhere(data == "X")

# find MAS letters in all directions from X
xmas_count = 0  

def find_mas(idx_arr):
    try:
        if np.any(idx_arr < 0):
            return 0
        if (data[idx_arr.T[0],idx_arr.T[1]] == np.array(["M","A","S"])).all():
            # print(data[idx_arr.T[0],idx_arr.T[1]], idx_arr)
            return 1
    except IndexError as ie:
        return 0
    return 0

possible_dirs = np.array([[0,1],[1,0],[1,1],[1,-1],[-1,0],[0,-1],[-1,-1],[-1,1]])[...,np.newaxis].repeat(3,axis=-1) * np.array(range(1,4))
for x in xses:
    for direc in possible_dirs:
        offset_dirs = x + direc.T
        xmas_count += find_mas(offset_dirs)

print(xmas_count)
#
# # part 2

kernel = np.array([[1,0,1],[0,1,0],[1,0,1]], dtype=bool)
#slide kernel over data and count the number of MAS in each window
mas_count = 0
for i in range(data.shape[0]-2):
    for j in range(data.shape[1]-2):
        values = data[i:i+3,j:j+3][kernel]
        if list(values) in [["M","M","A","S","S"],["S","S","A","M","M"],["M","S","A","M","S"],["S","M","A","S","M"]]:
            mas_count += 1

print(mas_count)