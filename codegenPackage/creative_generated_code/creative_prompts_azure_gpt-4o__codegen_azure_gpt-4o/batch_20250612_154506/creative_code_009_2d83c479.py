"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stewartpayroll.com
Prompt: Write a program that checks for browser compatibility with Paylocity's supported browsers and suggests an upgrade if necessary.
Generated: DETERMINISTIC_2d83c479720f5b3b
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def check_browser_compatibility(browser_name, browser_version):
    """
    Checks if the browser is compatible with Paylocity's supported browsers.
    If not, suggests an upgrade.

    :param browser_name: str - Name of the browser (e.g., "Chrome", "Firefox", "Edge", "Safari")
    :param browser_version: float - Version number of the browser
    :return: str - Compatibility status or upgrade suggestion
    """
    # Supported browsers and their minimum required versions
    supported_browsers = {
        "Chrome": 90.0,
        "Firefox": 88.0,
        "Edge": 91.0,
        "Safari": 14.0
    }

    # Check if the browser is in the supported list
    if browser_name in supported_browsers:
        # Compare version numbers
        min_version = supported_browsers[browser_name]
        if browser_version >= min_version:
            return f"{browser_name} {browser_version} is compatible with Paylocity."
        else:
            return (f"{browser_name} {browser_version} is not compatible with Paylocity. "
                    f"Please upgrade to version {min_version} or higher.")
    else:
        return (f"{browser_name} is not a supported browser for Paylocity. "
                f"Please use one of the following browsers: {', '.join(supported_browsers.keys())}.")

def main():
    """
    Main entry point for the program.
    Accepts user input for browser name and version, and checks compatibility.
    """
    try:
        # Prompt the user for browser name and version
        browser_name = input("Enter your browser name (e.g., Chrome, Firefox, Edge, Safari): ").strip()
        browser_version = float(input("Enter your browser version (e.g., 90.0, 88.0): ").strip())

        # Check compatibility and display the result
        result = check_browser_compatibility(browser_name, browser_version)
        print(result)

    except ValueError:
        # Handle invalid input
        print("Error: Invalid browser version. Please enter a valid numeric version.")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Execute the program
    main()
```
