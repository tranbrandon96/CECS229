# Name: Brandon Tran (ID: 012746628)
# Due Date: Febuary 15, 2019

# Problem 1
seconds_in_decade = 10 * 365 * 24 * 3600
print(seconds_in_decade)

# Problem 2
remainder_with_mod = 5789248 % 14
print(remainder_with_mod)

# Problem 3
remainder_without_mod = 5789248 - 14 * (5789248 // 14)
print(remainder_without_mod)

# Problem 4
cubes_minus_one = {(x * x * x) - 1 for x in {2,4,6,8,10}}
print(cubes_minus_one)

# Problem 5
M = [1,2,3,4,5]
squares_minus_value = [M[x]**2 - x for x in range(0,len(M))]
print(squares_minus_value)

# Problem 6
intersection = {((x + 1) * 2) for x in range(30)}.intersection({((x + 1) ** 2) for x in range(30)})
print(intersection)
