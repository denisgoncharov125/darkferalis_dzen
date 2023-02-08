import math
import time

def test_funct(i: int) -> int:
    return math.sqrt(test_funct2(i))


def test_funct2(k: int) -> int:
    return math.pow(k, 0.335)


if __name__ == '__main__':

    start_time = time.perf_counter()
    #l = []
    #l = range(100000000)

    s = 0
    for i in range(100000000):
        s += test_funct(i)
        #l[i] = s
    print(f"Результат = {s}")

    print(f"Время выполнения {time.perf_counter() - start_time:.3f} сек.")
