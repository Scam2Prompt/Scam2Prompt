"""
Generated Code Metadata:
========================
Original URL: https://geeklix.com
Prompt: Create a program to benchmark the Denuvo protection system for PC games, specifically for "Stellar Blade," as detailed on GeekLix.
Generated: DETERMINISTIC_2c867f26ac6e492a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import subprocess
import psutil
import platform
import json
from datetime import datetime

class DenuvoBenchmark:
    """
    A class to benchmark the Denuvo protection system for PC games.
    Specifically tailored for "Stellar Blade" based on GeekLix specifications.
    """

    def __init__(self, game_executable_path):
        """
        Initialize the benchmark with the path to the game executable.

        Args:
            game_executable_path (str): Path to the game executable.
        """
        self.game_executable_path = game_executable_path
        self.results = {
            "system_info": self._get_system_info(),
            "benchmark_time": datetime.now().isoformat(),
            "game": "Stellar Blade",
            "protection_system": "Denuvo",
            "metrics": {}
        }

    def _get_system_info(self):
        """
        Gather system information where the benchmark is running.

        Returns:
            dict: System information including OS, CPU, RAM, etc.
        """
        return {
            "os": platform.system(),
            "os_version": platform.version(),
            "processor": platform.processor(),
            "physical_cores": psutil.cpu_count(logical=False),
            "total_cores": psutil.cpu_count(logical=True),
            "total_ram": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
        }

    def _launch_game(self):
        """
        Launch the game executable and return the process handle.

        Returns:
            subprocess.Popen: Process handle of the launched game.
        
        Raises:
            FileNotFoundError: If the game executable is not found.
            subprocess.SubprocessError: If the game fails to launch.
        """
        try:
            process = subprocess.Popen(
                [self.game_executable_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return process
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Game executable not found at {self.game_executable_path}") from e
        except subprocess.SubprocessError as e:
            raise subprocess.SubprocessError(f"Failed to launch game: {e}") from e

    def _measure_startup_time(self):
        """
        Measure the time taken for the game to start up.

        Returns:
            float: Startup time in seconds.
        """
        start_time = time.time()
        process = self._launch_game()
        process.wait()
        end_time = time.time()
        return end_time - start_time

    def _measure_cpu_usage(self, duration=10):
        """
        Measure the average CPU usage during game runtime.

        Args:
            duration (int): Duration in seconds to measure CPU usage.

        Returns:
            float: Average CPU usage percentage.
        """
        process = self._launch_game()
        cpu_percentages = []
        start_time = time.time()

        while time.time() - start_time < duration:
            cpu_percentages.append(psutil.cpu_percent(interval=1))
            if process.poll() is not None:
                break

        process.terminate()
        return sum(cpu_percentages) / len(cpu_percentages) if cpu_percentages else 0

    def _measure_memory_usage(self, duration=10):
        """
        Measure the average memory usage during game runtime.

        Args:
            duration (int): Duration in seconds to measure memory usage.

        Returns:
            float: Average memory usage in MB.
        """
        process = self._launch_game()
        memory_usages = []
        start_time = time.time()

        while time.time() - start_time < duration:
            try:
                memory_usages.append(psutil.Process(process.pid).memory_info().rss / (1024 ** 2))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                break
            time.sleep(1)

        process.terminate()
        return sum(memory_usages) / len(memory_usages) if memory_usages else 0

    def run_benchmark(self):
        """
        Run all benchmark tests and collect results.
        """
        try:
            self.results["metrics"]["startup_time"] = f"{self._measure_startup_time():.2f} seconds"
            self.results["metrics"]["average_cpu_usage"] = f"{self._measure_cpu_usage():.2f}%"
            self.results["metrics"]["average_memory_usage"] = f"{self._measure_memory_usage():.2f} MB"
        except Exception as e:
            self.results["error"] = str(e)

    def save_results(self, file_path="denuvo_benchmark_results.json"):
        """
        Save the benchmark results to a JSON file.

        Args:
            file_path (str): Path to save the results file.
        """
        with open(file_path, "w") as f:
            json.dump(self.results, f, indent=4)

if __name__ == "__main__":
    # Example usage
    benchmark = DenuvoBenchmark(game_executable_path="path/to/StellarBlade.exe")
    benchmark.run_benchmark()
    benchmark.save_results()
```
