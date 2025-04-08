import numpy as np

apple = np.array([1,2,3,4,5,6,7,8,9,10])

print(apple[4])
print(apple[0:5])
#last number is exclusive 
#using colon is slciing operator 
print(apple[4:10])
#start is same, last number is last + 1
#from start, no need to put thr extra number eg instead of 0:7 u can js do :7

print(apple[:7])
print(apple[2:])

print(apple[0:10:2])
#0 is start, 10 is end, 2 is step

print(apple[1:10:2])

#to print every 2nd element
#"print(a[::2])"

print(apple[::2])

#multi dimensional array

banana = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(banana)

print(banana[1][1])

print(banana[0:2,0:2])

jam = np.arange(1,50).reshape(7,7)
print(jam)

print(jam[2:5, 2:5])

arr = np.array([1,2,3,4,5,6,7,8,9,10])
even_array = arr[arr%2 == 0]
print(even_array)
#shows even numbers

odd_array = arr[arr%2 != 0]
print(odd_array)
#shows odd numbers

pop = arr[arr == 13]
print(pop)
#to see if 13 exists within the array

lop = arr[arr == 6]
print(lop)
#prints actual value of index 6

print(arr[4])
print(arr[[2,5,8]])
#prints  value of these index numbers

plop = arr[arr < 5]
print(plop)
#all  less than index value 5 

arr += 1
print(arr)
 # makes all elements gain 1 (+1)


matA = np.arange(1,6)
matB = np.arange(6,11)

print(matA)
print(matB)

print(matA + matB)

#creating linear equations

def linear(x):
    y = (2*x)+ 3
    print(y)

linear(4)
z = np.array([1,2,3,4,5])
linear(z)