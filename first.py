# # Question No.1

# x=int(input("Enter the first number- "))
# y=int(input("Enter the second number- "))
# sum=x+y
# difference = x-y
# product=x*y
# quo = x//y
# print(sum, difference, product, quo)

# # Question No.2
# a=15
# b=4
# floor = a//b
# remainder = a%b
# power = a**b
# print(floor, remainder, power)
# pen = 15
# notebook = 40
# total_cost = pen*3+notebook*2
# print(total_cost)

# # Question No.3
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# d=int(input("Enter fourth number: "))
# e=int(input("Enter five number: "))

# average = (a+b+c+d+e)/5;
# print(average)

# # Question No.4
# n = 2;
# square = n**2
# cube = n**3
# square_root = n**0.5
# print(square, cube, square_root)

# # Question No.5
# a = int(input("Enter total seconds: "))
# min = a//60
# sec = a%60
# c=min, sec;
# print(c)

# # Question No.6
# distance=120
# time=3
# average_speed=distance//time
# print(average_speed) 

# Question 7
# num=10
# if(num >0):
#     print("Number is positive")
# else:
#     print("number is negative")

# Question 8
# age = 15
# if(age >=18):
#     print("Eligible to vote")
# elif(age<18):
#     print("Not eligible to vote")
# else:
#     print("Invalid age")

# Question 9
# number = int(input("Enter a number: "))
# if(number%2==0):
#     print("Number is even")
# else:
#     print("Number is odd")

# Question 10
# num1 = int(input("Enter 1st number"))
# num2 = int(input("Enter 2nd number"))
# if(num1>num2):
#     print(num1)
# elif(num1<num2):
#     print(num2)
# else:
#     print("Invalid number")

# Question 11
# num=int(input("Enter a number: "))
# if(num%5==0):
#     print("Number is divisible by 5")
# else:
#     print("Invalid number")

# Question 12
# marks=int(input("Enter your marks: "))
# if(marks>=90):
#     print("A")
# elif(marks>=75 and marks<90):
#     print("B")
# elif(marks>=50 and marks<75):
#     print("C")
# else:
#     print("Fail")

# Question 13
# year=int(input("Enter year: "))
# if(year%4==0):
#     print("Year is leap year")
# else:
#     print("Year is not leap year")

# Question 14
# num=int(input("Enter a number: "))
# if(num<10):
#     print("Number is single digit number")
# elif(num>=10 and num<100):
#     print("Number is double digit number")
# else:
#     print("More than two digits")

# Question 15
# temp = int(input("Enter a temperature: "))
# if(temp<0):
#     print("Freezing")
# elif(temp>=0 and temp>=20):
#     print("Cold")
# elif(temp>21 and temp<35):
#     print("Warm")
# else:
#     print("Hot")

# Question 16
# num = int(input("Take a number: "))
# positive = num%2==0;
# if(num>=0):
#     if(positive):
#         print("Number is even and positive")
#     else:
#         print("Odd and positive")

#for loop

# for i in range(5):
#     print(i)

#while loop

# count = 0
# while count < 5:
#     print(count)
#     count -=1

#print numbers from 1 to 10
# for i in range(11):
#     print(i)

# sum=0
# count=0
# while count <=10:
#     sum +=count
#     count+=1
# print(sum)

#Table
# table=int(input("Enter a number: "))
# for i in range(1, 11):
#     print(i*table)

#factorial
# num=int(input("Enter a number: "))
# fact=1
# i=1
# while i <= num:
#     fact*=i
#     i+=1
# print(fact)

# num=int(input("Enter a number: "))
# rev = 0
# while num >0:
#     digit = num%10
#     rev = rev*10+d
#     num = num//10
# print(rev)

#even numbers
# for i in range(1, 50):
#     if(i%2==0):
#         print(i)

rows = 5
for i in range(1, rows + 1):     
    for j in range(1, i + 1):
        print("* ", end="")                
    print("")

