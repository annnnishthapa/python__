#finding the maximum and minimum element in a list
x =[1,2,3,4,5,6]
min  = 0
max  = 0
for i in x:
    if i < min:
         min = i
    else:
         max = i

print("max : ", max)
print("min : ", min)


#sun of the elements

x = [1,2,3,4 ,5 ]
sum = 0
for i in x:
    sum += i

print(sum)

#find the second largest element in a list

largest = second_largest = x[0]
for i in x:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)
       