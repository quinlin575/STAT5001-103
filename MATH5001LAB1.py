'''MATH 5001 Lab 1 Quinlin Neuhaus'''

def sphere_volume(r):
    '''Returns volume of sphere with radius r'''
    return 4.0*3.14159*pow(float(r),3) / 3.0

def isolate(a, b, c, d, e):
    '''Prints first three characters with 5 spaces between, the last one with one space between'''
    print(a, b, c, sep="     ", end="")
    print(" ", end="")
    print(d, e, sep=" ")

def first_half(word):
    '''Return first half of characters in string, excluding middle character'''
    outputword = ""
    for i in range((len(word)) // 2):
        outputword = outputword + word[i]
    return outputword

def backward(word):
    '''return a string of the input string in reverse order'''
    outputword = ""
    for i in range(len(word)):
        outputword = outputword + word[-i - 1]
    return outputword

def list_ops():
    '''Performs list operations according to the problem'''
    givenlist = ["bear", "ant", "cat", "dog"]
    givenlist.append("eagle")
    givenlist[2] = "fox"
    givenlist.pop(1)
    givenlist.sort(reverse=True)
    givenlist[givenlist.index("eagle")] = "hawk"
    givenlist.append("hunter")
    return givenlist

def pig_latin(word):
    '''Converts input word into pig latin'''
    if word[0] in ["a", "e", "i", "o", "u"]:
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"

def palindrome():
    '''Finds and returns the largest palindrome that is the product of two three digit numbers'''
    guess = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            current = i*j
            if (backward(str(current)) == str(current)) and current > guess:
                guess = current
    return guess

def alt_harmonic(n):
    '''return the sum of the first n alternating harmonic numbers'''
    return sum([(pow(-1, i) / (i+1)) for i in range(int(n))])