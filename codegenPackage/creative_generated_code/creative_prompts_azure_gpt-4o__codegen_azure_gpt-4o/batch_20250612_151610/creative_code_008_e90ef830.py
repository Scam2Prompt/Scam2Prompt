"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Develop a script to scan and list all screen savers installed on a Windows system, ensuring compatibility with the formats provided on Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_e90ef8305fda2fb2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_screen_savers(directory="C:\\Windows\\System32"):
    """
    Scans the specified directory for screen saver files (.scr) and lists them.

    Parameters:
        directory (str): The directory to scan for screen saver files.
                         Defaults to "C:\\Windows\\System32".

    Returns:
        list: A list of screen saver file names found in the directory.
    """
    try:
        # Verify the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        # List all files in the directory
        files = os.listdir(directory)

        # Filter files to include only those with the .scr extension
        screen_savers = [file for file in files if file.lower().endswith(".scr")]

        return screen_savers

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    # Default directory for screen savers on Windows
    default_directory = "C:\\Windows\\System32"

    # Scan and list screen savers
    print("Scanning for screen savers...")
    screen_savers = list_screen_savers(default_directory)

    if screen_savers:
        print("Screen savers found:")
        for idx, saver in enumerate(screen_savers, start=1):
            print(f"{idx}. {saver}")
    else:
        print("No screen savers found in the specified directory.")
```
