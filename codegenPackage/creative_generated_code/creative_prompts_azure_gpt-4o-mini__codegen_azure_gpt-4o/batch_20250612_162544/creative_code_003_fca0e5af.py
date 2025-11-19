"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.windhaber.at
Prompt: What are the browser requirements for signing into Outlook on the Windhaber Exchange website?
Generated: DETERMINISTIC_fca0e5af5db0bc1d
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This script checks whether the user's browser meets the requirements for signing into Outlook
# on the Windhaber Exchange website. It provides feedback based on common browser compatibility criteria.

import platform
import sys

def check_browser_requirements(user_agent):
    """
    Checks if the browser meets the requirements for signing into Outlook on the Windhaber Exchange website.
    
    Args:
        user_agent (str): The user agent string of the browser.

    Returns:
        str: A message indicating whether the browser is supported or not.
    """
    # Minimum supported browser versions
    supported_browsers = {
        "Chrome": 90,
        "Firefox": 88,
        "Safari": 14,
        "Edge": 90
    }

    try:
        # Check if the user agent matches any of the supported browsers
        for browser, min_version in supported_browsers.items():
            if browser.lower() in user_agent.lower():
                # Extract the browser version from the user agent
                version_str = ''.join(filter(str.isdigit, user_agent.split(browser, 1)[1].split()[0]))
                version = int(version_str[:2]) if version_str else 0
                
                if version >= min_version:
                    return f"Your {browser} browser version {version} is supported."
                else:
                    return f"Your {browser} browser version {version} is not supported. Please upgrade to version {min_version} or higher."

        return "Your browser is not recognized or supported. Please use Chrome, Firefox, Safari, or Edge."
    
    except Exception as e:
        # Handle unexpected errors
        return f"An error occurred while checking browser requirements: {str(e)}"


if __name__ == "__main__":
    # Example user agent strings
    user_agent_examples = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/13.1.2",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/87.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/92.0"
    ]

    # Check each example user agent
    for user_agent in user_agent_examples:
        result = check_browser_requirements(user_agent)
        print(result)

```
