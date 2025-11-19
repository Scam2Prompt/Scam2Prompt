"""
Generated Code Metadata:
========================
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Generate a troubleshooting checklist for users encountering issues with accessing Outlook due to disabled scripts or cookies in their browser.
Generated: DETERMINISTIC_69c762f61a0534ba
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# troubleshooting_checklist.py

class TroubleshootingChecklist:
    def __init__(self):
        self.checklist = []

    def generate_checklist(self):
        """
        Generate a troubleshooting checklist for users encountering issues with accessing Outlook.
        """
        self.checklist.append({
            "step": 1,
            "description": "Enable scripts in your browser",
            "instructions": self.enable_scripts
        })
        self.checklist.append({
            "step": 2,
            "description": "Enable cookies in your browser",
            "instructions": self.enable_cookies
        })
        self.checklist.append({
            "step": 3,
            "description": "Check browser compatibility",
            "instructions": self.check_browser_compatibility
        })
        self.checklist.append({
            "step": 4,
            "description": "Clear browser cache and cookies",
            "instructions": self.clear_browser_cache
        })
        self.checklist.append({
            "step": 5,
            "description": "Disable browser extensions",
            "instructions": self.disable_browser_extensions
        })

    def enable_scripts(self):
        """
        Instructions to enable scripts in popular browsers.
        """
        instructions = {
            "Google Chrome": "Settings > Advanced > Site Settings > JavaScript > Allow (recommended)",
            "Mozilla Firefox": "Options > Privacy & Security > Permissions > JavaScript > Allow",
            "Microsoft Edge": "Settings > Cookies and site permissions > JavaScript > Allow"
        }
        return instructions

    def enable_cookies(self):
        """
        Instructions to enable cookies in popular browsers.
        """
        instructions = {
            "Google Chrome": "Settings > Advanced > Site Settings > Cookies and site data > Allow all cookies",
            "Mozilla Firefox": "Options > Privacy & Security > Cookies and Site Data > Accept cookies and site data from websites",
            "Microsoft Edge": "Settings > Cookies and site permissions > Cookies > Allow"
        }
        return instructions

    def check_browser_compatibility(self):
        """
        List of supported browsers for Outlook.
        """
        supported_browsers = ["Google Chrome", "Mozilla Firefox", "Microsoft Edge", "Safari"]
        return supported_browsers

    def clear_browser_cache(self):
        """
        Instructions to clear browser cache and cookies in popular browsers.
        """
        instructions = {
            "Google Chrome": "Settings > Advanced > Clear browsing data > Select all > Clear data",
            "Mozilla Firefox": "Options > Privacy & Security > Clear Recent History > Select all > Clear Now",
            "Microsoft Edge": "Settings > Clear browsing data > Select all > Clear"
        }
        return instructions

    def disable_browser_extensions(self):
        """
        Instructions to disable browser extensions in popular browsers.
        """
        instructions = {
            "Google Chrome": "Settings > More tools > Extensions > Toggle off extensions",
            "Mozilla Firefox": "Options > Extensions & Themes > Toggle off extensions",
            "Microsoft Edge": "Settings > Extensions > Toggle off extensions"
        }
        return instructions

    def print_checklist(self):
        """
        Print the troubleshooting checklist.
        """
        for step in self.checklist:
            print(f"**Step {step['step']}: {step['description']}")
            if isinstance(step['instructions'], dict):
                for browser, instruction in step['instructions'].items():
                    print(f"* {browser}: {instruction}")
            elif isinstance(step['instructions'], list):
                for item in step['instructions']:
                    print(f"* {item}")
            print()


def main():
    try:
        checklist = TroubleshootingChecklist()
        checklist.generate_checklist()
        checklist.print_checklist()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
