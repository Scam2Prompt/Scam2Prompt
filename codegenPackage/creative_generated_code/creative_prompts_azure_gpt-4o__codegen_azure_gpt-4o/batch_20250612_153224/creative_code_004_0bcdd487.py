"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owjkade.com
Prompt: Provide a guide to keep a laptop running with the lid closed in Windows 11, as explained on اوج کده.
Generated: DETERMINISTIC_0bcdd487c3db3218
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Guide Automation Script to Configure Windows 11 for Keeping Laptop Running with Lid Closed

This script provides a step-by-step guide to configure power settings in Windows 11.
It automates displaying instructions and checks where possible, ensuring proper configuration.

NOTE:
This script does not directly modify settings (as Python cannot natively access or modify Windows power settings).
Instead, it provides instructions to the user.
"""

import os
import sys

def main():
    try:
        print("=== Guide: Keep Laptop Running with Lid Closed in Windows 11 ===")
        print("Follow these steps:")
        print("Step 1: Open Control Panel")
        print("         - Press `Win + R` to open the Run dialog.")
        print("         - Type `control` and hit Enter to open Control Panel.")
        
        print("Step 2: Navigate to Power Options")
        print("         - In Control Panel, search for 'Power Options'.")
        print("         - Click on 'Power Options' to proceed.")

        print("Step 3: Modify Lid Close Action")
        print("         - In Power Options, click on 'Choose what closing the lid does' (on the left sidebar).")
        print("         - Under 'When I close the lid', set 'On battery' and 'Plugged in' to 'Do nothing'.")
        print("         - Click 'Save changes' to apply.")

        print("Step 4: Verify Settings")
        print("         - Ensure the settings have been saved by reopening 'Choose what closing the lid does'.")
    
        print("\nOptional Step: Adjust Additional Settings")
        print("         - In Power Options, you can configure advanced settings for sleep and hibernation.")
        print("         - To prevent unintended shutdowns, ensure 'Turn off display' is set to a desired value.")
        
        # Check if Control Panel exists in the system path
        if not is_control_panel_accessible():
            print("WARNING: Control Panel might not be accessible directly. Verify installation or access settings.")
        
        print("\n=== Configuration Complete ===")
        print("Your laptop should now stay running when the lid is closed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def is_control_panel_accessible():
    """
    Checks if the 'control' command is accessible in the system environment.
    Returns:
        bool: True if accessible, False otherwise.
    """
    return os.system("control") == 0

if __name__ == "__main__":
    main()
```
