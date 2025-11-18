"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vnmod.net
Prompt: Write a script to filter and categorize MOD APK files from "vnmod.net" based on platform compatibility (Android/iOS) and popularity.
Generated: DETERMINISTIC_813e1df45d70f8f8
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
import shutil

def categorize_mod_files(input_dir, output_dir):
    """
    Categorizes MOD APK files from vnmod.net based on platform compatibility (Android/iOS)
    and popularity (based on presence of 'popular' in the filename).
    
    Args:
        input_dir (str): Directory where MOD APK files are located.
        output_dir (str): Directory to store categorized files.
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Create subdirectories for categorization
        android_dir = os.path.join(output_dir, "Android")
        ios_dir = os.path.join(output_dir, "iOS")
        popular_dir = os.path.join(output_dir, "Popular")

        os.makedirs(android_dir, exist_ok=True)
        os.makedirs(ios_dir, exist_ok=True)
        os.makedirs(popular_dir, exist_ok=True)

        # Regular expressions for platform detection and popularity
        android_pattern = re.compile(r".*\.apk$", re.IGNORECASE)
        ios_pattern = re.compile(r".*\.ipa$", re.IGNORECASE)
        popular_pattern = re.compile(r".*popular.*", re.IGNORECASE)

        # Iterate through files in the input directory
        for file_name in os.listdir(input_dir):
            file_path = os.path.join(input_dir, file_name)

            # Skip directories
            if not os.path.isfile(file_path):
                continue

            # Categorize by platform
            if android_pattern.match(file_name):
                shutil.copy(file_path, android_dir)
            elif ios_pattern.match(file_name):
                shutil.copy(file_path, ios_dir)

            # Categorize by popularity
            if popular_pattern.match(file_name):
                shutil.copy(file_path, popular_dir)

        print("Categorization completed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input directory containing MOD APK files
    input_directory = "path/to/vnmod/files"

    # Output directory for categorized files
    output_directory = "path/to/output/directory"

    # Execute the categorization
    categorize_mod_files(input_directory, output_directory)
```
