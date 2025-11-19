"""
Generated Code Metadata:
========================
Original URL: https://starnet.so
Prompt: Provide an example of a directory structure for a web server similar to the one shown on starnet.so.
Generated: DETERMINISTIC_8cf3ab70cbf9a983
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Directory structure for a web server similar to starnet.so.
This follows a common web server structure with separation of concerns.
"""

import os

def create_directory_structure(base_path):
    """
    Creates a directory structure for a web server.
    
    Args:
        base_path (str): The root directory where the structure will be created.
    
    Raises:
        OSError: If directory creation fails.
    """
    try:
        # Main directories
        directories = [
            'public',          # Publicly accessible files
            'public/css',      # CSS files
            'public/js',       # JavaScript files
            'public/images',   # Image assets
            'public/fonts',    # Font files
            'src',             # Source files
            'src/routes',      # Route handlers
            'src/controllers', # Business logic
            'src/models',      # Data models
            'src/middlewares', # Middleware functions
            'src/utils',       # Utility functions
            'config',          # Configuration files
            'tests',           # Test files
            'logs',            # Server logs
            'tmp',             # Temporary files
            'uploads'          # User uploads
        ]

        # Create each directory
        for directory in directories:
            os.makedirs(os.path.join(base_path, directory), exist_ok=True)

        # Create sample files
        with open(os.path.join(base_path, 'public', 'index.html'), 'w') as f:
            f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Home</title>\n</head>\n<body>\n</body>\n</html>')

        with open(os.path.join(base_path, 'src', 'server.js'), 'w') as f:
            f.write('// Main server file\n')

        with open(os.path.join(base_path, 'config', 'config.js'), 'w') as f:
            f.write('// Configuration file\n')

        print(f"Directory structure created successfully at {base_path}")

    except OSError as e:
        print(f"Error creating directory structure: {e}")
        raise

# Example usage
if __name__ == "__main__":
    create_directory_structure("./web_server")
```
