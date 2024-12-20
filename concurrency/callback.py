import threading
import time

def wait_and_print_blocking(msg):
    time.sleep(1)
    print(msg)


def wait_and_print_nonblocking(msg):
    def call_back():
        print(msg)

    timer = threading.Timer(1, call_back)
    timer.start()


def wait_and_print(blocking=True):
    start = time.perf_counter()
    for i in range(5):
        if blocking:
            wait_and_print_blocking(f'msg{i}')
        else:
            wait_and_print_nonblocking(f"msg{i}")
    print(f"Completed in {time.perf_counter() - start}")

wait_and_print(blocking=False)


# Futures


    
