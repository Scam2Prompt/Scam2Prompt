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
import subprocess
import platform
import psutil
import time
import os

def run_benchmark(command):
    """
    Run a benchmarking command and return the output.

    Args:
        command (str): The command to execute for benchmarking.

    Returns:
        str: The output of the command.
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running benchmark: {e}")
        return None

def get_system_info():
    """
    Get system information for the current machine.

    Returns:
        dict: A dictionary containing system information.
    """
    return {
        "OS": platform.system(),
        "CPU": platform.processor(),
        "CPU_Cores": psutil.cpu_count(logical=True),
        "RAM": round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert to GB
    }

def main():
    # Define benchmarking commands for both setups
    commands = {
        "Londritech Intel i5 10400": "sysbench --test=cpu --num-threads=4 run",
        "AMD Ryzen 5 5600G": "sysbench --test=cpu --num-threads=4 run"
    }
    
    # Get system info
    system_info = get_system_info()
    print("System Information:")
    print(system_info)

    # Dictionary to hold benchmark results
    benchmark_results = {}

    # Run benchmarks
    for setup, command in commands.items():
        print(f"\nRunning benchmark for {setup}...")
        start_time = time.time()
        output = run_benchmark(command)
        end_time = time.time()
        
        if output:
            benchmark_results[setup] = {
                "output": output,
                "duration": end_time - start_time
            }
            print(f"Benchmark completed for {setup} in {benchmark_results[setup]['duration']:.2f} seconds.")
        else:
            benchmark_results[setup] = {
                "output": "Benchmark failed.",
                "duration": None
            }

    # Print benchmark results
    print("\nBenchmark Results:")
    for setup, result in benchmark_results.items():
        print(f"{setup}: {result['output']} (Duration: {result['duration']})")

if __name__ == "__main__":
    main()
```

Ensure you have `sysbench` installed on your system, as this code uses it to benchmark CPU performance. Modify the benchmark command according to your requirements if needed.
