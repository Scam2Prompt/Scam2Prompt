"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Create a Python script to detect and remove malicious browser extensions like "HyperPlasmel" and "Bull Checker," following the removal guide on MyAntiSpyware.com.
Generated: DETERMINISTIC_e0fa417857801261
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
import shutil
import sqlite3
import json
import platform
from typing import List, Dict, Optional

# Constants for known malicious extensions
MALICIOUS_EXTENSIONS = {
    "chrome": ["HyperPlasmel", "Bull Checker"],
    "firefox": ["HyperPlasmel", "Bull Checker"],
    "edge": ["HyperPlasmel", "Bull Checker"]
}

# Browser paths based on OS
BROWSER_PATHS = {
    "Windows": {
        "chrome": os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data"),
        "firefox": os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles"),
        "edge": os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data")
    },
    "Darwin": {
        "chrome": os.path.expanduser("~/Library/Application Support/Google/Chrome"),
        "firefox": os.path.expanduser("~/Library/Application Support/Firefox/Profiles"),
        "edge": os.path.expanduser("~/Library/Application Support/Microsoft Edge")
    },
    "Linux": {
        "chrome": os.path.expanduser("~/.config/google-chrome"),
        "firefox": os.path.expanduser("~/.mozilla/firefox"),
        "edge": os.path.expanduser("~/.config/microsoft-edge")
    }
}

class BrowserExtensionCleaner:
    def __init__(self):
        self.system = platform.system()
        self.browser_paths = BROWSER_PATHS.get(self.system, {})
        
    def get_installed_extensions(self, browser: str) -> List[Dict]:
        """Get installed extensions for a specific browser."""
        extensions = []
        browser_path = self.browser_paths.get(browser)
        
        if not browser_path or not os.path.exists(browser_path):
            return extensions
            
        if browser == "chrome" or browser == "edge":
            extensions.extend(self._get_chrome_like_extensions(browser_path))
        elif browser == "firefox":
            extensions.extend(self._get_firefox_extensions(browser_path))
            
        return extensions
    
    def _get_chrome_like_extensions(self, browser_path: str) -> List[Dict]:
        """Get extensions for Chrome-like browsers (Chrome, Edge)."""
        extensions = []
        profiles = ["Default"] + [
            d for d in os.listdir(browser_path) 
            if d.startswith("Profile") and os.path.isdir(os.path.join(browser_path, d))
        ]
        
        for profile in profiles:
            profile_path = os.path.join(browser_path, profile)
            extensions_path = os.path.join(profile_path, "Extensions")
            
            if not os.path.exists(extensions_path):
                continue
                
            for ext_id in os.listdir(extensions_path):
                ext_path = os.path.join(extensions_path, ext_id)
                manifest_path = os.path.join(ext_path, "manifest.json")
                
                if not os.path.exists(manifest_path):
                    continue
                    
                try:
                    with open(manifest_path, "r", encoding="utf-8") as f:
                        manifest = json.load(f)
                        name = manifest.get("name", "")
                        if isinstance(name, dict):
                            name = name.get("message", name.get("default", ""))
                        extensions.append({
                            "id": ext_id,
                            "name": name,
                            "path": ext_path,
                            "profile": profile
                        })
                except (json.JSONDecodeError, UnicodeDecodeError) as e:
                    continue
                    
        return extensions
    
    def _get_firefox_extensions(self, browser_path: str) -> List[Dict]:
        """Get extensions for Firefox."""
        extensions = []
        
        for profile in os.listdir(browser_path):
            if not os.path.isdir(os.path.join(browser_path, profile)):
                continue
                
            extensions_path = os.path.join(browser_path, profile, "extensions")
            if not os.path.exists(extensions_path):
                continue
                
            # Check extensions.json
            extensions_json_path = os.path.join(browser_path, profile, "extensions.json")
            if os.path.exists(extensions_json_path):
                try:
                    with open(extensions_json_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        for addon in data.get("addons", []):
                            if "name" in addon and "path" in addon:
                                extensions.append({
                                    "id": addon.get("id", ""),
                                    "name": addon["name"],
                                    "path": addon["path"],
                                    "profile": profile
                                })
                except (json.JSONDecodeError, UnicodeDecodeError):
                    pass
                    
            # Check xpi files
            for ext_file in os.listdir(extensions_path):
                if ext_file.endswith(".xpi"):
                    extensions.append({
                        "id": ext_file,
                        "name": ext_file,
                        "path": os.path.join(extensions_path, ext_file),
                        "profile": profile
                    })
                    
        return extensions
    
    def is_malicious(self, extension_name: str, browser: str) -> bool:
        """Check if an extension is malicious."""
        malicious_list = MALICIOUS_EXTENSIONS.get(browser, [])
        return any(malicious.lower() in extension_name.lower() 
                  for malicious in malicious_list)
    
    def remove_extension(self, extension_path: str) -> bool:
        """Remove an extension by deleting its directory or file."""
        try:
            if os.path.isdir(extension_path):
                shutil.rmtree(extension_path)
            else:
                os.remove(extension_path)
            return True
        except (OSError, shutil.Error) as e:
            print(f"Error removing {extension_path}: {e}")
            return False
    
    def clean_browser(self, browser: str) -> Dict[str, List[Dict]]:
        """Clean malicious extensions from a specific browser."""
        results = {
            "found": [],
            "removed": [],
            "failed": []
        }
        
        extensions = self.get_installed_extensions(browser)
        for ext in extensions:
            if self.is_malicious(ext["name"], browser):
                results["found"].append(ext)
                if self.remove_extension(ext["path"]):
                    results["removed"].append(ext)
                else:
                    results["failed"].append(ext)
                    
        return results
    
    def clean_all_browsers(self) -> Dict[str, Dict[str, List[Dict]]]:
        """Clean all supported browsers."""
        results = {}
        for browser in self.browser_paths.keys():
            results[browser] = self.clean_browser(browser)
        return results

def main():
    cleaner = BrowserExtensionCleaner()
    results = cleaner.clean_all_browsers()
    
    print("\nMalicious Browser Extension Cleanup Results:")
    print("=" * 50)
    
    for browser, data in results.items():
        print(f"\n{browser.capitalize()}:")
        print(f"Found: {len(data['found'])}")
        print(f"Removed: {len(data['removed'])}")
        print(f"Failed to remove: {len(data['failed'])}")
        
        if data['found']:
            print("\nDetails of malicious extensions found:")
            for ext in data['found']:
                status = "REMOVED" if ext in data['removed'] else "FAILED"
                print(f"- {ext['name']} (Profile: {ext['profile']}) - {status}")

if __name__ == "__main__":
    main()
```
