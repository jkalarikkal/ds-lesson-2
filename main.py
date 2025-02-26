import numpy as np

apple = np.array([1,2,3,4,5,6,7,8,9,10])

print(apple[4])
print(apple[0:5])
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
