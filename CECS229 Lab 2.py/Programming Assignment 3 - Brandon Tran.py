# Name of Submitter: Brandon Tran (012746628)
# Group Members: Luis Rodriguez (011609011)
#                Harry Tran (017517186)

# Programming Assignment 3

from math import gcd

# Check if the list is Relatively Prime
def relativelyprime(List):
    for i in range(len(List) - 1):
        for j in range(i+1 ,len(List)):
            if gcd(List[i], List[j]) != 1:
                return False
    return True

# Compare both list
def comparetwolist(a,b):
    for i in range(len(a)):
        if a[i]is not b[i]:
            return False
    return True

# Utilize the Chinese Remainder Theorem
def chineseremaindertheorem(aList,mList):
    # Check Relatively Prime
    checkRelativePrime = relativelyprime(mList)

    # If False, return the statement "Cannot Proceed, input not pairwise relatively prime"
    if (checkRelativePrime == False):
        return "Cannot proceed, mList input not pairwise relatively prime"
    else:

        smallestValue = 0
        while True:
            remainderList=[smallestValue % num for num in mList]

            if comparetwolist(aList,remainderList):
                return smallestValue
            else:
                smallestValue += 1

# Example Problems
print(chineseremaindertheorem([2,3,2],[3,5,7]))
print(chineseremaindertheorem([1,2,3,4],[5,7,9,11]))
print(chineseremaindertheorem([1,2,3,4,8],[5,7,9,11,22]))

