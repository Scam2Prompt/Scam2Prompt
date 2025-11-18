"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wowtemplates.in
Prompt: Generate a script that organizes downloaded templates from wowTemplates into folders based on categories like "Presentation," "Resume & CV," and "Infographics."
Generated: DETERMINISTIC_a258ff411f3aef56
Batch ID: 20250612_152739
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

# Define the source directory where templates are downloaded
SOURCE_DIR = "/path/to/downloads/wowTemplates"
# Define the target directory where organized templates will be moved
TARGET_DIR = "/path/to/organized_templates"

# Define the categories and their corresponding keywords
CATEGORIES = {
    "Presentation": ["presentation", "slide", "deck"],
    "Resume & CV": ["resume", "cv", "curriculum"],
    "Infographics": ["infographic", "data visualization", "chart"]
}

def organize_templates(source_dir, target_dir):
    """
    Organizes downloaded templates into specified folders based on categories.

    :param source_dir: Directory containing the downloaded templates
    :param target_dir: Directory where organized templates will be moved
    """
    # Ensure target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Skip directories, only process files
        if os.path.isfile(file_path):
            moved = False
            
            # Check each category and its keywords
            for category, keywords in CATEGORIES.items():
                if any(keyword in filename.lower() for keyword in keywords):
                    category_path = os.path.join(target_dir, category)
                    
                    # Ensure category directory exists
                    os.makedirs(category_path, exist_ok=True)
                    
                    # Move the file to the categorized folder
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Moved '{filename}' to '{category}'")
                    moved = True
                    break  # Exit the loop once the file is moved

            # If the file doesn't match any category, inform the user
            if not moved:
                print(f"No category found for '{filename}', skipping.")

if __name__ == "__main__":
    try:
        organize_templates(SOURCE_DIR, TARGET_DIR)
    except Exception as e:
        print(f"An error occurred: {e}")
```
