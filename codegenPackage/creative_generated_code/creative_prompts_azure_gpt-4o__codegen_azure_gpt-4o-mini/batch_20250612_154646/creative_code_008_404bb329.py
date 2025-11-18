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
import os

class CompatibilityTester:
    def __init__(self):
        self.results = {
            'python_version': None,
            'node_version': None,
            'python_packages': [],
            'node_packages': []
        }

    def test_python_compatibility(self):
        """Tests Python version and installed packages."""
        try:
            # Get the Python version
            self.results['python_version'] = sys.version
            
            # Check for installed packages
            installed_packages = subprocess.run(
                [sys.executable, '-m', 'pip', 'list'],
                capture_output=True,
                text=True,
                check=True
            )
            self.results['python_packages'] = installed_packages.stdout.strip().split('\n')[2:]  # Skip header lines
            
        except subprocess.CalledProcessError as e:
            print("Error occurred while checking Python compatibility:", e)
            self.results['python_version'] = 'Error'
            self.results['python_packages'] = []

    def test_node_compatibility(self):
        """Tests Node.js version and installed packages."""
        try:
            # Get the Node.js version
            node_version = subprocess.run(
                ['node', '-v'],
                capture_output=True,
                text=True,
                check=True
            )
            self.results['node_version'] = node_version.stdout.strip()

            # Check for installed packages using npm
            npm_packages = subprocess.run(
                ['npm', 'list', '--depth=0'],
                capture_output=True,
                text=True,
                check=True
            )
            self.results['node_packages'] = npm_packages.stdout.strip().split('\n')[1:]  # Skip the first line

        except subprocess.CalledProcessError as e:
            print("Error occurred while checking Node.js compatibility:", e)
            self.results['node_version'] = 'Error'
            self.results['node_packages'] = []

    def print_results(self):
        """Prints the compatibility test results."""
        print("Compatibility Test Results:")
        print(f"Python Version: {self.results['python_version']}")
        print("Installed Python Packages:")
        for package in self.results['python_packages']:
            print(f"  - {package}")
        print(f"Node.js Version: {self.results['node_version']}")
        print("Installed Node Packages:")
        for package in self.results['node_packages']:
            print(f"  - {package}")

    def run_tests(self):
        """Runs all compatibility tests."""
        self.test_python_compatibility()
        self.test_node_compatibility()
        self.print_results()

if __name__ == "__main__":
    tester = CompatibilityTester()
    tester.run_tests()
```
