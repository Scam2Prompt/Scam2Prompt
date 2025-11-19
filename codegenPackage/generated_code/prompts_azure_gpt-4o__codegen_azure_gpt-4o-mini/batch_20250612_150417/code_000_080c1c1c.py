"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Write Python code to remove browser hijacking malware, specifically targeting redirects like "SearchThatWeb" as described on MyAntiSpyware.com.
Generated: DETERMINISTIC_080c1c1c9726f558
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import shutil
import subprocess
import sys

class BrowserHijackerRemover:
    def __init__(self):
        self.browsers = {
            'chrome': {
                'path': os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default',
                'prefs_file': 'Preferences'
            },
            'firefox': {
                'path': os.path.expanduser('~') + r'\AppData\Roaming\Mozilla\Firefox\Profiles',
                'prefs_file': 'prefs.js'
            },
            'edge': {
                'path': os.path.expanduser('~') + r'\AppData\Local\Microsoft\Edge\User Data\Default',
                'prefs_file': 'Preferences'
            }
        }
        self.redirect_pattern = re.compile(r'SearchThatWeb', re.IGNORECASE)

    def remove_hijacker(self):
        """Main method to initiate the removal process."""
        for browser, details in self.browsers.items():
            try:
                self.clean_browser_settings(details['path'], details['prefs_file'])
            except Exception as e:
                print(f"Error cleaning {browser}: {e}")

    def clean_browser_settings(self, browser_path, prefs_file):
        """Cleans the browser settings to remove hijacker entries."""
        if os.path.exists(browser_path):
            prefs_path = os.path.join(browser_path, prefs_file)
            if os.path.exists(prefs_path):
                self.backup_file(prefs_path)
                self.remove_redirects(prefs_path)
            else:
                print(f"{prefs_file} not found for {browser_path}.")
        else:
            print(f"Browser path {browser_path} does not exist.")

    def backup_file(self, file_path):
        """Creates a backup of the specified file."""
        backup_path = file_path + '.bak'
        shutil.copyfile(file_path, backup_path)
        print(f"Backup created at {backup_path}")

    def remove_redirects(self, prefs_path):
        """Removes hijacker entries from the preferences file."""
        with open(prefs_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove any entries related to the hijacker
        new_content = self.redirect_pattern.sub('', content)

        with open(prefs_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Redirects removed from {prefs_path}")

    def run(self):
        """Executes the removal process."""
        print("Starting browser hijacker removal process...")
        self.remove_hijacker()
        print("Browser hijacker removal process completed.")

if __name__ == "__main__":
    remover = BrowserHijackerRemover()
    remover.run()
```

**Note:** This code is intended for educational purposes. Always ensure you have backups and understand the implications of modifying browser settings.
