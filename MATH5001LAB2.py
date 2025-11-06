'''MATH 5001 Lab 2 Quinlin Neuhaus'''
import calculator
import box
import itertools 
import random
import sys
import time

def func1(L):
    '''Returns the min, max, and mean of a list'''
    return min(L), max(L), sum(L) / len(L)

integer = int(3)
newinteger = integer
newinteger +=1 
if (newinteger == integer):
    print("Integers are mutable")
else:
    print("Integers are immutable")

string = str("test")
newstring = string
newstring = newstring + "s"
if (newstring == string):
    print("Strings are mutable")
else:
    print("Strings are immutable")

oldlist = [1, 2, 3]
newlist = oldlist
newlist.append(4)
if (newlist == oldlist):
    print("Lists are mutable")
else:
    print("Lists are immutable")

tuple = func1(oldlist)
newtuple = tuple
newtuple += (1,)
if (newtuple == tuple):
    print("Tuples are mutable")
else:
    print("Tuples are immutable")

oldset = {"a", "b", "c"}
newset = oldset
newset.add("d")
if (newset == oldset):
    print("Sets are mutable")
else:
    print("Sets are immutable")

def hypotenuse(x, y):
    '''Returns the length of the hypotenuse of a right triangle with legs x and y'''
    return calculator.sqrt(calculator.sum(calculator.product(x, x), calculator.product(y, y)))

def pwrset(iterable):
    '''Returns the powerset of the iterable'''
    output = list(iterable)
    final = []
    powerset =  itertools.chain.from_iterable(itertools.combinations(output, i) for i in range(len(output) + 1))
    for i in powerset:
        final.append(set(i))
    return final

if __name__ == "__main__" and len(sys.argv) == 3:
    '''Plays the "Shut the Box" game if executed from a command line with player name and time arguements'''
    win = True
    playername = sys.argv[1]
    gametime = float(sys.argv[2])
    timeremaining = gametime
    starttime = time.time()
    numsremaining = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        if timeremaining - (time.time() - starttime) <= 0:
            win = False
            print("Game Over!")
            break
        print("Numbers left: ", numsremaining)
        roll = random.randint(1,6) + random.randint(1,6)
        print("Roll: ", roll)
        if not(box.isvalid(roll, numsremaining)):
            win = False
            print("Game Over!")
            break
        while True:
            if timeremaining - (time.time() - starttime) <= 0:
                win = False
                print("Game Over!")
                break
            print("Seconds left: ", round(timeremaining - (time.time() - starttime), 2))
            inputnums = box.parse_input(input("Numbers to eliminate: "), numsremaining)
            print()
            if sum(inputnums) == roll:
                break
            else:
                print("Invalid Input")
        for i in inputnums:
            numsremaining.remove(i)
        timeremaining = timeremaining - (time.time() - starttime)
        if len(numsremaining) == 0:
            break
    if win:
        print("\nScore for player ", playername, ": ", sum(numsremaining), " points")
        print("Time played: ", round(gametime - timeremaining, 2), " seconds")
        print("Congratulations you shut the box")
    else:
        print("\nScore for player ", playername, ": ", sum(numsremaining), " points")
        print("Time played: ", round(gametime - timeremaining, 2), " seconds")
        print("Better luck next time >:)")