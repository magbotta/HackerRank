# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

ans = []

for a in range(0, x + 1):
    for b in range(0, y + 1):
        for c in range(0, z + 1):
            if (a + b + c) != n:
                ans.append([a, b, c])

print(ans)