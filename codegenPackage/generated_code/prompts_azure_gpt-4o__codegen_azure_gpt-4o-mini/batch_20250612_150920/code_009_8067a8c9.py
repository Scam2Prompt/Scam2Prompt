"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Develop a Python script to detect and remove spyware from a computer, as suggested on Square Bear's website, using tools like Adaware or Spybot Search and Destroy.
Generated: DETERMINISTIC_8067a8c9b82306f5
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_tool_installed(tool_name):
    """Check if a tool is installed on the system."""
    try:
        subprocess.run([tool_name, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def run_tool(tool_name):
    """Run the spyware removal tool."""
    try:
        logging.info(f"Running {tool_name} for spyware detection and removal.")
        result = subprocess.run([tool_name, '/scan'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running {tool_name}: {e.stderr.decode()}")
        sys.exit(1)

def main():
    """Main function to detect and remove spyware."""
    # List of tools to check
    tools = ['Adaware', 'SpybotSD']

    # Check for installed tools and run them
    for tool in tools:
        if check_tool_installed(tool):
            run_tool(tool)
        else:
            logging.warning(f"{tool} is not installed. Please install it to proceed.")

if __name__ == "__main__":
    main()
```

**Note:** This script assumes that the tools `Adaware` and `Spybot Search and Destroy` are installed and accessible via the command line. The actual command-line arguments for running these tools may vary; please refer to their documentation for the correct usage.
