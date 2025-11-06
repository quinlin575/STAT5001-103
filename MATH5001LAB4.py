'''MATH 5001 Lab 4 Quinlin Neuhaus'''

class Backpack:
    '''Backpack object class, has a name, color, list of contents and maxsize.
    Attributes:
        name (str): The name of the backpack's owner
        contents (list): List of object in the backpack
        color (str): The color of the backpack
        maxsize (int): Maximum number of bjects that can be stored in the backpack, default=5'''
    def __init__(self, name, color, maxsize=5):
        '''Sets the name, color, and initializes backpack object with empty contents, set maxsize=5 if not given'''
        self.name = name
        self.contents = []
        self.color = color
        self.maxsize = maxsize
    
    def put(self, item):
        '''Adds an item into the backpack by appending it to the contents list if there is room'''
        if len(self.contents) < self.maxsize:
            self.contents.append(item)
        else:
            print("No Room!")
    
    def take(self, item):
        '''Removes given item from the contents list'''
        self.contents.remove(item)

    def dump(self):
        '''Empties the contents list'''
        self.contents.clear()
    
    def __eq__(self, other):
        '''Defines equality for the bacpack class, iff name, color, and number of contents are identical'''
        return self.name == other.name and self.color == other.color and len(self.contents) == len(other.contents)
    
    def __str__(self):
        '''Defines str() function for backpack class, returns the name, color, size, maxsize, and all contents as a formatted string'''
        return "Owner:\t" + self.name + "\nColor:\t" + self.color + "\nSize:\t" + str(len(self.contents)) + "\nMax Size:\t" + str(self.maxsize) + "/nContents:\t" + str(self.contents)

def test_backpack():
    '''Function for testing custom backpack class'''
    testpack = Backpack("Barry", "black")
    if testpack.name != "Barry":
        print("Name is incorrect")
    for item in ["a", "b", "c", "d", "e", "f"]:
        testpack.put(item)
    print(testpack.contents)
    
class Jetpack(Backpack):
    '''Jetpack object class, inherits from Backpack class, has a name, color, fuel level, list of contents and maxsize.
    Attributes:
        name (str): The name of the backpack's owner
        contents (list): List of object in the backpack
        color (str): The color of the backpack
        maxsize (int): Maximum number of bjects that can be stored in the backpack, default=2
        fuel (int): Amount of fuel currently in the jetpack, default=10'''
    def __init__(self, name, color, maxsize=2, fuel=10):
        '''Uses the Backpack constructor to initialize nam, color, maxsize, and contents list, also sets fuel'''
        Backpack.__init__(self, name, color, maxsize)
        self.fuel = fuel
    def fly(self, amount):
        '''Decrements fuel by given amount if there is enough fuel'''
        if amount <= self.fuel:
            self.fuel -= amount
    def dump(self):
        '''Uses Backpack dump method to empty contents list, also sets fuel to 0'''
        self.fuel = 0
        Backpack.dump(self)
    
class ComplexNumber:
    '''ComplexNumber class. Custom representation of complex numbers in a+bj form.
    Attributes:
        real (float): Real component of complex number
        imag (float): Imaginary component of complex number'''
    def __init__(self, real, imag):
        '''Default constructor for ComplexNumber class, sets real and imag'''
        self.real = real
        self.imag = imag
    def conjugate(self):
        '''Conjugate method, returns a ComplexNumber object with opposite imag'''
        return ComplexNumber(self.real, -1 * self.imag)
    def __str__(self):
        '''str() function for ComplexNumber object, returns string in a+-bj form'''
        if self.imag < 0:
            return "(" + str(self.real) + "-" + str(abs(self.imag)) + "j)"
        else:
            return "(" + str(self.real) + "+" + str(self.imag) + "j)"
    def __abs__(self):
        '''abs() function for ComplexNumber object, returns the absolute value'''
        return (self.real ** 2 + self.imag ** 2) ** .5
    def __eq__(self, other):
        '''== implementation for ComplexNumber object, returns True iff real and imag are identical'''
        return self.real == other.real and self.imag == other.imag
    def __add__(self, other):
        '''+ implementation for ComplexNumber object, return ComplexNumber object that is the sum'''
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        '''- implementation for ComplexNumber object, return ComplexNumber object that is the difference'''
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    def __mult__(self, other):
        '''* implementation for ComplexNumber object, return ComplexNumber object that is the product'''
        return ComplexNumber(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    def __truediv__(self, other):
        '''/ implementation for ComplexNumber object, return ComplexNumber object that is the quotient'''
        return ComplexNumber(self.real / other.real + self.imag / other.imag, self.imag / other.real - self.real / other.imag)
    
def test_ComplexNumber(a, b):
    '''Function for testing validity of custom ComplexNumber class against python's own complex numbers'''
    py_cnum, my_cnum = complex(a, b), ComplexNumber(a, b)

    if my_cnum.real != a or my_cnum.imag != b:
        print("__init__() set self.real and self.imag incorrectly")

    if py_cnum.conjugate().imag != my_cnum.conjugate().imag:
        print("conjugate() failed for", py_cnum)

    if str(py_cnum) != str(my_cnum):
        print("__str__() failed for", py_cnum)