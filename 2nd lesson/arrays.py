import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)
print(arr.size)
print(arr.shape)

print('reshaping')
print("reshaping")
x = arr.reshape((2, 3))
print(arr)
print(x)

print(x.shape)
print(x.size)

print(x[:])
print(x[0:1])  # 1 2 3
print(x[9999:0])  # []
print(x[0:1, 0:4])  # 1 2 3
print(x[1, 2])  # 6

print(x > 5)
print(x * 5)

arr1 = np.array([2, 3, 12])
arr2 = np.array([i for i in range(12)])
print(arr1)
print(arr2)

test = np.array([(i in arr2) for i in arr1])
print(test)

print(arr1[test])
