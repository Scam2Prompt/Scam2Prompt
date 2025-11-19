"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethgift.org
Prompt: What are the steps to set a default window size for Microsoft Word on Windows 10, based on user experiences shared on Super User?
Generated: DETERMINISTIC_c1721ac15069f801
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import winreg as reg
import os

def set_default_word_window_size(width=800, height=600):
    """
    Set the default window size for Microsoft Word on Windows 10.

    Parameters:
    - width (int): The desired default width of the Word window.
    - height (int): The desired default height of the Word window.
    """
    try:
        # Define the registry path for Microsoft Word settings
        word_registry_path = r"Software\Microsoft\Office\16.0\Word\Options"  # Adjust '16.0' based on your Office version

        # Open the registry key for Microsoft Word options
        with reg.OpenKey(reg.HKEY_CURRENT_USER, word_registry_path, 0, reg.KEY_ALL_ACCESS) as word_key:
            # Set window width and height
            reg.SetValueEx(word_key, "WindowWidth", 0, reg.REG_DWORD, width)
            reg.SetValueEx(word_key, "WindowHeight", 0, reg.REG_DWORD, height)
        
        print(f"Successfully set default Microsoft Word window size to {width}x{height}.")

    except FileNotFoundError:
        print("Error: Microsoft Word registry path not found. Ensure that Word is installed.")
    except PermissionError:
        print("Error: Permission denied. Run this script with administrator privileges.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Call the function to set the default window size
    set_default_word_window_size()
```
