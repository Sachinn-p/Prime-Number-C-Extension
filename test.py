import time
import tracemalloc
import prime



def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sum_primesPY(N):
    total = 0
    for num in range(2, N + 1):
        if is_prime(num):
            total += num
    return total



def benchmark(func, *args, **kwargs):
    """Measure execution time and memory usage of a function."""
    # Start memory tracing
    tracemalloc.start()

    # Start time
    start_time = time.perf_counter()

    # Call the function
    result = func(*args, **kwargs)

    # Stop time
    end_time = time.perf_counter()

    # Capture memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "result": result,
        "time_sec": end_time - start_time,
        "memory_kb": current / 1024,
        "peak_memory_kb": peak / 1024,
    }


# ---- Test Both Functions ----

N = 10_000_000

c_ext = benchmark(prime.sum_primes, N)
py_ver = benchmark(sum_primesPY, N)

print("\n--- C EXTENSION (prime.sum_primes) ---")
print(f"Result          : {c_ext['result']}")
print(f"Time (seconds)  : {c_ext['time_sec']:.6f}")
print(f"Memory (KB)     : {c_ext['memory_kb']:.2f}")
print(f"Peak Memory (KB): {c_ext['peak_memory_kb']:.2f}")

print("\n--- PURE PYTHON (sum_primesPY) ---")
print(f"Result          : {py_ver['result']}")
print(f"Time (seconds)  : {py_ver['time_sec']:.6f}")
print(f"Memory (KB)     : {py_ver['memory_kb']:.2f}")
print(f"Peak Memory (KB): {py_ver['peak_memory_kb']:.2f}")


print(prime.sum_primes(1000000))    # 17
print(sum_primesPY(1000000))   # 1060
