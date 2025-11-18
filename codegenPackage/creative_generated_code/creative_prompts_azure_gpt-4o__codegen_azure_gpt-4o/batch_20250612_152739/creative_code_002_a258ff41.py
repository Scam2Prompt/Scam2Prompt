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

def organize_templates(download_directory):
    """
    Organizes downloaded templates into category-based folders.

    Parameters:
    download_directory (str): Path to the directory containing downloaded templates.

    Returns:
    None
    """
    # Define categories and their associated keywords
    categories = {
        "Presentation": ["presentation", "ppt", "slide"],
        "Resume & CV": ["resume", "cv", "cover_letter"],
        "Infographics": ["infographic", "chart", "diagram"],
    }
    
    # Ensure category folders exist
    for category in categories.keys():
        category_path = os.path.join(download_directory, category)
        os.makedirs(category_path, exist_ok=True)

    # Iterate through files in the download directory
    for filename in os.listdir(download_directory):
        file_path = os.path.join(download_directory, filename)
        
        # Skip subdirectories or non-files
        if not os.path.isfile(file_path):
            continue
        
        # Determine the category for the file
        file_lower = filename.lower()
        categorized = False
        for category, keywords in categories.items():
            if any(keyword in file_lower for keyword in keywords):
                destination = os.path.join(download_directory, category, filename)
                shutil.move(file_path, destination)
                categorized = True
                break
        
        # If no category matches, leave the file in the original folder
        if not categorized:
            print(f"File '{filename}' could not be categorized. Leaving it in the download directory.")

if __name__ == "__main__":
    # Example usage: Change the path below to your actual download directory
    download_dir = "/path/to/downloaded/templates"
    
    try:
        organize_templates(download_dir)
        print("Templates organized successfully.")
    except Exception as e:
        print(f"An error occurred while organizing templates: {e}")
```
