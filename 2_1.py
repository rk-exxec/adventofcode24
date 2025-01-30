#2_1
import numpy as np

with open("i2.txt") as f:
    lines = f.readlines()

# lines = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# 1 5 2 4 5""".split("\n")

nums = [np.fromstring(line, dtype=int, sep=' ') for line in lines]

diffs = [np.diff(x) for x in nums]

# count all the differences that are 

unsafe_counter = 0
safe_counter = 0

def mask_issues(diff):
    signs = np.sign(diff)
    monoton_iss_idx = np.where(np.diff(signs) != 0)[0]
    diff_iss_idx = np.where(~((diff <= 3) & (diff >= -3)))[0]
    return np.unique(list(monoton_iss_idx) + list(diff_iss_idx))


issues_arr = [mask_issues(diff) for diff in diffs]

safe_counter = np.sum([(~np.any(issues))*1 for issues in issues_arr])

print(safe_counter)

# part 2
safe_counter = 0
unsafe_counter = 0
unifxable_nums = []
for i in range(len(issues_arr)):
    if len(issues_arr[i]) == 0:
        safe_counter += 1
    elif len(issues_arr[i]) == 1:
        new_diff = np.diff(np.delete(nums[i], issues_arr[i]+1))
        if len(mask_issues(new_diff)) == 0:
            safe_counter += 1
        else:
            unsafe_counter += 1
            unifxable_nums.append(nums[i])
    elif len(issues_arr[i]) == 2 and (issues_arr[i][1] - issues_arr[i][0]) == 1:
        new_diff = np.diff(np.delete(nums[i], issues_arr[i][1]))
        if len(mask_issues(new_diff)) == 0:
            safe_counter += 1
        else:
            unsafe_counter += 1
            unifxable_nums.append(nums[i])
    else:
        unsafe_counter += 1


print(safe_counter)
# print(unifxable_nums)