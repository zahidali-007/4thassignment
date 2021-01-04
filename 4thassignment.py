# ------------------------------->>> Functions <<<-------------------------------
#           -------->>> Function Without Parameters <<<--------
def my_function():
    print("Hello from a simple function")


print("Function without Parameters")
my_function()

#             -------->>> Function With Parameters <<<--------


def my_function_withParameter(fname, lname):
    print(fname + " " + lname)


print("Function with Parameters")
my_function_withParameter("Zahid", "Ali")

# By passing arbitrary keyword arguments, (**kwargs)
# function will recieve dictionary argument


def my_friends(**friend):
    print("last name of my friend is " + " " + friend["lname"])


my_friends(fname="Ali", lname="Khan")
# by passing Arbitrary Arguments, (*args) ....*args access item accordingly
# function will recieve tuple arguments


def my_best_friend(*friend):
    print("My best friend is" + " " + friend[1])


my_best_friend("Farhan", "Hassan", "Hannan")
# Keyword Arguments
# we can also send arguments with the key = value syntax.


def my_friend(f1, f2, f3):
    print("My best friend is " + f2)


my_friend(f1="Ali", f2="Farhan", f3="Arslan")
# default parameter value


def my_friends_from_city(city="Sanjar pur"):
    print("my best friend is from " + city)


my_friends_from_city("Sadiqabad")
# Passing a List as an Argument


def list_as_argument(book):
    for x in book:
        print(x)


books = ["Informaation Security", "Artificial Intelligence", "Data Structure"]
list_as_argument(books)
# return values


def in_number(number):
    return 5 * number


print(in_number(4))
print(in_number(5))
print(in_number(6))
# pass statement


def passed_func():
    pass  # if function with no content put the pass statement to avoid getting error

# ------------------------------->>> Methods <<<-------------------------------


class Person:
    def __init__(self, name, age):  # Init function it works like constructor
        self.name = name
        self.age = age

    def myfunc(self):  # Method
        print("Hello my name is " + self.name)
        print("My age is ", self.age)


p1 = Person("Zahid Ali ", 21)  # Object of class
p1.myfunc()  # object called by method

# ------------------------------->>> Recursive Method <<<-------------------------------


def try_recursion(num):
    if(num > 0):
        result = num + try_recursion(num - 1)
        print(result)
    else:
        result = 0
    return result


print("\nRecursion Example Results")
try_recursion(5)
