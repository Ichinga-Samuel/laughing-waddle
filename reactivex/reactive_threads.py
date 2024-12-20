import time
from multiprocessing import cpu_count
from random import randint
from threading import current_thread

from reactivex import of, range as rx_range, interval
from reactivex.scheduler import ThreadPoolScheduler
from reactivex import operators


def long_calc(value):
    time.sleep(randint(1, 3))
    return value


otc = cpu_count()  # optimal thread count
pool_scheduler = ThreadPoolScheduler(otc)
# use subscribe_on to run operations on a separate thread
# first_process
of(1, 2, 3, 4, 5, 6, 7, 8, 9, 0).pipe(operators.map(long_calc), operators.subscribe_on(pool_scheduler)).subscribe(
    on_next = lambda x: print(f"Processed {x} on {current_thread().name} for process 1"),
    on_completed = lambda: print("Process 1 complete")
)

# second process
rx_range(30).pipe(operators.map(long_calc), operators.subscribe_on(pool_scheduler)).subscribe(
    on_next = lambda x: print(f"Processed {x} on {current_thread().name} for process 2"),
    on_completed = lambda: print("Process 2 complete")
)

# third process
interval(1).pipe(operators.map(lambda x: x*100), operators.observe_on(pool_scheduler), operators.map(long_calc)).subscribe(
    on_next = lambda x: print(f"Processed {x} on {current_thread().name} for process 3"),
    on_completed = lambda: print("Process 3 complete")
)
