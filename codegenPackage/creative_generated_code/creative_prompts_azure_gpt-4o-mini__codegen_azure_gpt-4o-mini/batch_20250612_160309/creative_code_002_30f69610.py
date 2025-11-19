"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myantispyware.com
Prompt: Can you provide a code snippet for automating the removal of browser hijackers as described on MyAntiSpyware?
Generated: DETERMINISTIC_30f696108eec3fd2
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import platform
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_windows():
    """Check if the operating system is Windows."""
    return platform.system() == "Windows"

def uninstall_program(program_name):
    """Uninstall a program if it is found in the installed programs list."""
    try:
        logging.info(f"Attempting to uninstall {program_name}...")
        if is_windows():
            subprocess.run(["wmic", "product", "where", f"name='{program_name}'", "call", "uninstall"], check=True)
        else:
            logging.warning("Uninstallation is only supported on Windows.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to uninstall {program_name}: {e}")

def remove_browser_extension(browser_name, extension_name):
    """Remove a browser extension if it exists."""
    try:
        logging.info(f"Attempting to remove {extension_name} from {browser_name}...")
        if browser_name.lower() == "chrome":
            # Path to Chrome Extensions directory (Windows)
            extensions_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Extensions")
            # Logic to find and remove the extension
            for ext in os.listdir(extensions_path):
                if extension_name in ext:
                    ext_path = os.path.join(extensions_path, ext)
                    logging.info(f"Removing extension at {ext_path}...")
                    os.rmdir(ext_path)  # Remove the extension directory
                    break
        else:
            logging.warning(f"Removing extensions from {browser_name} is not implemented.")
    except Exception as e:
        logging.error(f"Error removing extension {extension_name} from {browser_name}: {e}")

def clean_browser_settings(browser_name):
    """Reset browser settings to default to remove hijackers."""
    try:
        logging.info(f"Resetting settings for {browser_name}...")
        # Implement browser-specific reset logic here
        # This is an example and may vary based on the browser
        if browser_name.lower() == "chrome":
            chrome_settings_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Preferences")
            if os.path.exists(chrome_settings_path):
                with open(chrome_settings_path, 'r+') as file:
                    data = file.read()
                    file.seek(0)
                    file.write(data.replace('"homepage":', '"homepage": "default_url_here",'))  # Example modification
                    file.truncate()
            else:
                logging.error("Chrome preferences file not found.")
        else:
            logging.warning(f"Resetting settings for {browser_name} is not implemented.")
    except Exception as e:
        logging.error(f"Error resetting settings for {browser_name}: {e}")

def main():
    """Main function to perform the hijacker removal."""
    # Define the programs and extensions to remove
    programs_to_uninstall = ["Suspicious Program 1", "Suspicious Program 2"]
    browser_extensions_to_remove = {"chrome": ["Suspicious Extension 1", "Suspicious Extension 2"]}
    
    # Uninstall suspicious programs
    for program in programs_to_uninstall:
        uninstall_program(program)

    # Remove suspicious browser extensions
    for browser, extensions in browser_extensions_to_remove.items():
        for extension in extensions:
            remove_browser_extension(browser, extension)
            clean_browser_settings(browser)

if __name__ == "__main__":
    main()
```
