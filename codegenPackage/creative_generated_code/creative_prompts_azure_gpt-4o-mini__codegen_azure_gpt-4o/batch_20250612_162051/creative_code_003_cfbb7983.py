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

This task involves changing the power settings on a Windows 11 system to keep the laptop on when the lid is closed. Since this cannot be achieved directly through programming, the following Python script uses the `subprocess` module to execute the necessary Windows commands (via `powercfg`) to change the lid close action settings. Note that administrative privileges are required to run this script.

```python
import subprocess
import sys

def set_lid_close_action():
    """
    Sets the laptop lid close action to 'Do Nothing' for both battery and plugged-in states.
    Requires administrative privileges to execute.
    """
    try:
        # Command to set lid close action to 'Do Nothing' on battery
        subprocess.run(
            ["powercfg", "/SETACVALUEINDEX", "SCHEME_CURRENT", "SUB_BUTTONS", "LIDCLOSE", "0"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Command to set lid close action to 'Do Nothing' when plugged in
        subprocess.run(
            ["powercfg", "/SETDCVALUEINDEX", "SCHEME_CURRENT", "SUB_BUTTONS", "LIDCLOSE", "0"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Apply the updated power configuration
        subprocess.run(
            ["powercfg", "/S", "SCHEME_CURRENT"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        print("Successfully updated lid close action to 'Do Nothing'.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to update lid close action.\n{e.stderr.decode()}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Changing laptop lid close action to 'Do Nothing'...")
    set_lid_close_action()
```

**Notes:**
1. To run this script, you need to execute it as an administrator.
2. Ensure Python is installed on your system.
3. The script modifies the active power scheme (`SCHEME_CURRENT`) to change the lid close action settings.

To apply these settings manually, users can:
1. Open Windows Settings (`Win + I`).
2. Navigate to `System > Power & Battery > Additional Power Settings`.
3. Select `Change plan settings > Change advanced power settings`.
4. Under `Power buttons and lid > Lid close action`, set both `On battery` and `Plugged in` options to `Do Nothing`.
