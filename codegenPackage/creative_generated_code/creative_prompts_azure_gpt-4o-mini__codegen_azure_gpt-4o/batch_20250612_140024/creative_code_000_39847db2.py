"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elmensajero.e-kraken.net
Prompt: What are the available directories in the e-Kraken web server and how can I access them programmatically?
Generated: DETERMINISTIC_39847db29cd1b66f
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_directories(server_directory_path):
    """
    List all available directories in the given server directory path.

    :param server_directory_path: Path to the root directory of the web server.
    :return: List of available directories.
    """
    try:
        # Validate if the given path exists
        if not os.path.exists(server_directory_path):
            raise FileNotFoundError(f"Path '{server_directory_path}' does not exist.")
        
        # List directories
        directories = [
            entry.name for entry in os.scandir(server_directory_path) if entry.is_dir()
        ]
        
        return directories
    except Exception as e:
        # Log errors and provide meaningful feedback
        print(f"Error: {e}")
        return []

def main():
    """
    Main function to demonstrate directory listing in the e-Kraken web server.

    Modify 'server_directory_path' to the root path of your e-Kraken web server.
    """
    # Path to the root directory of the web server (modify as needed)
    server_directory_path = "/path/to/e-kraken-web-server"
    
    # Fetch available directories
    directories = list_directories(server_directory_path)
    
    if directories:
        print("Available Directories in e-Kraken Web Server:")
        for directory in directories:
            print(f"- {directory}")
    else:
        print("No directories found or an error occurred.")

if __name__ == "__main__":
    main()
```
