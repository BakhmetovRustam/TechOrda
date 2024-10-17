##int-cmp Дается два числа a и b. Вернуть: 1, если a > b 0, если a = b -1, если a < b
def int_cmp(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


##max-of-three Дается три числа a, b и c. Вернуть максимальное число из них.
def max_of_three(a, b, c):
    return max(a, b, c)


##sqr-sum-1-n Вернуть сумму квадратов чисел от 1 до n включительно
def sqr_sum_1_n(n):
    return sum(i * i for i in range(1, n + 1))


##print-even-a-b Вывести в консоль четные числа в диапазоне от a включительно до b включительно
def print_even_a_b(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=' ')


##pow-a-b Вернуть число a в степени b. Используя цикл.
def pow_a_b(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result


##calc-deposit Написать функцию, которая возвращает сколько будет денег на депозите
# через n месяцев при ставке k и изначальном балансе b тенге. Вознаграждения по депозиту начисляются каждый месяц
def calc_deposit(n, k, b):
    for _ in range(n):
        b += b * (k / 100)
    return b


##Min Реализовать функцию min, которая возвращает минимальное число из массива. Если в массиве нет элементов, верните 0
def min_value(array):
    if not array:
        return 0
    return min(array)


##range Реализовать функцию range, которая создает массив размером n, заполняет ячейки значениями от 1 до n
# и возвращает созданный массив.
def create_range(n):
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return arr


##sum Реализовать функцию sum, которая возвращает сумму чисел массива. Пример int array[] = {7, 5, 9, 1, 4};
# int sum_number = sum(array);
def sum_array(array):
    return sum(array)

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]



if __name__ == '__main__':
    print(int_cmp(1, 0))
    print(max_of_three(42, 1, 0))
    print(sqr_sum_1_n(3))
    print_even_a_b(0, 4)
    print()
    print(pow_a_b(2, 6))
    print(calc_deposit(1, 5, 1000))
    print(min_value([1, 2, 3, ]))
    print(range_n(10))
    print(sum_array([1, 2, 3, 4, 5]))
