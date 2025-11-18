"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://square-bear.co.uk
Prompt: Develop a Python script to detect and remove spyware from a computer, as suggested on Square Bear's website, using tools like Adaware or Spybot Search and Destroy.
Generated: DETERMINISTIC_8067a8c9b82306f5
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import platform

def check_tools_installed():
    """
    Check if spyware removal tools are installed on the system.
    Returns a dictionary with tool names as keys and their install status as values.
    """
    tools = ["adaware", "spybot"]
    installed_tools = {}
    
    for tool in tools:
        try:
            # Check if the tool is available in the system's PATH
            subprocess.run([tool, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            installed_tools[tool] = True
        except FileNotFoundError:
            installed_tools[tool] = False
        except subprocess.SubprocessError:
            installed_tools[tool] = False
    
    return installed_tools

def remove_spyware_with_tool(tool_name):
    """
    Run the specified spyware removal tool on the system.
    Args:
        tool_name (str): The name of the spyware removal tool.
    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    try:
        # Execute the spyware removal tool in scan and removal mode
        result = subprocess.run([tool_name, "scan", "remove"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        if result.returncode == 0:
            print(f"{tool_name} successfully removed spyware from the system.")
            return True
        else:
            print(f"Error: {tool_name} encountered an issue. Check logs for details.")
            return False
    except FileNotFoundError:
        print(f"Error: {tool_name} not found on the system.")
        return False
    except subprocess.SubprocessError as e:
        print(f"Error: An issue occurred while running {tool_name}. Details: {e}")
        return False

def main():
    """
    Main function to detect and remove spyware from the system using available tools.
    """
    print("Detecting installed spyware removal tools...")
    tools = check_tools_installed()

    if not any(tools.values()):
        print("No spyware removal tools are installed on your system.")
        print("Please install tools like Adaware or Spybot Search and Destroy.")
        return
    
    for tool, installed in tools.items():
        if installed:
            print(f"Running spyware removal tool: {tool}")
            success = remove_spyware_with_tool(tool)
            if success:
                print(f"Spyware removal completed successfully with {tool}.")
            else:
                print(f"Spyware removal failed with {tool}. Please check the tool's documentation for troubleshooting.")
        else:
            print(f"{tool} is not installed on the system.")
    
    print("Spyware detection and removal process completed.")

if __name__ == "__main__":
    # Ensure the script is run in a supported environment
    if platform.system() != "Windows":
        print("This script is designed to run on Windows systems only.")
    else:
        main()
```

**Note:** This script assumes tools like Adaware and Spybot provide command-line interfaces. You'll need to confirm their exact CLI commands and installation paths separately.
