"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiodigital.live
Prompt: Recommend libraries or APIs to integrate the "Windows 7_10,11 Software" tools into a system optimization application.
Generated: DETERMINISTIC_3c0b05a232b65484
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import os
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SystemOptimization:
    """
    A class to handle system optimization tasks and integrate with various tools available for Windows 7, 10, and 11.
    
    Attributes:
        tools (list): List of available tools for system optimization.
    """

    def __init__(self):
        """
        Initializes the SystemOptimization class with a predefined list of tools.
        """
        self.tools = [
            'CCleaner',     # Popular tool for cleaning up junk files
            'Defraggler',   # Tool for disk defragmentation
            'Windows Disk Cleanup',  # Built-in Windows cleanup utility
            'Advanced SystemCare',  # Comprehensive system optimization tool
            'Glary Utilities'  # Multi-functional tool for system optimization
        ]

    def check_tool_installed(self, tool_name):
        """
        Check if a specified optimization tool is installed on the system.

        Args:
            tool_name (str): The name of the tool to check for installation.

        Returns:
            bool: True if the tool is installed, False otherwise.
        """
        try:
            output = subprocess.check_output(['where', tool_name], stderr=subprocess.STDOUT)
            return bool(output)
        except subprocess.CalledProcessError:
            return False

    def list_available_tools(self):
        """
        Lists all available optimization tools and checks if they are installed.

        Returns:
            dict: A dictionary with tool names as keys and their installation status as values.
        """
        availability = {}
        for tool in self.tools:
            availability[tool] = self.check_tool_installed(tool)
        return availability

    def run_tool(self, tool_name):
        """
        Executes the specified optimization tool if it is installed.

        Args:
            tool_name (str): The name of the tool to run.

        Raises:
            RuntimeError: If the tool is not installed or cannot be executed.
        """
        if not self.check_tool_installed(tool_name):
            logging.error(f"{tool_name} is not installed on this system.")
            raise RuntimeError(f"{tool_name} is not installed.")
        
        try:
            logging.info(f"Running {tool_name}...")
            subprocess.run([tool_name], check=True)
            logging.info(f"{tool_name} executed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error occurred while running {tool_name}: {e}")
            raise RuntimeError(f"Failed to execute {tool_name}.") from e

if __name__ == "__main__":
    optimizer = SystemOptimization()

    # List and log available tools
    available_tools = optimizer.list_available_tools()
    logging.info("Available Optimization Tools:")
    for tool, is_installed in available_tools.items():
        logging.info(f"{tool}: {'Installed' if is_installed else 'Not Installed'}")

    # Example to run a tool (uncomment to use)
    # try:
    #     optimizer.run_tool('CCleaner')
    # except RuntimeError as e:
    #     logging.error(e)
```
