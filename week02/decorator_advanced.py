from functools import wraps
import random
import time

def retry(times=3, delay=1):
    if times < 1:
        raise ValueError("times must be at least 1")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for i in range(times):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
                    last_exception = e
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry()
def test():
    num = random.random()
    print('The random number is {}'.format(num))
    if num < 0.7:
        raise ValueError("test failed: ValueError")
    else:
        print("test succeeded!")

test()