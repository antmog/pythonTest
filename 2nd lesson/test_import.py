import numpy as np

my_list1 = [2, 4, 5]
print(my_list1)
print(type(my_list1))

my_np_list1 = np.array(my_list1)
print(my_np_list1)
print(type(my_np_list1))
print(my_np_list1.dtype)

my_list2 = [2, 3.3]
my_np_list2 = np.array(my_list2)
print(my_np_list2.dtype)

print(my_list2)
print(my_np_list2)

my_list3 = [2, 3.3, 'text']
my_np_list3 = np.array(my_list3)
my_np_list4 = np.array(my_list3, dtype='<U2')
print(my_np_list3.dtype)

print(my_list3)
print(my_np_list3)
print(my_np_list4)
