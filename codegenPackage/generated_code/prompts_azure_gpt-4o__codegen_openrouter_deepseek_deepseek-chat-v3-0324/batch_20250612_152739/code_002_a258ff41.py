"""
Generated Code Metadata:
========================
Original URL: https://wowtemplates.in
Prompt: Generate a script that organizes downloaded templates from wowTemplates into folders based on categories like "Presentation," "Resume & CV," and "Infographics."
Generated: DETERMINISTIC_a258ff411f3aef56
Batch ID: 20250612_152739
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

# Define the categories and their corresponding keywords
CATEGORIES = {
    "Presentation": ["presentation", "ppt", "powerpoint", "slide"],
    "Resume & CV": ["resume", "cv", "curriculum vitae"],
    "Infographics": ["infographic", "info graphic", "data visualization"]
}

def categorize_file(filename, categories):
    """
    Categorize a file based on its name and predefined categories.
    
    Args:
        filename (str): Name of the file to categorize
        categories (dict): Dictionary of categories and their keywords
        
    Returns:
        str: The category name if matched, None otherwise
    """
    filename_lower = filename.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in filename_lower:
                return category
    return None

def organize_files(source_dir, dest_dir, categories):
    """
    Organize files from source directory into categorized folders in destination directory.
    
    Args:
        source_dir (str): Path to the directory containing files to organize
        dest_dir (str): Path to the directory where organized files will be placed
        categories (dict): Dictionary of categories and their keywords
        
    Raises:
        FileNotFoundError: If source directory doesn't exist
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist")
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Process each file in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
            
        # Get file category
        category = categorize_file(filename, categories)
        
        if category:
            # Create category directory if it doesn't exist
            category_dir = os.path.join(dest_dir, category)
            os.makedirs(category_dir, exist_ok=True)
            
            # Move file to category directory
            dest_path = os.path.join(category_dir, filename)
            try:
                shutil.move(file_path, dest_path)
                print(f"Moved '{filename}' to '{category}'")
            except Exception as e:
                print(f"Error moving '{filename}': {str(e)}")
        else:
            print(f"No category found for '{filename}' - skipping")

def main():
    # Configuration - adjust these paths as needed
    downloads_dir = str(Path.home() / "Downloads")
    organized_dir = str(Path.home() / "Documents" / "Organized Templates")
    
    try:
        print("Starting template organization...")
        organize_files(downloads_dir, organized_dir, CATEGORIES)
        print("Template organization completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
