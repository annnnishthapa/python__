#simple calculator
x = int(input("Enter a number: "))
y = int(input("Enter second number: "))
operation = input("which operation do you want to perform?")

if operation =="+":
    result = x + y
elif operation =="-":
    result = x -y
elif operation =="*":
    result = x*y

else:
    print("Error")

print(result)

#swap two numbers

x = 1
y = 2

temp = x
x = y
y= temp 
print(x,y)

#odd even
x = 3

if x/2 is True :
    print("even")
else:
    print("odd")

#largest of three numbers
x = 1
y = 2
z = 3

if x > y and x > z:
    print("x is largest")
elif y > x and y > z:
    print("y is largest")
elif z > x and z > y:
    print("z is largest")
else:
    print("they are equal.")

#leap year
year = int(input("enter the year: "))

if (year%4 == 0) and ( year%100 !=0 or year%400 == 0):
    print("It is a leap year.")
else :
    print("Not a leap year.")

#CESIUS TO FEHERENHIGHT
temp = int(input("Enter the temperature. "))

value = input("if you want to convert fron C to F press 1 or vice versa press 2. ")

if value == "2":
    C = (temp - 32) * 5/9
    print(C)
elif value == "1" :
    f = (temp * 9/5) + 32
    print(f)

#square root and cube root.
x = 9

square_root = x ** 1/2
print(square_root)
cube_root = x ** 1/3
print(cube_root)

#multiplicationn 
n= 7

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

#factorial of a number
n = 0
fact = 1 
for i in range(1,n+1):
    fact *= i

print(fact)

#fibonacci series
n = int(input("enter the no of series: "))

a , b = 0 ,1

for i in range(n):
    print(a , end = " ")
    
    a , b = b , a + b

#reverse a number 
n = int(input("Enter the no: "))
reverse = 0 

while(n!=0):
    remainder = n % 10
    reverse = reverse * 10 + remainder
    n//= 10
     
print(reverse)


