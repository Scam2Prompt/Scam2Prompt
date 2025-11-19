"""
Generated Code Metadata:
========================
Original URL: https://psanda.co.za
Prompt: Can you provide code examples for organizing files in the public_html directory for a new website?
Generated: DETERMINISTIC_5492a6a32eca723f
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Directory Organizer Script**
```python
import os
import shutil

# Define the public_html directory path
PUBLIC_HTML_DIR = 'public_html'

def create_directory_structure():
    """
    Creates a basic directory structure for a new website in the public_html directory.
    """
    # Define the directory structure
    dir_structure = {
        'css': os.path.join(PUBLIC_HTML_DIR, 'css'),
        'js': os.path.join(PUBLIC_HTML_DIR, 'js'),
        'images': os.path.join(PUBLIC_HTML_DIR, 'images'),
        'uploads': os.path.join(PUBLIC_HTML_DIR, 'uploads'),
    }

    # Create the directories
    for dir_path in dir_structure.values():
        try:
            os.makedirs(dir_path, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory: {e}")

def organize_files():
    """
    Organizes files in the public_html directory into their respective folders.
    """
    # Define file extensions for each directory
    file_extensions = {
        'css': ['.css'],
        'js': ['.js'],
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    }

    # Iterate through files in the public_html directory
    for filename in os.listdir(PUBLIC_HTML_DIR):
        file_path = os.path.join(PUBLIC_HTML_DIR, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Organize the file
        for dir_name, extensions in file_extensions.items():
            if file_ext in extensions:
                dest_dir = os.path.join(PUBLIC_HTML_DIR, dir_name)
                try:
                    shutil.move(file_path, dest_dir)
                    print(f"Moved {filename} to {dir_name}")
                except Exception as e:
                    print(f"Error moving file: {e}")
                break

if __name__ == '__main__':
    create_directory_structure()
    organize_files()
```

**index.php Example**
```php
<?php
/**
 * Index.php file for the website.
 */

// Include configuration file
require_once 'config.php';

// Define constants
define('CSS_DIR', 'css');
define('JS_DIR', 'js');
define('IMAGES_DIR', 'images');

// Include CSS and JS files
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Website</title>
    <link rel="stylesheet" href="<?php echo CSS_DIR; ?>/styles.css">
</head>
<body>
    <!-- Content here -->
    <script src="<?php echo JS_DIR; ?>/script.js"></script>
</body>
</html>
```

**config.php Example**
```php
<?php
/**
 * Configuration file for the website.
 */

// Define database connection settings
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'username');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'database');

// Define other constants
?>
```
