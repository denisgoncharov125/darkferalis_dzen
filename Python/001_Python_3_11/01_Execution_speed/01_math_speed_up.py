import math
import time

RANGE_CNT = 200000000


def test_funct(i: int) -> int:
    return math.sqrt(test_funct2(i))


def test_funct2(k: int) -> int:
    return math.pow(k, 0.335)


def time_process_decorator(func):
    """Декоратор для рамера времени выполнения"""

    def _wrapper(*args, **kwargs):
        print("\n-----------------------------------------------------------------------------------------")
        print(f"{func.__doc__} [{func.__name__}]")  # Отобразим информацию о функции
        start_time = time.perf_counter()  # Засечем время выполнения
        func(*args, **kwargs)  # Сделаем вызов самой функции из декоратора
        print(f"\nВремя выполнения {time.perf_counter() - start_time:.3f} сек.")
        print("-----------------------------------------------------------------------------------------")

    return _wrapper


@time_process_decorator
def test_cycle_math():
    """Тестирование простого цикла с математикой"""
    s = 0
    for i in range(RANGE_CNT):
        s += i
    print(f"Результат = {s}")


@time_process_decorator
def test_cycle_2_function():
    """Тестирование цикла с двумя вложенными функциями"""
    s = 0
    for i in range(RANGE_CNT):
        s += test_funct(i)
    print(f"Результат = {s}")


@time_process_decorator
def test_assignment_by_index():
    """Тестирование присвоение коллекции по индексу"""
    t_list = [None] * RANGE_CNT

    # Тут для интереса переделаем цикл for на while и протестируем как раз как бы увеличеную скорость на бинарные операции
    i = RANGE_CNT
    while i > 0:
        i -= 1
        t_list[i] = i


if __name__ == '__main__':
    test_cycle_math()
    test_cycle_2_function()
    test_assignment_by_index()
