#2_1
import numpy as np

with open("i2.txt") as f:
    lines = f.readlines()

# lines = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9""".split("\n")

nums = [np.fromstring(line, dtype=int, sep=' ') for line in lines]

diffs = [np.diff(x) for x in nums]

# count all the differences that are 

unsafe_counter = 0
safe_counter = 0

def mask_issues(diff):
    signs = np.sign(diff)
    zero_diff_idx = np.argwhere(diff==0)
    monoton_iss_idx = np.argwhere(np.diff(signs) != 0)+1
    diff_iss_idx = np.argwhere(np.abs(diff)>3)
    return np.unique(list(zero_diff_idx) + list(monoton_iss_idx) + list(diff_iss_idx))


issues_arr = [mask_issues(diff) for diff in diffs]

safe_counter = np.sum([(~np.any(issues))*1 for issues in issues_arr])

print(safe_counter)

# part 2
# safe_counter = 0
# unsafe_counter = 0
# unifxable_nums = []
# for i in range(len(issues_arr)):
#     if len(issues_arr[i]) == 0:
#         safe_counter += 1
#     elif len(issues_arr[i]) == 1:
#         new_diff = np.diff(np.delete(nums[i], issues_arr[i]))
#         if len(mask_issues(new_diff)) == 0:
#             safe_counter += 1
#         else:
#             unsafe_counter += 1
#             unifxable_nums.append(nums[i])
#     elif len(issues_arr[i]) == 2 and (issues_arr[i][1] - issues_arr[i][0]) == 1:
#         new_diff = np.diff(np.delete(nums[i], issues_arr[i][1]))
#         if len(mask_issues(new_diff)) == 0:
#             safe_counter += 1
#         else:
#             unsafe_counter += 1
#             unifxable_nums.append(nums[i])
#     else:
#         unsafe_counter += 1
safe_counter = 0
safe_idx = []
for i in range(len(nums)):
    if mask_issues(np.diff(nums[i])).size == 0:
        safe_counter += 1
        safe_idx.append(i)
    else:
        for j in range(len(nums[i])):
            if mask_issues(np.diff(np.delete(nums[i], j))).size == 0:
                safe_counter += 1
                safe_idx.append(i)
                break



print(safe_counter)
# print(safe_idx)
# print(unifxable_nums)
# print([mask_issues(np.diff(x)) for x in unifxable_nums])

safe_idx2 = []
def checkSafety(report):
    """ Checks if a report is safe. """
    deltas = np.diff(report)
    
    # prüfen, ob legale Schrittgröße vorliegt
    if np.any(np.abs(deltas) > 3) or np.any(deltas == 0):
        return False
    
    # Monotonie (streng) überprüfen
    monotony = np.all(deltas > 0) or np.all(deltas < 0) 
    return monotony

def is_safe_with_removal(report):
    """ Checks if a report can get safe by removing one level. """
    # brute force: jedes Element einmal rauslöschen und prüfen, ob Report dann "safe" ist
    for i in range(0, len(report)):
        newReport = np.delete(report, i)
        if checkSafety(newReport):
            return True
    return False

with open("i2.txt") as file:
    safeCounter = 0
    i=0
    for line in file:
        ## read line data and convert to numpy int array
        raw_report = line.rsplit()
        report = np.array(raw_report, dtype=int)
        
        ## analyze lines
        if not checkSafety(report):
            if is_safe_with_removal(report): 
                safeCounter += 1
                safe_idx2.append(i)
        else: 
            safeCounter += 1
            safe_idx2.append(i)
        i+=1
        
    print(f"Number of safe reports (allowing one faulty level): \n{safeCounter}")

print(set(safe_idx) - set(safe_idx2))
