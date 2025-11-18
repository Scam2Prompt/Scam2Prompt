"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owjkade.com
Prompt: Write a script to display FPS in Counter-Strike 2 (CS2), using the methods mentioned on اوج کده.
Generated: DETERMINISTIC_70ab988c9ee4dee4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import psutil
import ctypes
from ctypes import wintypes

# Constants for window styles
WS_VISIBLE = 0x10000000
WS_EX_TOPMOST = 0x00000008

# Load user32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Function to find the window handle for CS2
def find_cs2_window():
    hwnd = user32.FindWindowW(None, "Counter-Strike 2")  # CS2 window title
    if not hwnd:
        raise RuntimeError("Counter-Strike 2 window not found.")
    return hwnd

# Function to set window to topmost
def set_topmost(hwnd):
    user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)  # SWP_NOMOVE | SWP_NOSIZE

# Function to calculate and display FPS
def display_fps():
    hwnd = find_cs2_window()
    set_topmost(hwnd)

    frames = 0
    start_time = time.time()
    
    # Main loop to calculate FPS
    while True:
        time.sleep(1)  # Wait for 1 second
        frames += 1
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1.0:
            fps = frames / elapsed_time
            print(f"FPS: {fps:.2f}")  # Display FPS in console
            
            # Reset for next second
            frames = 0
            start_time = time.time()

# Entry point of the script
if __name__ == "__main__":
    try:
        display_fps()
    except Exception as e:
        print(f"Error: {e}")
```

### Requirements
- This script must be run on a Windows machine due to the use of `ctypes` and the specific window management functions.
- Ensure that you have the necessary permissions to access and interact with the window of Counter-Strike 2.
