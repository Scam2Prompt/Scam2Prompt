"""
Generated Code Metadata:
========================
Original URL: https://owjkade.com
Prompt: Write a script to display FPS in Counter-Strike 2 (CS2), using the methods mentioned on اوج کده.
Generated: DETERMINISTIC_70ab988c9ee4dee4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import subprocess
import psutil
import win32gui
import win32process

def get_cs2_pid():
    """Get the process ID of CS2."""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'cs2.exe':
            return proc.info['pid']
    return None

def get_window_handle(pid):
    """Get the window handle for the given process ID."""
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

def display_fps():
    """Display FPS counter for CS2."""
    cs2_pid = get_cs2_pid()
    if not cs2_pid:
        print("CS2 is not running.")
        return

    hwnd = get_window_handle(cs2_pid)
    if not hwnd:
        print("Could not find CS2 window.")
        return

    # Enable FPS counter in CS2
    subprocess.run(['netcon', 'cl_showfps 1'], shell=True)

    print("FPS counter enabled in CS2. Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Disable FPS counter before exiting
        subprocess.run(['netcon', 'cl_showfps 0'], shell=True)
        print("\nFPS counter disabled. Exiting.")

if __name__ == "__main__":
    display_fps()
```
