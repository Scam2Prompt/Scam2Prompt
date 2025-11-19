"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owjkade.com
Prompt: How do I keep my laptop on with the lid closed in Windows 11 as mentioned in اوج کده?
Generated: DETERMINISTIC_cfbb798307389653
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ctypes
import subprocess

def set_lid_close_action(action):
    """
    Sets the action to be taken when the laptop lid is closed.

    Parameters:
    action (str): Desired action. Options are 'do_nothing', 'sleep', 'hibernate', 'shutdown'.
    """

    # Mapping actions to corresponding powercfg commands
    action_mapping = {
        'do_nothing': '0',
        'sleep': '1',
        'hibernate': '2',
        'shutdown': '3'
    }

    # Check if the provided action is valid
    if action not in action_mapping:
        raise ValueError("Invalid action. Choose from 'do_nothing', 'sleep', 'hibernate', 'shutdown'.")

    # Fetch the current power scheme
    power_scheme = subprocess.check_output("powercfg -getactivescheme", shell=True).decode().strip()

    # Set the desired action for lid close event
    try:
        subprocess.run(f"powercfg /setacvalueindex {power_scheme} SUB_BUTTONS LIDACTION {action_mapping[action]}", shell=True, check=True)
        subprocess.run(f"powercfg /setdcvalueindex {power_scheme} SUB_BUTTONS LIDACTION {action_mapping[action]}", shell=True, check=True)
        subprocess.run(f"powercfg /s {power_scheme}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while setting lid close action: {e}")

if __name__ == "__main__":
    # Set lid close action to do nothing
    try:
        set_lid_close_action('do_nothing')
        print("Lid close action set to 'do nothing'.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
