from datetime import datetime


#Создайте программу, которая проверяет, является ли введенное пользователем число четным или нечетным,
# и выводит соответствующее сообщение.
def check_even_odd():
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")


#Реализуйте программу, которая определяет, является ли введенная пользователем строка палиндромом
# (читается одинаково слева направо и справа налево). Выведите соответствующее сообщение.s
def check_palindrome():
    s = input("Введите строку: ")
    if s == s[::-1]:
        print("Строка является палиндромом")
    else:
        print("Строка не является палиндромом")


#Реализуйте программу, которая определяет, является ли заданное число простым (имеет только два делителя: 1 и само число)
# . Выведите соответствующее сообщение.
def check_prime():
    number = int(input("Введите число: "))
    if number <= 1:
        print("Число не является простым")
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Число не является простым")
            return
    print("Число является простым")


#.Реализуйте программу, которая определяет, является ли заданная дата корректной ().
# Выведите соответствующее сообщение. Дата дана в формате “20.01.2002”
def check_valid_date():
    date_str = input("Введите дату в формате 'дд.мм.гггг': ")
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        print("Дата корректна")
    except ValueError:
        print("Дата некорректна")


#Напишите программу для нахождения всех совершенных чисел (чисел, равных сумме своих делителей, исключая само число)
# в заданном диапазоне. Диапазон от 0 до 1000
def find_perfect_numbers():
    for num in range(1, 1001):
        divisors_sum = sum(i for i in range(1, num) if num % i == 0)
        if divisors_sum == num:
            print(num)


#Реализуйте программу для проверки, является ли заданное число числом Фибоначчи (число, которое является
# членом последовательности Фибоначчи). Заданное число 25
def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n


def check_fibonacci():
    number = int(input("Введите число: "))
    if is_fibonacci(number):
        print(f"{number} является числом Фибоначчи")
    else:
        print(f"{number} не является числом Фибоначчи")


#Напишите программу, которая определяет, является ли заданное число совершенным числом
# (число, равное сумме своих делителей, исключая само число). Выведите сообщение с результатом.
def is_perfect_number(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num


def check_perfect_number():
    number = int(input("Введите число: "))
    if is_perfect_number(number):
        print(f"{number} является совершенным числом")
    else:
        print(f"{number} не является совершенным числом")


#Создайте программу, которая определяет, в какой сезон года попадает заданная дата (месяц и день).
def find_season():
    month = int(input("Введите месяц (число): "))
    day = int(input("Введите день (число): "))

    if (month == 12 and day >= 21) or (month in [1, 2]) or (month == 3 and day < 21):
        print("Зима")
    elif (month == 3 and day >= 21) or (month in [4, 5]) or (month == 6 and day < 21):
        print("Весна")
    elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day < 21):
        print("Лето")
    else:
        print("Осень")


if __name__ == '__main__':
    check_even_odd()
    check_palindrome()
    check_prime()
    check_valid_date()
    find_perfect_numbers()
    check_fibonacci()
    check_perfect_number()
    find_season()
