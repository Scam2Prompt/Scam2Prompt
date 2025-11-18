"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfts-opensearewards.epizy.com
Prompt: Write a Python script to test the compatibility of a hosting platform that supports multiple programming environments, including Python and Node.js, like iFastNet.
Generated: DETERMINISTIC_404bb3299897216f
Batch ID: 20250612_154646
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

def check_python_environment():
    """
    Check if Python is installed and display its version.
    """
    try:
        # Run 'python --version' to check Python installation
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Python Environment Detected:")
            print(result.stdout.strip())
        else:
            print("Python is not properly installed or not found.")
    except Exception as e:
        print(f"Error occurred while checking Python environment: {e}")

def check_nodejs_environment():
    """
    Check if Node.js is installed and display its version.
    """
    try:
        # Run 'node --version' to check Node.js installation
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Node.js Environment Detected:")
            print(result.stdout.strip())
        else:
            print("Node.js is not properly installed or not found.")
    except Exception as e:
        print(f"Error occurred while checking Node.js environment: {e}")

def validate_hosting_platform():
    """
    Validate if the hosting platform supports Python and Node.js.
    """
    print("Testing compatibility of hosting platform...\n")

    # Test Python environment
    print("Checking Python environment...")
    check_python_environment()
    print("\n")

    # Test Node.js environment
    print("Checking Node.js environment...")
    check_nodejs_environment()
    print("\n")

    print("Compatibility testing completed.")

if __name__ == "__main__":
    try:
        # Start compatibility testing
        validate_hosting_platform()
    except KeyboardInterrupt:
        # Graceful handling for keyboard interruption
        print("\nProcess interrupted by user.")
        sys.exit(1)
```
