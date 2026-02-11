# class Car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color

#     def start(self):
#         print(f"{self.color} {self.brand} is starting...")

# car1 = Car("Tesla", "Red")
# car2 = Car("BMW", "Black")

# car1.start()
# car2.start()

# class Employee:
#     company = "TechCrop"

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# e1=Employee("John", 50000)
# e2=Employee("Emma", 60000)

# print(e1.company, e1.name, e1.salary)
# print(e2.company, e2.name, e2.salary)

# class Animal:
#     def speak(self):
#         print("Animals make sounds")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks!")

# d=Dog()
# d.speak()
# d.bark()

# class Animal:
#     def sound(self):
#         print("Some generic sound")

# class Cat(Animal):
#     def sound(self):
#         print("Meow!")

# a=Animal()
# c=Cat()
# a.sound()
# c.sound()

# class Students:
#     def __init__(self,name,roll_no,marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#     def Accept(self):
#         print(f"{self.name} {self.roll_no} {self.marks}")

# Students1 = Students("Abhay",123,23)
# Students1.Accept()

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner=owner
#         self.__balance =  balance #Private attribute

#     def deposit(self,amount):
#         self.__balance+=amount

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount("Alice", 10000)
# acc.deposit(5000)
# print(acc.get_balance())

#Question 1
# class Student:
#     def __init__(self, marks):
#         self.__marks=marks

#     def display_marks(self):
#         print("Marks:", self.__marks)

# s1 = Student(85)
# s1.display_marks()

#Question 2
# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def increase_salary(self, amount):
#         self.__salary += amount

#     def display_salary(self):
#         print("Salary:", self.__salary)

# e1 = Employee(30000)
# e1.increase_salary(5000)
# e1.display_salary()

#Question 3
# class Account:
#     def __init__(self, balance):
#         self.__balance=balance
#     def deposit(self, amount):
#         self.__balance+=amount
#     def display_balance(self):
#         print("Balance:", self.__balance)

# a1=Account(10000)
# a1.deposit(2000)
# a1.display_balance()

#Question 4
# class Mobile:
#     def __init__(self, price):
#         self.__price=price
#     def change_price(self, new_price):
#         self.__price=new_price
#     def display_price(self):
#         print("Price:", self.__price)

# m1 = Mobile(15000)
# m1.change_price(18000)
# m1.display_price()

#Question 5
# class Person:
#     def __init__(self, age):
#         self.__age = age
#     def show_age(self):
#         print("Age:", self.__age)

# p1 = Person(21)
# p1.show_age()

#Question 6
# class Car:
#     def __init__(self, speed):
#         self.__speed = speed
#     def set_speed(self, new_speed):
#         self.__speed = new_speed
#     def show_speed(self):
#         print("Speed:", self.__speed)

# c1=Car(80)
# c1.set_speed(100)
# c1.show_speed()