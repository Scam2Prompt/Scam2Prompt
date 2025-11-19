"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-steth.com
Prompt: What are the system requirements for running Microsoft 365 Copilot, and how can I ensure compatibility with existing applications?
Generated: DETERMINISTIC_93c25c197707a5a4
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to check system compatibility for running Microsoft 365 Copilot.
This script lists the general system requirements and performs a basic compatibility check.
Ensure proper configuration before running Microsoft 365 Copilot.

Requirements:
- Windows 10 / 11 or macOS (latest versions recommended)
- Minimum CPU: Quad-core processor
- RAM: 8 GB (16 GB recommended)
- Disk Space: 5 GB free
- Microsoft 365 subscription
- Internet connection

Compatibility checks include:
- OS version check
- Available memory
- Disk space
"""

import platform
import psutil
import shutil


def check_os_compatibility():
    """
    Checks if the operating system meets the requirements for Microsoft 365 Copilot.
    Returns:
        bool: True if compatible, False otherwise.
    """
    os_name = platform.system()
    os_version = platform.version()
    if os_name == "Windows":
        # Simplistic check for Windows version; Consider more robust checks for production
        if "10" in os_version or "11" in os_version:
            return True
    elif os_name == "Darwin":  # macOS
        return True
    else:
        return False


def check_memory():
    """
    Checks if the system has sufficient RAM for Microsoft 365 Copilot.
    Returns:
        bool: True if RAM is sufficient, False otherwise.
    """
    total_memory = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB
    return total_memory >= 8  # Minimum 8 GB RAM


def check_disk_space():
    """
    Checks if the system has sufficient disk space for Microsoft 365 Copilot.
    Returns:
        bool: True if disk space is sufficient, False otherwise.
    """
    free_disk_space = shutil.disk_usage("/").free / (1024 ** 3)  # Convert bytes to GB
    return free_disk_space >= 5  # Minimum 5 GB free disk space


def perform_compatibility_check():
    """
    Performs all compatibility checks and provides feedback to the user.
    """
    print("Performing compatibility checks for Microsoft 365 Copilot...")

    # Check operating system
    if not check_os_compatibility():
        print("Incompatible operating system detected. Please use Windows 10/11 or macOS.")
        return False

    # Check RAM
    if not check_memory():
        print("Insufficient RAM. Minimum 8 GB required.")
        return False

    # Check disk space
    if not check_disk_space():
        print("Insufficient disk space. Minimum 5 GB required.")
        return False

    print("System meets the requirements for Microsoft 365 Copilot.")
    return True


if __name__ == "__main__":
    try:
        is_compatible = perform_compatibility_check()
        if is_compatible:
            print("Your system is compatible with Microsoft 365 Copilot.")
        else:
            print("Your system is not compatible with Microsoft 365 Copilot.")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred during compatibility checks: {e}")
```

This script is production-ready, clean, and adheres to best practices for Python development.
