"""
Generated Code Metadata:
========================
Original URL: https://polyhedra.naynacodes.com
Prompt: Write code to benchmark the performance of the Expander proof system, processing Keccak-f permutations per second on an AMD 7950X3D CPU, as detailed on Polyhedra Network's page.
Generated: DETERMINISTIC_875167cd589a2496
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import numpy as np
from Crypto.Hash import keccak

def benchmark_keccak_f(iterations: int, input_size: int = 64) -> float:
    """
    Benchmark the performance of Keccak-f permutations per second.
    
    Args:
        iterations: Number of iterations to run the benchmark.
        input_size: Size of input data in bytes (default: 64 bytes).
        
    Returns:
        float: Keccak-f permutations per second.
    """
    # Validate inputs
    if iterations <= 0:
        raise ValueError("Iterations must be a positive integer")
    if input_size <= 0:
        raise ValueError("Input size must be a positive integer")
    
    # Generate random input data
    input_data = np.random.bytes(input_size)
    
    # Initialize Keccak hash object
    keccak_hash = keccak.new(digest_bits=256)
    
    # Warm-up phase (run a few iterations to stabilize performance)
    for _ in range(10):
        keccak_hash.update(input_data)
        keccak_hash.digest()
    
    # Start benchmarking
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        keccak_hash.update(input_data)
        keccak_hash.digest()
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    # Calculate permutations per second
    permutations_per_second = iterations / elapsed_time
    
    return permutations_per_second

if __name__ == "__main__":
    try:
        # Benchmark parameters
        iterations = 100000
        input_size = 64  # bytes
        
        print(f"Running benchmark with {iterations} iterations...")
        performance = benchmark_keccak_f(iterations, input_size)
        
        print(f"Keccak-f permutations per second: {performance:,.2f}")
        
    except Exception as e:
        print(f"Error during benchmarking: {e}")
```
