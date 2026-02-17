def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

PI = 3.14159

def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def reverse_string():
    string = input("Enter a string: ")
    revese = ""
    for ch in string:
        revese = ch + revese
    print("Reversed String: ", revese)

def square(num):
    return num*num

def cube(num):
    return num*num*num

def c_to_f(C):
    return (C*9/5)+32

def f_to_c(F):
    return (F-32)*5/9

def area_of_circle(r):
    return PI*r*r
def area_of_rectangle(l, w):
    return l*w
def area_of_triangle(b, h):
    return 1/2*b*h

def say_hello(name):
    return f"Hello {name}! Have a great day!"

# list_tools.py

def unique_elements(lst):
    result = []
    for item in lst:
        found = False
        for r in result:
            if r == item:
                found = True
                break
        if not found:
            result.append(item)
    return result