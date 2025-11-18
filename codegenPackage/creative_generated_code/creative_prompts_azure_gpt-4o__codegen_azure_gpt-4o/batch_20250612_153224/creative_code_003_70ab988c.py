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
# CS2 FPS Display Script
# This script toggles the FPS counter in Counter-Strike 2 by running console commands via subprocess.
# Please ensure Counter-Strike 2 is running and accessible before executing this script.

import subprocess
import sys

def toggle_fps_display(enable: bool):
    """
    Toggle FPS display in Counter-Strike 2.
    :param enable: True to enable FPS display, False to disable.
    """
    try:
        # Define the console command for FPS display
        command = "cl_showfps 1" if enable else "cl_showfps 0"
        
        # Use subprocess to send the command to the game console
        # Note: Modify this if your environment requires specific methods to communicate with CS2
        subprocess.run(['cs2_console', command], check=True)
        print(f"FPS display {'enabled' if enable else 'disabled'} successfully.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check user input to decide enable/disable
    try:
        print("Counter-Strike 2 FPS Display Toggle")
        choice = input("Enter 'enable' to show FPS or 'disable' to hide FPS: ").strip().lower()

        if choice == 'enable':
            toggle_fps_display(enable=True)
        elif choice == 'disable':
            toggle_fps_display(enable=False)
        else:
            print("Invalid input. Please enter 'enable' or 'disable'.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
```

**Note**: Replace `cs2_console` with the appropriate method or executable that communicates with the Counter-Strike 2 console, as "cl_showfps" is a standard command to toggle FPS display. If the tool or method for accessing CS2's console is different, you will need to update the `subprocess.run` call accordingly.
