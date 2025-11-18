"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://statapk.com
Prompt: Develop a Python program that categorizes APK files downloaded from APKMabbu into predefined folders based on their category (e.g., "Entertainment," "Tools").
Generated: DETERMINISTIC_4a1ce3f2c8c86465
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define the directory where APK files are downloaded
DOWNLOAD_DIR = "APKMabbu_Downloads"
# Define the destination directory where files will be categorized
DESTINATION_DIR = "Categorized_APKs"

# Define the categories and their associated keywords
CATEGORIES = {
    "Entertainment": ["game", "video", "music", "movie"],
    "Tools": ["utility", "editor", "calculator", "manager"],
    "Productivity": ["office", "task", "note", "calendar"],
    "Social": ["chat", "messaging", "network", "share"],
}

def create_category_folders():
    """Create category folders in the destination directory."""
    try:
        os.makedirs(DESTINATION_DIR, exist_ok=True)
        for category in CATEGORIES.keys():
            os.makedirs(os.path.join(DESTINATION_DIR, category), exist_ok=True)
        logging.info("Category folders created successfully.")
    except Exception as e:
        logging.error(f"Error creating category folders: {e}")

def categorize_apk_files():
    """Categorize APK files into predefined folders based on their category."""
    try:
        # List all APK files in the download directory
        for file_name in os.listdir(DOWNLOAD_DIR):
            if file_name.endswith('.apk'):
                categorized = False
                for category, keywords in CATEGORIES.items():
                    if any(keyword in file_name.lower() for keyword in keywords):
                        source_path = os.path.join(DOWNLOAD_DIR, file_name)
                        destination_path = os.path.join(DESTINATION_DIR, category, file_name)
                        shutil.move(source_path, destination_path)
                        logging.info(f"Moved '{file_name}' to '{category}' folder.")
                        categorized = True
                        break
                if not categorized:
                    logging.warning(f"No category found for '{file_name}'. It was not moved.")
    except Exception as e:
        logging.error(f"Error categorizing APK files: {e}")

def main():
    """Main function to create category folders and categorize APK files."""
    create_category_folders()
    categorize_apk_files()

if __name__ == "__main__":
    main()
```
