"""
Phase 1, Week 2 — Context Managers practice.
Covers: using built-in context managers, writing function-based managers
with @contextlib.contextmanager, and nested contexts + error handling
(both cleanup-without-suppression via try/finally, and catch-and-suppress
via try/except).
"""

import contextlib
import time


# --- 1. Using context managers -------------------------------------------
# Confirms that `with` closes a file automatically, even without an
# explicit .close() call — this is the baseline behavior everything
# else in this file builds on.

with open('week02/progress.txt', 'w') as f:
    f.write("Phase 1, Week 2 - context managers")

with open('week02/progress.txt', 'r') as f:
    print(f.read())

print(f.closed)  # True — proves __exit__ ran after the block


# --- 2. Function-based context manager (@contextlib.contextmanager) ------
# Times a block of code. Uses try/finally so the timing still prints
# even if the block raises — code placed after a bare `yield` with no
# try/finally would be skipped entirely on exception.

@contextlib.contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('Block took {} seconds.'.format(end - start))


with timer():
    sum(range(1_000_000))

# Uncomment to confirm exception-safety: the timing line still prints,
# then the exception continues propagating as normal.
# with timer():
#     raise ValueError("oops")


# --- 3. Nested contexts + error handling (cleanup, not suppression) ------
# Opens two files and yields both. Nesting `with` statements this way
# means each resource is protected by its own layer during an exception
# unwind — if opening path2 fails, path1's `with` still closes path1
# correctly, even with no manual try/finally needed for that part.

@contextlib.contextmanager
def open_files(path1, path2):
    with open(path1, 'r') as f1:
        with open(path2, 'r') as f2:
            yield (f1, f2)


with open_files('week02/progress.txt', 'week02/progress.txt') as (f1, f2):
    print("opened both files:", f1.read())

# Confirmed separately: calling open_files() with a bad second path raises
# FileNotFoundError while opening f2, but f1 still gets closed correctly
# as the exception unwinds through its own `with` block.


# --- 4. Nested contexts + error handling (catch and suppress) ------------
# Unlike timer()'s try/finally (which lets the exception keep propagating
# after cleanup), this uses try/except to actually stop the exception at
# the with-block boundary — the caller's script keeps running afterward.

@contextlib.contextmanager
def track_errors(label):
    try:
        yield
    except Exception as e:
        print(f"[{label}] failed: {e}")


with track_errors("record_1"):
    result = 10 / 0  # caught and suppressed — script keeps running

print("still running after the failure")

with track_errors("record_2"):
    result = 10 / 2  # no error — runs silently

print("done")