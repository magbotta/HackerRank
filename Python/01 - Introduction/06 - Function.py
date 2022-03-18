
# ************************
#       Information
# ************************

# Direct Link: https://www.hackerrank.com/challenges/write-a-function/problem
# Difficulty: Medium
# Max Score: 10
# Language: Python

# ************************
#         Solution
# ************************

def is_leap(year):
    leap = False
    
    # Write your logic here
    
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))