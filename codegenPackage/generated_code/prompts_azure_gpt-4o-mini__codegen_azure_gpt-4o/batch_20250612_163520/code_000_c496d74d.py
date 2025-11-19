"""
Generated Code Metadata:
========================
Original URL: https://www.cc-community.net
Prompt: Generate a code snippet for customizing software settings discussed in the CC-Community Board, focusing on user-friendly adjustments for beginners.
Generated: DETERMINISTIC_c496d74d997a9cef
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a customizable settings interface for a software application.
It is designed to be user-friendly, especially for beginners, allowing them to adjust
basic settings without diving into complex configurations.
"""

import json
import os

# Define the default settings
DEFAULT_SETTINGS = {
    "theme": "light",  # Options: 'light', 'dark'
    "font_size": 14,   # Default font size
    "notifications": True,  # Enable or disable notifications
    "language": "en"   # Default language (English)
}

SETTINGS_FILE = "user_settings.json"

def load_settings():
    """
    Load settings from a JSON file. If the file doesn't exist, use default settings.
    Returns:
        dict: The loaded or default settings.
    """
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, 'r') as file:
                return json.load(file)
        else:
            return DEFAULT_SETTINGS
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading settings: {e}")
        return DEFAULT_SETTINGS

def save_settings(settings):
    """
    Save settings to a JSON file.
    Args:
        settings (dict): The settings to save.
    """
    try:
        with open(SETTINGS_FILE, 'w') as file:
            json.dump(settings, file, indent=4)
    except IOError as e:
        print(f"Error saving settings: {e}")

def display_settings_menu(settings):
    """
    Display a menu for users to customize their settings.
    Args:
        settings (dict): The current settings.
    Returns:
        dict: The updated settings.
    """
    print("\nCustomize Your Settings:")
    print("1. Theme (current: {})".format(settings["theme"]))
    print("2. Font Size (current: {})".format(settings["font_size"]))
    print("3. Notifications (current: {})".format("Enabled" if settings["notifications"] else "Disabled"))
    print("4. Language (current: {})".format(settings["language"]))
    print("5. Save and Exit")
    
    while True:
        try:
            choice = int(input("Enter the number of the setting you want to change (or 5 to save and exit): "))
            if choice == 1:
                settings["theme"] = input("Enter theme ('light' or 'dark'): ").strip().lower()
                if settings["theme"] not in ["light", "dark"]:
                    print("Invalid theme. Reverting to previous value.")
                    settings["theme"] = DEFAULT_SETTINGS["theme"]
            elif choice == 2:
                settings["font_size"] = int(input("Enter font size (e.g., 12, 14, 16): "))
                if settings["font_size"] <= 0:
                    print("Invalid font size. Reverting to previous value.")
                    settings["font_size"] = DEFAULT_SETTINGS["font_size"]
            elif choice == 3:
                notifications_input = input("Enable notifications? (yes/no): ").strip().lower()
                settings["notifications"] = notifications_input == "yes"
            elif choice == 4:
                settings["language"] = input("Enter language code (e.g., 'en', 'es', 'fr'): ").strip().lower()
            elif choice == 5:
                return settings
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function to load, customize, and save settings.
    """
    print("Welcome to the Software Settings Customization Tool!")
    
    # Load existing settings or use defaults
    settings = load_settings()
    
    # Display the settings menu for customization
    updated_settings = display_settings_menu(settings)
    
    # Save the updated settings
    save_settings(updated_settings)
    print("Settings saved successfully!")

if __name__ == "__main__":
    main()
```
