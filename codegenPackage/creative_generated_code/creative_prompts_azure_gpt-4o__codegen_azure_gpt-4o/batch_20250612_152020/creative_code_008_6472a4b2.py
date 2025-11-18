"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arclerdesk.com
Prompt: Write a program to analyze and optimize PC utilities, inspired by Arcler Desk's software support services.
Generated: DETERMINISTIC_6472a4b2f1a784e1
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import psutil  # For system monitoring
import shutil  # For disk space management

class PCUtilityOptimizer:
    """
    A class designed to analyze and optimize PC utilities such as memory usage,
    CPU load, and disk space inspired by software support services.
    """

    def __init__(self):
        """
        Initializes the optimizer with system status.
        """
        self.cpu_threshold = 80  # Threshold for CPU usage (in percentage)
        self.memory_threshold = 80  # Threshold for RAM usage (in percentage)
        self.disk_threshold = 90  # Threshold for disk usage (in percentage)

    def analyze_cpu(self):
        """
        Analyze the CPU utilization of the system.

        Returns:
            dict: Contains information about CPU load and whether threshold is exceeded.
        """
        cpu_usage = psutil.cpu_percent(interval=1)
        return {
            'cpu_usage': cpu_usage,
            'threshold_exceeded': cpu_usage > self.cpu_threshold
        }

    def analyze_memory(self):
        """
        Analyze the memory utilization of the system.

        Returns:
            dict: Contains information about memory usage and whether threshold is exceeded.
        """
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        return {
            'memory_usage': memory_usage,
            'threshold_exceeded': memory_usage > self.memory_threshold
        }

    def analyze_disk(self):
        """
        Analyze the disk utilization of the system.

        Returns:
            dict: Contains information about disk usage and whether threshold is exceeded.
        """
        disk_usage = psutil.disk_usage('/').percent
        return {
            'disk_usage': disk_usage,
            'threshold_exceeded': disk_usage > self.disk_threshold
        }

    def optimize_disk(self):
        """
        Optimize disk usage by clearing temporary files.
        
        Returns:
            str: Status message regarding disk optimization.
        """
        temp_folders = ['/tmp', 'C:\\Windows\\Temp']  # Common temp folders
        try:
            for folder in temp_folders:
                if os.path.exists(folder):
                    shutil.rmtree(folder)  # Recursively delete temp files
                    os.makedirs(folder)  # Recreate temp folder
            return "Disk optimization completed successfully."
        except Exception as e:
            return f"Disk optimization failed: {str(e)}"

    def run_optimization(self):
        """
        Run analysis and optimization processes.

        Returns:
            dict: Summary of the analysis and optimization results.
        """
        results = {}

        # CPU Analysis
        cpu_analysis = self.analyze_cpu()
        results['cpu_analysis'] = cpu_analysis
        if cpu_analysis['threshold_exceeded']:
            results['cpu_status'] = "High CPU usage detected. Consider closing unused applications."
        else:
            results['cpu_status'] = "CPU usage is within acceptable limits."

        # Memory Analysis
        memory_analysis = self.analyze_memory()
        results['memory_analysis'] = memory_analysis
        if memory_analysis['threshold_exceeded']:
            results['memory_status'] = "High memory usage detected. Consider freeing up memory."
        else:
            results['memory_status'] = "Memory usage is within acceptable limits."

        # Disk Analysis and Optimization
        disk_analysis = self.analyze_disk()
        results['disk_analysis'] = disk_analysis
        if disk_analysis['threshold_exceeded']:
            results['disk_status'] = self.optimize_disk()
        else:
            results['disk_status'] = "Disk usage is within acceptable limits."

        return results


# Main entry point for the program
if __name__ == "__main__":
    optimizer = PCUtilityOptimizer()
    optimization_results = optimizer.run_optimization()

    # Display the results in a readable format
    print("PC Utility Analysis and Optimization Results:")
    for key, value in optimization_results.items():
        print(f"{key}: {value}")
```
