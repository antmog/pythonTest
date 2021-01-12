import numpy as np
import time
import timeit as tm


def main():
    time.sleep(1)
    arr = np.array([1, 2])
    print(arr.sum())
    print(arr.max())
    print(arr.min())
    print(arr.prod())

    str_arr = np.array(["one", "two", "three", "four"])
    str_arr.sort()
    print(str_arr)

    my_type = [('city', '<U32'), ('region', np.int32)]
    values = [("Moscow", 99), ("Penza", 58), ("SPB", 78)]

    regions = np.array(values, dtype=my_type)
    print(regions)
    print(type(regions))

    regions['region'].sort()
    print(regions)

    np.arange(3, 16, 4)  # from 3 to 16 with step 4


def main1():
    time.sleep(1)


print('ehlo')
print(tm.Timer(lambda: main()).timeit(5))
print(tm.Timer(lambda: main1(), 'import time').timeit(5))
