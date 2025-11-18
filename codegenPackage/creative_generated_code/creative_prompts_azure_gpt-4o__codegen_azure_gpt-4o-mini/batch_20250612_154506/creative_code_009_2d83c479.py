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

# List of supported browsers and their versions
SUPPORTED_BROWSERS = {
    "Chrome": "81.0.0",  # Minimum supported version
    "Firefox": "76.0.0",
    "Safari": "13.0.0",
    "Edge": "81.0.0",
    "Opera": "67.0.0"
}

class BrowserCompatibilityChecker:
    def __init__(self, browser_name, browser_version):
        """Initialize the checker with browser name and version."""
        self.browser_name = browser_name
        self.browser_version = browser_version

    def is_supported(self):
        """Check if the browser is supported and if the version is sufficient."""
        if self.browser_name not in SUPPORTED_BROWSERS:
            return False, "Browser not supported."
        
        required_version = SUPPORTED_BROWSERS[self.browser_name]
        if self.compare_versions(self.browser_version, required_version) < 0:
            return False, f"Upgrade required. Your version: {self.browser_version}, Required version: {required_version}."
        
        return True, "Browser is supported."

    @staticmethod
    def compare_versions(version1, version2):
        """Compare two version strings."""
        v1_parts = list(map(int, version1.split(".")))
        v2_parts = list(map(int, version2.split(".")))

        # Compare version parts
        for v1, v2 in zip(v1_parts, v2_parts):
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        # Check for additional parts
        if len(v1_parts) < len(v2_parts):
            return -1
        elif len(v1_parts) > len(v2_parts):
            return 1
        
        return 0

def main():
    """Main function to run the compatibility check."""
    if len(sys.argv) != 3:
        print("Usage: python browser_compatibility_checker.py <browser_name> <browser_version>")
        sys.exit(1)
    
    browser_name = sys.argv[1]
    browser_version = sys.argv[2]

    checker = BrowserCompatibilityChecker(browser_name, browser_version)
    is_compatible, message = checker.is_supported()
    print(message)

if __name__ == "__main__":
    main()
```
