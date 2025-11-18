"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap-lottery.rf.gd
Prompt: Develop a Python script to test the compatibility of different Python versions on a hosting service that supports multiple versions of Python.
Generated: DETERMINISTIC_a060dbc5ac6df067
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys
import os
from typing import List, Dict

# Function to check if a specific Python version is installed and return its version string
def check_python_version(version: str) -> str:
    """
    Checks whether the specified Python version is installed on the system.

    Args:
        version (str): The version of Python to check (e.g., '3.8', '3.9').

    Returns:
        str: The version string if the specified version is found, else None.
    """
    try:
        # Using subprocess to call the Python executable
        result = subprocess.run(
            [f'python{version}', '--version'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        # Handle the error case if the Python version is not found
        print(f"Python {version} not found. Error: {e.stderr.strip()}")
        return None

# Function to test compatibility of the specified Python versions
def test_python_versions(versions: List[str]) -> Dict[str, str]:
    """
    Tests compatibility of the given list of Python versions.

    Args:
        versions (List[str]): A list of Python version strings to test.

    Returns:
        Dict[str, str]: A dictionary with version strings as keys and their compatibility status as values.
    """
    compatibility_results = {}
    
    for version in versions:
        version_string = check_python_version(version)
        if version_string:
            compatibility_results[version] = f"Compatible: {version_string}"
        else:
            compatibility_results[version] = "Not Installed"

    return compatibility_results

# Main function to execute the script
def main():
    """
    Main entry point for the script. Sets the Python versions to test and calls the compatibility function.
    """
    # List of Python versions to check for compatibility
    python_versions_to_test = ['3.6', '3.7', '3.8', '3.9', '3.10', '3.11']

    # Testing compatibility
    results = test_python_versions(python_versions_to_test)

    # Displaying results
    print("Python Compatibility Test Results:")
    for version, result in results.items():
        print(f"{version}: {result}")

if __name__ == "__main__":
    main()
```
