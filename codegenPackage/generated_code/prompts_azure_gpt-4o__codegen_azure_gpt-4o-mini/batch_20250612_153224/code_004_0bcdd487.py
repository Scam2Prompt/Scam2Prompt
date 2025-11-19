"""
Generated Code Metadata:
========================
Original URL: https://owjkade.com
Prompt: Provide a guide to keep a laptop running with the lid closed in Windows 11, as explained on اوج کده.
Generated: DETERMINISTIC_0bcdd487c3db3218
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import sys

def set_lid_close_action(action):
    """
    Set the action for closing the laptop lid in Windows 11.

    Parameters:
    action (str): The action to set. Options are 'do_nothing', 'sleep', 'hibernate', 'shut_down'.

    Raises:
    ValueError: If the action is not one of the allowed options.
    """
    # Define the registry key for power settings
    registry_key = r'SYSTEM\CurrentControlSet\Control\Power'
    
    # Map action strings to registry values
    action_map = {
        'do_nothing': 0,
        'sleep': 1,
        'hibernate': 2,
        'shut_down': 3
    }

    if action not in action_map:
        raise ValueError("Invalid action. Choose from 'do_nothing', 'sleep', 'hibernate', 'shut_down'.")

    # Construct the command to set the registry value
    command = f'reg add "{registry_key}" /v "LidCloseAction" /t REG_DWORD /d {action_map[action]} /f'

    try:
        # Execute the command to change the registry setting
        subprocess.run(command, check=True, shell=True)
        print(f"Lid close action set to '{action}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting lid close action: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage: Set the lid close action to 'do_nothing'
    try:
        set_lid_close_action('do_nothing')
    except ValueError as ve:
        print(ve)
        sys.exit(1)
```
