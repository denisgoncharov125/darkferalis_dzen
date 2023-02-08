import time

if __name__ == '__main__':

    # s = 0 Обычный цикл и обычная математика
    s = 0
    start_time = time.perf_counter()

    for i in range(100000000):
        s += i
    print(f"Результат = {s}")

    print(f"Время выполнения {time.perf_counter() - start_time:.3f} сек.")
