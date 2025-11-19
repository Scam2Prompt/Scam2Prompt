"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://attntoken.io
Prompt: What steps should I take to clear my browser cache when accessing a site hosted on BrainyCP?
Generated: DETERMINISTIC_deb8f63f1f059723
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import webbrowser
import os
import platform
import subprocess

def clear_browser_cache():
    """
    Clears the cache for commonly used web browsers.
    
    This function detects the operating system and performs the appropriate
    cache-clearing commands for Chrome, Firefox, and Safari.
    """

    try:
        # Determine the operating system
        os_type = platform.system()

        if os_type == "Windows":
            # Clear Chrome Cache
            chrome_cache_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache")
            if os.path.exists(chrome_cache_path):
                subprocess.call(['rmdir', '/s', '/q', chrome_cache_path], shell=True)

            # Clear Firefox Cache
            firefox_cache_path = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")
            if os.path.exists(firefox_cache_path):
                for profile in os.listdir(firefox_cache_path):
                    cache_path = os.path.join(firefox_cache_path, profile, "cache2")
                    if os.path.exists(cache_path):
                        subprocess.call(['rmdir', '/s', '/q', cache_path], shell=True)

        elif os_type == "Darwin":  # macOS
            # Clear Safari Cache
            safari_cache_path = os.path.expanduser("~/Library/Caches/com.apple.Safari")
            if os.path.exists(safari_cache_path):
                subprocess.call(['rm', '-rf', safari_cache_path])

            # Clear Chrome Cache
            chrome_cache_path = os.path.expanduser("~/Library/Caches/Google/Chrome/Default")
            if os.path.exists(chrome_cache_path):
                subprocess.call(['rm', '-rf', chrome_cache_path])

            # Clear Firefox Cache
            firefox_cache_path = os.path.expanduser("~/Library/Application Support/Firefox/Profiles")
            if os.path.exists(firefox_cache_path):
                for profile in os.listdir(firefox_cache_path):
                    cache_path = os.path.join(firefox_cache_path, profile, "cache2")
                    if os.path.exists(cache_path):
                        subprocess.call(['rm', '-rf', cache_path])

        elif os_type == "Linux":
            # Clear Chrome Cache
            chrome_cache_path = os.path.expanduser("~/.cache/google-chrome/Default/Cache")
            if os.path.exists(chrome_cache_path):
                subprocess.call(['rm', '-rf', chrome_cache_path])

            # Clear Firefox Cache
            firefox_cache_path = os.path.expanduser("~/.cache/mozilla/firefox")
            if os.path.exists(firefox_cache_path):
                for profile in os.listdir(firefox_cache_path):
                    cache_path = os.path.join(firefox_cache_path, profile, "cache2")
                    if os.path.exists(cache_path):
                        subprocess.call(['rm', '-rf', cache_path])

        print("Browser cache cleared successfully.")

    except Exception as e:
        print(f"An error occurred while clearing the browser cache: {e}")

if __name__ == "__main__":
    clear_browser_cache()
```
