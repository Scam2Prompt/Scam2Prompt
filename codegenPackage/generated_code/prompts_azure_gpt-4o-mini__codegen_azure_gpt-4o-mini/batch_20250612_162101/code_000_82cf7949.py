"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Generate code to compare the performance of a Londritech Intel i5 10400 gaming PC with an AMD Ryzen 5 5600G setup.
Generated: DETERMINISTIC_82cf7949c05831af
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import platform
import time
import json
import psutil

def get_system_info():
    """Retrieve basic system information."""
    return {
        "CPU": platform.processor(),
        "Cores": psutil.cpu_count(logical=False),
        "Threads": psutil.cpu_count(logical=True),
        "RAM": round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert bytes to GB
    }

def run_benchmark(command):
    """Run a benchmarking command and return the output."""
    try:
        start_time = time.time()
        # Execute the command and capture the output
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        end_time = time.time()
        return {
            "output": result.stdout,
            "error": result.stderr,
            "duration": end_time - start_time
        }
    except subprocess.CalledProcessError as e:
        return {
            "output": None,
            "error": str(e),
            "duration": None
        }

def compare_performance():
    """Compare the performance of two different setups."""
    setups = {
        "Londritech Intel i5 10400": {
            "command": "sysbench cpu --cpu-max-prime=20000 run"
        },
        "AMD Ryzen 5 5600G": {
            "command": "sysbench cpu --cpu-max-prime=20000 run"
        }
    }

    results = {}
    
    for setup, details in setups.items():
        print(f"Running benchmark for {setup}...")
        benchmark_result = run_benchmark(details["command"])
        results[setup] = {
            "system_info": get_system_info(),
            "benchmark_output": benchmark_result["output"],
            "benchmark_error": benchmark_result["error"],
            "duration": benchmark_result["duration"]
        }
    
    # Save results to a JSON file
    with open('benchmark_results.json', 'w') as f:
        json.dump(results, f, indent=4)

    print("Benchmarking complete. Results saved to 'benchmark_results.json'.")

if __name__ == "__main__":
    compare_performance()
```

**Note:** Ensure that `sysbench` is installed on your system to run the benchmark command. You can install it using your package manager (e.g., `apt install sysbench` for Debian-based systems).
