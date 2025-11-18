"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fundacionbuenaventura.cl
Prompt: Generate a script for testing server compatibility with Linux hosting plans optimized for PHP applications in Chile.
Generated: DETERMINISTIC_4015cd919f18464d
Batch ID: 20250612_154331
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import platform
import requests

def check_linux_distribution():
    """
    Check if the server is running a Linux operating system and return the distribution details.
    """
    if platform.system() != "Linux":
        raise EnvironmentError("This script is designed to run only on Linux servers.")
    
    try:
        # Using os-release file to determine Linux distribution
        with open("/etc/os-release", "r") as f:
            lines = f.readlines()
            distro_info = {}
            for line in lines:
                key, value = line.strip().split("=")
                distro_info[key] = value.strip('"')
            return distro_info.get("NAME", "Unknown"), distro_info.get("VERSION", "Unknown")
    except Exception as e:
        raise EnvironmentError("Unable to determine Linux distribution.") from e

def check_php_installation():
    """
    Check if PHP is installed and return the PHP version.
    """
    try:
        # Run PHP version command
        result = subprocess.run(["php", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise EnvironmentError("PHP is not installed or not found in the system PATH.")
        
        # Extract the version from the command output
        php_version = result.stdout.split("\n")[0].split(" ")[1]
        return php_version
    except FileNotFoundError:
        raise EnvironmentError("PHP is not installed or not found in the system PATH.")
    except Exception as e:
        raise EnvironmentError("An error occurred while checking PHP installation.") from e

def check_internet_connectivity():
    """
    Check if the server has internet connectivity.
    """
    try:
        # Ping a known stable website
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code != 200:
            raise ConnectionError("Internet connectivity check failed.")
        return True
    except requests.ConnectionError:
        raise ConnectionError("Server does not have internet connectivity.")
    except requests.Timeout:
        raise ConnectionError("Internet connectivity check timed out.")
    except Exception as e:
        raise ConnectionError("An error occurred while checking internet connectivity.") from e

def main():
    """
    Main function to test server compatibility for Linux hosting plans optimized for PHP applications.
    """
    try:
        # Check Linux distribution
        distro_name, distro_version = check_linux_distribution()
        print(f"Linux Distribution: {distro_name} {distro_version}")

        # Check PHP installation
        php_version = check_php_installation()
        print(f"PHP Version: {php_version}")

        # Check internet connectivity
        if check_internet_connectivity():
            print("Internet connectivity: OK")
        
        print("Server is compatible with Linux hosting plans optimized for PHP applications in Chile.")
    
    except EnvironmentError as env_err:
        print(f"Environment Error: {env_err}")
    
    except ConnectionError as conn_err:
        print(f"Connection Error: {conn_err}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
