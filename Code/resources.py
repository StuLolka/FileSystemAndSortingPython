# Алгоритм сортировки по методу пузырька (возрастание)
def buble_sort_ascending(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


# Алгоритм сортировки по методу пузырька (убывание)
def buble_sort_descending(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j + 1] > lst[j]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


#Алгоритм "Шейкерная сортировка" (возрастание)
def shaker_sort_ascending(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        for i in range(start, end):
            if lst[i] > lst[i + 1]:
                lst[i + 1], lst[i] = lst[i], lst[i + 1]
        end -= 1

        for i in range(end, start, -1):
            if lst[i] < lst[i - 1]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
        start += 1
    return lst


#Алгоритм "Шейкерная сортировка" (убывание)
def shaker_sort_descending(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        for i in range(start, end):
            if lst[i] < lst[i + 1]:
                lst[i + 1], lst[i] = lst[i], lst[i + 1]
        end -= 1
        for i in range(end, start, -1):
            if lst[i] > lst[i - 1]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
        start += 1
    return lst


# Tests
def test(test_func, is_descending=False):
    name = f"{test_func.__name__} test"
    lst_1 = [3, 2, 5, 10, 15, 20, 0, -1]
    lst_2 = [0, 1, 2, 3]
    lst_3 = [9, 6, 5, 0, -1]
    lst_4 = [1]
    for i, lst in enumerate([lst_1, lst_2, lst_3, lst_4]):
        test_sort_result = test_func(lst)
        sorted_result = sorted(lst, reverse=is_descending)
        result = test_sort_result == sorted_result
        if not result:
            print(f"\n {name} {i + 1} is failed ❌")
            print(f"\tExpected: {sorted_result}")
            print(f"\t{name} returned: {test_sort_result}\n")
        else:
            print(f"\n {name} {i + 1} is passed ✅", end="")
    print()


def start_tests():
    test(buble_sort_ascending)
    test(buble_sort_descending, True)
    test(shaker_sort_ascending)
    test(shaker_sort_descending, True)


if __name__ == "__main__":
    start_tests()
