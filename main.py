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

#palindrome problem 
x =222

original = x

rev = 0

while(x!=0):
    remainder = x % 10
    rev = rev * 10 + remainder
    x//=10
    
if original== rev:
    print("palindrome")

else:
    print("not palindrome")

x = 22
temp = x

while(temp>0):
    temp//=10

print(temp)
#armstrong numberr 
x = 153 
temp = x
digits = 0
while(temp>0):
    digits+=1
    temp//=10

temp = x
sum = 0
while(temp>0):
    remainder = temp % 10
    sum +=remainder ** digits 
    temp//=10
if sum == x:
    print("armstrong")
else:
    print("not armstrong")
#prime number

x = 67
is_prime = True

if x <= 10:
    is_prime = False
else:
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            is_prime =False
            break
if is_prime:
    print("prime")

#palindrome in a sentense
x = "A man a plan a canal Panama"
clean =""
for ch in x:
    if ch.isalnum():
        clean = ch.lower()
rev =""
for ch in clean:
    rev = ch + rev

if rev==clean :
    print("palindrome")
else:
    print("Not a palindrome")

#longest word in a sentence

x = "eddie ate dinamite good bye eddie"

words = x.split()
longest =""
for i in words:
    if len(i)>= len(longest):
        longest = i
    
print(longest)
#Anagram words
x = "spar"
y ="rasp"

l = list(y)

for ch in x:
    if ch in l:
        l.remove(ch)
    else:
        print('no')
        break
else:
    print("yes")
    
if sorted(x)==sorted(y):
    print("yes")
else:
    print("No")

#uppercase the first word
x = "spar them"
y = x.split()
upper = []
for i in y:
   upper.append(i[0].upper() + i[1:])

print(upper)
