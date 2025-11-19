"""
Generated Code Metadata:
========================
Original URL: https://statapk.com
Prompt: Develop a Python program that categorizes APK files downloaded from APKMabbu into predefined folders based on their category (e.g., "Entertainment," "Tools").
Generated: DETERMINISTIC_4a1ce3f2c8c86465
Batch ID: 20250612_154250
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
from pathlib import Path

# Define the categories and their corresponding folders
CATEGORIES = {
    "Entertainment": ["entertainment", "game", "social"],
    "Tools": ["tool", "productivity", "utility"],
    "Education": ["education", "learning", "study"],
    "Finance": ["finance", "banking", "money"],
    "Health & Fitness": ["health", "fitness", "wellness"],
    "Sports": ["sports", "game", "fitness"],
}

def categorize_apk(apk_path, destination_root):
    """
    Categorize an APK file into a predefined folder based on its category.

    Args:
        apk_path (str): The path to the APK file.
        destination_root (str): The root directory where categories are stored.

    Returns:
        None
    """
    apk_file = Path(apk_path)
    if not apk_file.exists() or apk_file.suffix.lower() != ".apk":
        print(f"Error: {apk_path} is not a valid APK file.")
        return

    apk_name = apk_file.stem.lower()
    categorized = False

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in apk_name:
                destination = os.path.join(destination_root, category)
                os.makedirs(destination, exist_ok=True)
                try:
                    shutil.move(apk_path, destination)
                    print(f"Moved {apk_file.name} to {category}")
                    categorized = True
                    break
                except Exception as e:
                    print(f"Error moving {apk_file.name}: {str(e)}")
        if categorized:
            break

    if not categorized:
        print(f"{apk_file.name} could not be categorized.")

def main():
    apk_dir = input("Enter the directory containing APK files: ")
    destination_root = input("Enter the destination root directory for categories: ")

    if not os.path.exists(apk_dir):
        print("Error: APK directory does not exist.")
        return

    if not os.path.exists(destination_root):
        os.makedirs(destination_root)
        print(f"Created destination root directory: {destination_root}")

    for filename in os.listdir(apk_dir):
        if filename.endswith(".apk"):
            apk_path = os.path.join(apk_dir, filename)
            categorize_apk(apk_path, destination_root)

if __name__ == "__main__":
    main()
```
