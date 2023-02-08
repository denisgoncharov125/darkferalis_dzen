import math
import time

RANGE_CNT = 300000000


class TestPerformance(object):
    """Класс для тестирования производительности"""

    def __init__(self, value, value2):
        self.__value = value
        self.__value2 = value2

    @property
    def value(self):
        return self.__value

    @property
    def value2(self):
        return self.__value2

    def test_perfomance_method(self):
        return math.sqrt(self.value) + math.pow(self.value2, 2)


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
    """Тестирование присвоения коллекции по индексу"""
    t_list = [None] * RANGE_CNT

    # Тут для интереса переделаем цикл for на while и протестируем как раз как бы увеличеную скорость на бинарные операции
    i = RANGE_CNT
    while i > 0:
        i -= 1
        t_list[i] = i


@time_process_decorator
def test_class_method_and_property():
    """Тестирование получений свойств класса и вызова метода"""
    s = 0
    obj_class = TestPerformance(value=342, value2=2345)
    for i in range(RANGE_CNT):
        s += obj_class.test_perfomance_method()


if __name__ == '__main__':
    test_cycle_math()  # Обычный цикл + математика
    test_cycle_2_function()  # Цикл с двумя вложенными функциями
    test_assignment_by_index()  # Тестирование присловения коллекции по индексу
    test_class_method_and_property()
