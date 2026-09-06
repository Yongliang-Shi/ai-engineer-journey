# decorator_basic.py
from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def foo(value):
    time.sleep(1)
    print(value)

foo("hello")

@timer
def sum_range(n):
    total = 0
    for i in range(n):
        total += i+1
    print(total)

sum_range(10000)