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
import shutil
import winreg
import ctypes
import sys
import platform
import subprocess
from typing import List, Optional, Dict

def is_admin() -> bool:
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def run_as_admin() -> bool:
    """Relaunch the script with admin privileges."""
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    return False

def remove_registry_entries() -> None:
    """Remove malicious registry entries related to browser hijacking."""
    malicious_keys = [
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
        r"Software\Microsoft\Internet Explorer\Main",
        r"Software\Microsoft\Windows\CurrentVersion\Policies\Ext",
        r"Software\Microsoft\Windows\CurrentVersion\Uninstall",
        r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    malicious_values = ["SearchThatWeb", "BrowserExtension", "WebSearch"]

    try:
        for key_path in malicious_keys:
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                    for value_name in malicious_values:
                        try:
                            winreg.DeleteValue(key, value_name)
                        except WindowsError:
                            pass
            except WindowsError:
                pass

            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                    for value_name in malicious_values:
                        try:
                            winreg.DeleteValue(key, value_name)
                        except WindowsError:
                            pass
            except WindowsError:
                pass
    except Exception as e:
        print(f"Error cleaning registry: {e}")

def remove_malicious_files() -> None:
    """Remove malicious files associated with browser hijacking."""
    temp_dirs = [
        os.environ.get("TEMP", ""),
        os.environ.get("TMP", ""),
        os.path.join(os.environ.get("APPDATA", ""), "Temp"),
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "Temp")
    ]

    malicious_files = [
        "SearchThatWeb.exe",
        "BrowserExtension.dll",
        "WebSearch.dll",
        "searchthatweb.crx",
        "browserextension.xpi"
    ]

    for temp_dir in temp_dirs:
        if not temp_dir:
            continue
        for root, _, files in os.walk(temp_dir):
            for file in files:
                if file.lower() in [f.lower() for f in malicious_files]:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception as e:
                        print(f"Error removing file {file}: {e}")

def reset_browser_settings() -> None:
    """Reset browser settings to default for major browsers."""
    browsers = ["chrome", "firefox", "edge", "opera", "brave"]
    
    for browser in browsers:
        try:
            if browser == "chrome":
                chrome_path = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome", "User Data")
                if os.path.exists(chrome_path):
                    shutil.rmtree(os.path.join(chrome_path, "Default"), ignore_errors=True)
            elif browser == "firefox":
                firefox_path = os.path.join(os.environ.get("APPDATA", ""), "Mozilla", "Firefox", "Profiles")
                if os.path.exists(firefox_path):
                    for profile in os.listdir(firefox_path):
                        if profile.endswith(".default"):
                            shutil.rmtree(os.path.join(firefox_path, profile), ignore_errors=True)
            elif browser == "edge":
                edge_path = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "Edge", "User Data")
                if os.path.exists(edge_path):
                    shutil.rmtree(os.path.join(edge_path, "Default"), ignore_errors=True)
        except Exception as e:
            print(f"Error resetting {browser} settings: {e}")

def remove_scheduled_tasks() -> None:
    """Remove potentially malicious scheduled tasks."""
    try:
        tasks = subprocess.check_output(["schtasks", "/query", "/fo", "LIST"]).decode("utf-8", errors="ignore")
        malicious_tasks = ["SearchThatWeb", "BrowserUpdate", "WebSearch"]
        
        for task in malicious_tasks:
            if task in tasks:
                subprocess.run(["schtasks", "/delete", "/tn", task, "/f"], check=True)
    except Exception as e:
        print(f"Error removing scheduled tasks: {e}")

def main() -> None:
    """Main function to execute the malware removal process."""
    if platform.system() != "Windows":
        print("This script is designed for Windows only.")
        return

    if not is_admin():
        print("Administrator privileges required. Restarting with elevated permissions...")
        run_as_admin()
        return

    print("Starting malware removal process...")
    remove_registry_entries()
    remove_malicious_files()
    reset_browser_settings()
    remove_scheduled_tasks()
    print("Malware removal process completed. Please restart your computer.")

if __name__ == "__main__":
    main()
```
