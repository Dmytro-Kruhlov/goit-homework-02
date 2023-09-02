from threading import Thread
from time import time
import multiprocessing


class FactorThread(Thread):
    def __init__(self, target, args=()):
        super().__init__(target=target, args=args)

        self.result = None

    def run(self):
        self.result = self._target(*self._args)


def factors(num):
    nums = [n for n in range(1, num + 1) if num % n == 0]
    return nums


def factorizing(*nums):
    st = time()
    result = []

    for num in nums:
        result.append(factors(num))
    at = time()
    time_in_work = at - st
    return result, time_in_work


def factorizing_with_threads(*nums):
    st = time()
    threads = []

    for num in nums:
        th = FactorThread(target=factors, args=(num,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    result = [th.result for th in threads]
    at = time()

    time_in_work = at - st
    return result, time_in_work


if __name__ == "__main__":
    # st = time()
    # result = factorizing_with_threads(128, 255, 99999, 10651060, 2134151, 13141, 214151, 23151521)
    # et = time()
    # print(et - st)
    st = time()
    result2 = factorizing(128, 255, 99999, 10651060, 2134151, 13141, 214151, 23151521)
    et = time()
    print(et - st)
    numbers = [128, 255, 99999, 10651060, 2134151, 13141, 214151, 23151521]
    num_processes = multiprocessing.cpu_count()
    print(num_processes)
    pool = multiprocessing.Pool(processes=num_processes)
    start_time = time()
    parallel_result = pool.map(factors, numbers)
    pool.close()
    pool.join()
    end_time = time()

    print(end_time - start_time)
