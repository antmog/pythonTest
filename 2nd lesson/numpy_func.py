import numpy as np
import timeit as tm


def main():
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


print(tm.Timer('main').timeit(1000000)/1000000)
