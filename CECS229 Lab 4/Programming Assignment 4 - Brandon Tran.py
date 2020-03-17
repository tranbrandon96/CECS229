# Name of Submitter: Brandon Tran (012746628)
# Group Members: Luis Rodriguez (011609011), Harry Tran (017517186)
# Due Date: April 19, 2019
# Programming Assignment 4

def RSAencrypt(n, e, message):
    # Set Single Digit numbers to Double Digits and assign them to letters
    # Set Double Digit numbers to letters
    letterDictionary = \
        {"A": "00",
         "B": "01",
         "C": "02",
         "D": "03",
         "E": "04",
         "F": "05",
         "G": "06",
         "H": "07",
         "I": "08",
         "J": "09",
         "K": "10",
         "L": "11",
         "M": "12",
         "N": "13",
         "O": "14",
         "P": "15",
         "Q": "16",
         "R": "17",
         "S": "18",
         "T": "19",
         "U": "20",
         "V": "21",
         "W": "22",
         "X": "23",
         "Y": "24",
         "Z": "25"}

    # If statement for text that are blank
    if len(message) < 1:
        print("\'Message length needs to be greater than 0.\'")
    else:

        N = len(str(n))
        bTester = "25"
        for i in range(1, N - 1, 2):
            bTester += str(25)
        if int(bTester) <= n:
            bS = len(bTester)
        else:
            bS = len(bTester) - 2

        mLength = len(message) * 2
        pString = "X"
        while mLength % bS != 0:
            message += pString
            mLength = len(message) * 2

        iRep = ""
        for letter in message:
            iRep += letterDictionary[letter]

        blocks = []
        for o in range(0, len(iRep) - 1, bS):
            blocks.append(iRep[o:o + bS])

        fBlock = []
        for y in blocks:
            y = int(y)
            y = y ** e % n
            y = str(y)
            fBlock.append(y.zfill(bS))

        print(fBlock)

# Test Outputs
RSAencrypt(2537, 13, "STOP")
RSAencrypt(2537, 13, "ABC")
RSAencrypt(2537, 13, "")
RSAencrypt(256027, 21, "HELLO")