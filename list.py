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
#merging two list

def merge_list(l1,l2):
    new_list = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i]==l2[j]:
            new_list.append(l1[i])
            i+=1
            j+=1
        elif l1[i] <= l2[j]:
            new_list.append(l1[i])
            i+=1
        else:
            new_list.append(l2[j])
            j+=1
    while i < len(l1):
        new_list.append(l1[i])
        i+=1
    while j < len(l2):
        new_list.append(l2[j])
        j+=1
    return new_list

a = [1,3,4,5,6]
b = [5,7,8,9]  

print(merge_list(a,b))
    
    
    