# Name of Submitter: Brandon Tran (012746628)
# Team Members: Khoa Tran (017517186)
#               Luis Rodriguez (011609011)

# Problem 1
def modulus(a,b,c):
    binary = bin(b)
    print(binary)
    value = []
    answer = 1

    for i in range(len(binary) - 1):
        if(i == 0):
            value.append(1)
        elif(i == 1):
            value.append(a%c)
        else:
            v = (value[i - 1] * value[i - 1]) % c
            value.append(v)
    answerlist = []
    length = len(binary)
    for i in range(length - 2):
        if(binary[length - i - 1] == '1'):
            answerlist.append(value[i + 1])
    for i in answerlist:
        answer = answer * i;
    print(value)
    print(answerlist)
    print(answer%c)

# Print output for Problem 1
modulus(3,644,645)
print()

# Problem 2
from math import gcd
def relativelyPrime(array):
    pairwisePrime = 0;
    for i in range (0,len(array) - 1):
        for j in range(i + 1, len(array)):
            if(gcd(array[i],array[j]) != 1):
                pairwisePrime = 1
                break;
        if (pairwisePrime == 1):
            break;
    if (pairwisePrime == 1):
        print("Not Pairwise Relative Prime")
    else:
        print("Pairwise Relatively Prime")

# Print output for Problem 2
relativelyPrime([32,11,29])
relativelyPrime([32,11,29,44,8,1])
relativelyPrime([5,8])
relativelyPrime([5,8,5])
relativelyPrime([-2,4])
relativelyPrime([-2,4,3])


