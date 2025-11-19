"""
Generated Code Metadata:
========================
Original URL: https://stewartpayroll.com
Prompt: Write a program that checks for browser compatibility with Paylocity's supported browsers and suggests an upgrade if necessary.
Generated: DETERMINISTIC_2d83c479720f5b3b
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# browser_compatibility_checker.py

import re

class BrowserCompatibilityChecker:
    """
    Checks browser compatibility with Paylocity's supported browsers.
    """

    def __init__(self):
        # Supported browsers and their minimum versions
        self.supported_browsers = {
            'Chrome': 90,
            'Firefox': 80,
            'Edge': 90,
            'Safari': 14,
            'Internet Explorer': None  # Not supported
        }

    def check_browser_compatibility(self, browser_name, browser_version):
        """
        Checks if the given browser and version are compatible with Paylocity.

        Args:
            browser_name (str): The name of the browser.
            browser_version (str): The version of the browser.

        Returns:
            dict: A dictionary containing a boolean indicating compatibility and a message.
        """
        try:
            # Validate browser name
            if browser_name not in self.supported_browsers:
                return {'compatible': False, 'message': f"Unsupported browser: {browser_name}"}

            # Check if browser is Internet Explorer
            if browser_name == 'Internet Explorer':
                return {'compatible': False, 'message': "Internet Explorer is not supported. Please upgrade to a modern browser."}

            # Validate browser version
            version = self._parse_browser_version(browser_version)
            if version is None:
                return {'compatible': False, 'message': f"Invalid browser version: {browser_version}"}

            # Check version compatibility
            min_supported_version = self.supported_browsers[browser_name]
            if min_supported_version is not None and version < min_supported_version:
                return {'compatible': False, 'message': f"Your {browser_name} version ({browser_version}) is outdated. Please upgrade to version {min_supported_version} or later."}

            return {'compatible': True, 'message': f"Your {browser_name} version ({browser_version}) is compatible."}

        except Exception as e:
            return {'compatible': False, 'message': f"An error occurred: {str(e)}"}

    @staticmethod
    def _parse_browser_version(version_str):
        """
        Parses a browser version string into an integer.

        Args:
            version_str (str): The browser version string.

        Returns:
            int or None: The parsed version as an integer, or None if parsing fails.
        """
        try:
            # Use regex to extract the major version number
            match = re.match(r'(\d+)', version_str)
            if match:
                return int(match.group(1))
        except Exception:
            pass
        return None


def main():
    checker = BrowserCompatibilityChecker()

    # Example usage:
    browsers_to_check = [
        {'name': 'Chrome', 'version': '89'},
        {'name': 'Firefox', 'version': '81'},
        {'name': 'Edge', 'version': '91'},
        {'name': 'Safari', 'version': '13'},
        {'name': 'Internet Explorer', 'version': '11'},
        {'name': 'Opera', 'version': '80'}  # Unsupported browser
    ]

    for browser in browsers_to_check:
        result = checker.check_browser_compatibility(browser['name'], browser['version'])
        print(f"Browser: {browser['name']} {browser['version']}")
        print(f"Compatible: {result['compatible']}")
        print(f"Message: {result['message']}\n")


if __name__ == "__main__":
    main()
```
