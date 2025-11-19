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
import timeit
import platform
import psutil
import cpuinfo
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Any, List, Tuple

class SystemInfo:
    """Class to gather system information."""
    
    @staticmethod
    def get_system_info() -> Dict[str, Any]:
        """Collects and returns system information.
        
        Returns:
            Dict[str, Any]: Dictionary containing system information.
        """
        info = {
            "platform": platform.system(),
            "platform_version": platform.version(),
            "architecture": platform.machine(),
            "processor": cpuinfo.get_cpu_info()['brand_raw'],
            "physical_cores": psutil.cpu_count(logical=False),
            "total_cores": psutil.cpu_count(logical=True),
            "cpu_frequency": psutil.cpu_freq().current,
            "ram": round(psutil.virtual_memory().total / (1024.0 ** 3), 2)
        }
        return info

class Benchmark:
    """Class to perform CPU benchmarks."""
    
    @staticmethod
    def cpu_benchmark(iterations: int = 5) -> Dict[str, float]:
        """Performs CPU benchmarks and returns average times.
        
        Args:
            iterations (int): Number of iterations to run each benchmark.
            
        Returns:
            Dict[str, float]: Dictionary containing benchmark results.
        """
        def fibonacci(n: int) -> int:
            """Recursive Fibonacci function for CPU benchmark."""
            if n <= 1:
                return n
            return fibonacci(n-1) + fibonacci(n-2)
        
        def matrix_multiplication(size: int) -> List[List[float]]:
            """Matrix multiplication for CPU benchmark."""
            matrix = np.random.rand(size, size)
            return np.dot(matrix, matrix)
        
        benchmarks = {
            "fibonacci_35": timeit.timeit(lambda: fibonacci(35), number=iterations) / iterations,
            "matrix_128": timeit.timeit(lambda: matrix_multiplication(128), number=iterations) / iterations,
            "matrix_256": timeit.timeit(lambda: matrix_multiplication(256), number=iterations) / iterations
        }
        
        return benchmarks

class PerformanceComparator:
    """Class to compare performance between two systems."""
    
    @staticmethod
    def compare_systems(system1: Dict[str, Any], system2: Dict[str, Any]) -> None:
        """Compares two systems and prints the results.
        
        Args:
            system1 (Dict[str, Any]): First system's information and benchmarks.
            system2 (Dict[str, Any]): Second system's information and benchmarks.
        """
        print("\nSystem Comparison:")
        print("=" * 50)
        
        # Print system information
        print("\nSystem 1 Information:")
        for key, value in system1["info"].items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("\nSystem 2 Information:")
        for key, value in system2["info"].items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        # Print benchmark results
        print("\nBenchmark Results (Lower is better):")
        print("-" * 50)
        for benchmark in system1["benchmarks"]:
            sys1_time = system1["benchmarks"][benchmark]
            sys2_time = system2["benchmarks"][benchmark]
            faster = "System 1" if sys1_time < sys2_time else "System 2"
            improvement = abs(sys1_time - sys2_time) / min(sys1_time, sys2_time) * 100
            
            print(f"{benchmark}:")
            print(f"  System 1: {sys1_time:.4f}s | System 2: {sys2_time:.4f}s")
            print(f"  {faster} is {improvement:.2f}% faster\n")
    
    @staticmethod
    def plot_results(system1: Dict[str, Any], system2: Dict[str, Any]) -> None:
        """Plots benchmark results for visual comparison.
        
        Args:
            system1 (Dict[str, Any]): First system's benchmarks.
            system2 (Dict[str, Any]): Second system's benchmarks.
        """
        labels = list(system1["benchmarks"].keys())
        sys1_times = [system1["benchmarks"][b] for b in labels]
        sys2_times = [system2["benchmarks"][b] for b in labels]
        
        x = np.arange(len(labels))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(10, 6))
        rects1 = ax.bar(x - width/2, sys1_times, width, label='System 1')
        rects2 = ax.bar(x + width/2, sys2_times, width, label='System 2')
        
        ax.set_ylabel('Time (seconds)')
        ax.set_title('Benchmark Comparison')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        
        fig.tight_layout()
        plt.show()

def main():
    """Main function to execute the performance comparison."""
    try:
        print("Gathering System 1 (Intel i5 10400) information...")
        system1 = {
            "info": {
                "platform": "Windows",
                "platform_version": "10",
                "architecture": "x86_64",
                "processor": "Intel Core i5-10400",
                "physical_cores": 6,
                "total_cores": 12,
                "cpu_frequency": 2900,
                "ram": 16.0
            },
            "benchmarks": Benchmark.cpu_benchmark()
        }
        
        print("\nGathering System 2 (AMD Ryzen 5 5600G) information...")
        system2 = {
            "info": {
                "platform": "Windows",
                "platform_version": "10",
                "architecture": "x86_64",
                "processor": "AMD Ryzen 5 5600G",
                "physical_cores": 6,
                "total_cores": 12,
                "cpu_frequency": 3900,
                "ram": 16.0
            },
            "benchmarks": Benchmark.cpu_benchmark()
        }
        
        PerformanceComparator.compare_systems(system1, system2)
        PerformanceComparator.plot_results(system1, system2)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
