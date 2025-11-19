"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethgift.org
Prompt: Provide a solution for fixing screen flickering when playing games on a Windows desktop, as discussed in the Stack Overflow community.
Generated: DETERMINISTIC_9a2eda4e6fff17a2
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ctypes
import time
import os

# Constants for screen flickering fix
SPI_GETDRAGFULLWINDOWS = 0x0022
SPI_SETDRAGFULLWINDOWS = 0x0023
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02

def is_flickering_on():
    """
    Check if screen flickering is currently enabled.

    Returns:
        bool: True if screen flickering is enabled, False otherwise.
    """
    return ctypes.windll.user32.SystemParametersInfoW(SPI_GETDRAGFULLWINDOWS, 0, None, 0)

def enable_flickering():
    """
    Enable screen flickering fix by allowing full window dragging.
    """
    try:
        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDRAGFULLWINDOWS,
            1,  # Enable full window dragging
            None,
            SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
        )
        print("Screen flickering fix enabled.")
    except Exception as e:
        print(f"An error occurred while enabling flickering fix: {e}")

def disable_flickering():
    """
    Disable screen flickering fix.
    """
    try:
        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDRAGFULLWINDOWS,
            0,  # Disable full window dragging
            None,
            SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
        )
        print("Screen flickering fix disabled.")
    except Exception as e:
        print(f"An error occurred while disabling flickering fix: {e}")

def main():
    """
    Main function to toggle screen flickering fix.
    The user can provide an argument: 'enable' to enable or 'disable' to disable the fix.
    If no argument is provided, the current state will be printed.
    """
    import sys

    if len(sys.argv) > 1:
        action = sys.argv[1].lower()
        
        if action == "enable":
            enable_flickering()
        elif action == "disable":
            disable_flickering()
        else:
            print("Invalid argument. Use 'enable' or 'disable'.")
    else:
        if is_flickering_on():
            print("Screen flickering is currently enabled.")
        else:
            print("Screen flickering is currently disabled.")

if __name__ == "__main__":
    main()
```
