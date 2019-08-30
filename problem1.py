"""
Multiples of 3 and 5
Problem 1

Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

# natural_numbers = []
# for i in range(1, 10):
#     if i % 3 == 0:
#         natural_numbers.append(i)
#     elif i % 5 == 0:
#         natural_numbers.append(i)

# print (natural_numbers)

import numpy as np

print(np.sum([x for x in range(1, 1000) if (x % 3 == 0) or (x % 5 == 0)]))
