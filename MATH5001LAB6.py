'''Math 5001 Lab 6 Quinlin Neuhaus'''

from random import choice

def arithmagic():
    '''Prompts user for input and returns sum of the difference of a three digit number and its reverse and the reverse of that difference'''
    step_1 = input("Enter a 3-digit number where the first and last digits differ by 2 or more: ")
    if len(step_1) != 3:
        raise ValueError("This is not a three digit number")
    if abs(int(step_1[2]) - int(step_1[0])) < 2:
        raise ValueError("The first and last digits must differ by two or more")
    step_2 = input("Enter the reverse of the first number, obtained by reading it backwards: ")
    if step_1[0] != step_2[-1] or step_1[1] != step_2[-2] or step_1[2] != step_2[-3]:
        raise ValueError("These numbers are not reverses")
    step_3 = input("Enter the positive difference of these numbers: ")
    if step_3 != abs(int(step_1) - int(step_2)):
        raise ValueError("Not the positive difference")
    step_4 = input("Enter the reverse of the previous result: ")
    if step_3[0] != step_4[-1] or step_3[1] != step_4[-2] or step_3[2] != step_4[-3]:
        raise ValueError("These numbers are not reverses")
    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")

def random_walk(max_iters=1e12):
    '''Returns the final position of a random walk of max_iters steps with default = 1 trillion, if keyboard interrupted, prints the step it was on'''
    walk = 0
    directions = [-1,1]
    try:
        for i in range(int(max_iters)):
            walk += choice(directions)
    except KeyboardInterrupt:
        print("Function Interrupted at ", i)
    else:
        print("Function Completed")
    finally:
        return walk

class ContentFilter:
    '''ContentFilter class for simple file i/o
    Attributes:
    filename: name of read file
    contents: string of all contents of filename
    '''
    def __init__(self, filename):
        '''Constructor for ContentFilter class, accepts read file name as an arguement, prompts user to input filename until a vlid one is chosen, counts the number of characters, letters, digits, spaces, and lines'''
        self.filename = None
        self.contents = None
        while True:
            try:
                with open(filename, "r") as f:
                    self.contents = f.read()
                self.filename = filename
                break
            except:
                filename = input("Enter a valid filename:\t")
        self.numchar = len(self.contents)
        self.numletter = sum([i.isalpha() for i in self.contents])
        self.numdigit = sum([i.isnumeric() for i in self.contents])
        self.numspace = sum([i.isspace() for i in self.contents])
        self.numline = sum([i == "\n" for i in self.contents]) + 1

    def uniform(self, outfile, mode="w", case="upper"):
        '''Uniform method writes the read file to the outfile in specified case and write mode'''
        if mode not in ["w", "x", "a"]:
            raise ValueError("Enter a valid mode")
        if case not in ["upper", "lower"]:
            raise ValueError("Enter a valid case")
        data = ""
        if case == "upper":
            data = self.contents.upper()
        else:
            data = self.contents.lower()
        with open(outfile, mode) as f:
            f.write(data)
    
    def reverse(self, outfile, mode="w", unit="line"):
        '''Reverse method writes the read file to the outfile by reversing lines or reversing words, specifies write mode'''
        if mode not in ["w", "x", "a"]:
            raise ValueError("Enter a valid mode")
        if unit not in ["line", "word"]:
            raise ValueError("Enter a valid case")
        data = ""
        lines = self.contents.splitlines()
        if unit == "line":
            data = "\n".join(lines[::-1])
        else:
            data = "\n".join([" ".join(line.split()[::-1]) for line in lines])
        with open(outfile, mode) as f:
            f.write(data)
    
    def transpose(self, outfile, mode="w"):
        '''Transpose method writes the read file to the outfile by swapping the rows and columns of the read file, specifies write mode'''
        if mode not in ["w", "x", "a"]:
            raise ValueError("Enter a valid mode")
        data = ""
        lines = [i.split() for i in self.contents.splitlines()]
        transpose = zip(*lines)
        transposelines = [" ".join(i) for i in transpose]
        data = "\n".join(transposelines)
        with open(outfile, mode) as f:
            f.write(data)

    def __str__(self):
        '''String method defines ContentFilter class behavior for str() function, returns formatted filename, and counts of characters, letters, digits, spaces, and lines'''
        return (
            f"Source file:\t{self.filename}\n"
            f"Total characters:\t{self.numchar}\n"
            f"Alphabetic characters:\t{self.numletter}\n"
            f"Numerical characters:\t{self.numdigit}\n"
            f"Whitespace characters:\t{self.numspace}\n"
            f"Number of lines:\t{self.numline}"
        )
