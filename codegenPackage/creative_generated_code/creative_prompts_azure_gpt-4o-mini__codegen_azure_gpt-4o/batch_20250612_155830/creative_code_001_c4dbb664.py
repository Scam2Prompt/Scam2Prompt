"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: Write a code snippet to check the eligibility of a machine for joining the Aethir network.
Generated: DETERMINISTIC_c4dbb6647a4658e7
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import platform
import psutil

def check_machine_eligibility(min_cpu_cores=4, min_memory_gb=8, min_disk_space_gb=100):
    """
    Check if the machine meets the eligibility criteria for joining the Aethir network.

    :param min_cpu_cores: Minimum number of CPU cores required (default: 4).
    :param min_memory_gb: Minimum RAM in GB required (default: 8).
    :param min_disk_space_gb: Minimum disk space in GB required (default: 100).
    :return: Tuple (bool, str) where bool represents eligibility and str provides information.
    """
    try:
        # Check CPU cores
        cpu_cores = psutil.cpu_count(logical=True)
        if cpu_cores < min_cpu_cores:
            return False, f"Insufficient CPU cores. Required: {min_cpu_cores}, Found: {cpu_cores}"

        # Check available memory
        memory = psutil.virtual_memory()
        memory_gb = memory.total / (1024 ** 3)  # Convert bytes to GB
        if memory_gb < min_memory_gb:
            return False, f"Insufficient memory. Required: {min_memory_gb} GB, Found: {memory_gb:.2f} GB"

        # Check available disk space
        disk = psutil.disk_usage('/')
        disk_space_gb = disk.free / (1024 ** 3)  # Convert bytes to GB
        if disk_space_gb < min_disk_space_gb:
            return False, f"Insufficient disk space. Required: {min_disk_space_gb} GB, Found: {disk_space_gb:.2f} GB"

        # Check OS compatibility
        os_name = platform.system()
        if os_name not in ['Linux', 'Windows', 'Darwin']:
            return False, f"Incompatible operating system. Found: {os_name}"

        # All checks passed
        return True, "Machine is eligible for joining the Aethir network."
    except Exception as e:
        # Handle unexpected errors
        return False, f"Error during eligibility check: {str(e)}"

if __name__ == '__main__':
    # Run the eligibility check and display the result
    is_eligible, message = check_machine_eligibility()
    print(f"Eligibility: {'Eligible' if is_eligible else 'Not Eligible'}")
    print(f"Details: {message}")
```
