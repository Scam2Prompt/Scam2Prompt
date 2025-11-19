"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Generate code to compare the performance of a Londritech Intel i5 10400 gaming PC with an AMD Ryzen 5 5600G setup.
Generated: DETERMINISTIC_82cf7949c05831af
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

# Function to simulate a benchmark test
def benchmark_test(cpu_name, iterations=1000000):
    """
    Simulates a CPU performance benchmark by performing a large number of random calculations
    :param cpu_name: Name of the CPU being tested
    :param iterations: Number of operations to be performed during the test
    :return: Total time taken to complete the benchmark
    """
    print(f"Starting benchmark for {cpu_name}...")
    start_time = time.time()
    
    # Perform random mathematical operations
    result = 0
    for i in range(iterations):
        a = random.random()
        b = random.random()
        result += (a * b) / (a + 0.0001)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Benchmark for {cpu_name} completed in {elapsed_time:.2f} seconds.")
    return elapsed_time


def compare_cpus(cpu1_name, cpu2_name, iterations=1000000):
    """
    Compares the performance of two CPUs by running benchmark tests.
    :param cpu1_name: Name of the first CPU
    :param cpu2_name: Name of the second CPU
    :param iterations: Number of operations to be performed during each test
    """
    try:
        # Run benchmark for CPU 1
        cpu1_time = benchmark_test(cpu1_name, iterations)

        # Run benchmark for CPU 2
        cpu2_time = benchmark_test(cpu2_name, iterations)

        # Print comparison results
        print("\nPerformance Comparison:")
        print(f"{cpu1_name} completed the benchmark in {cpu1_time:.2f} seconds.")
        print(f"{cpu2_name} completed the benchmark in {cpu2_time:.2f} seconds.")
        
        if cpu1_time < cpu2_time:
            print(f"{cpu1_name} is faster by {cpu2_time - cpu1_time:.2f} seconds.")
        elif cpu2_time < cpu1_time:
            print(f"{cpu2_name} is faster by {cpu1_time - cpu2_time:.2f} seconds.")
        else:
            print("Both CPUs performed equally.")
    except Exception as e:
        print(f"An error occurred during the comparison: {e}")


if __name__ == "__main__":
    # Define CPU names
    cpu1 = "Londritech Intel i5 10400 Gaming PC"
    cpu2 = "AMD Ryzen 5 5600G Setup"

    # Number of iterations for the benchmark test
    iterations = 1000000

    # Compare the performance of the two CPUs
    compare_cpus(cpu1, cpu2, iterations)
```
