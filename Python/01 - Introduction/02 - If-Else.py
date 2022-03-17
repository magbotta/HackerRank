#!/bin/python3
# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-if-else/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import math
import os
import random
import re
import sys


N = int(input())

if (N % 2 == 1) | (6 <= N <= 20):
    print("Weird")
elif N >= 2 & N <= 5:
    print("Not Weird")
elif N > 20:
    print()