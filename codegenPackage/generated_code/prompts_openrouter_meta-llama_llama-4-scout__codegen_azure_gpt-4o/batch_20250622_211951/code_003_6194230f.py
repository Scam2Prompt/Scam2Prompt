"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Identify and remove the HyperPlasmel malicious extension from Chrome.
Generated: DETERMINISTIC_6194230f3684987b
Batch ID: 20250622_211951
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
import json

def find_and_remove_malicious_extension(extension_name="HyperPlasmel"):
    """
    Identifies and removes the specified malicious Chrome extension.
    
    Parameters:
        extension_name (str): The name of the malicious extension to remove.
    """
    try:
        # Get the path to Chrome's extensions directory
        chrome_extensions_path = os.path.expanduser(
            "~/.config/google-chrome/Default/Extensions"
        )
        
        # Check if the directory exists
        if not os.path.exists(chrome_extensions_path):
            print("Chrome extensions directory not found.")
            return
        
        # Iterate through all extension directories
        for extension_id in os.listdir(chrome_extensions_path):
            extension_path = os.path.join(chrome_extensions_path, extension_id)
            
            # Ensure the path is a directory
            if not os.path.isdir(extension_path):
                continue
            
            # Check each version folder for manifest.json
            for version_folder in os.listdir(extension_path):
                version_path = os.path.join(extension_path, version_folder)
                manifest_path = os.path.join(version_path, "manifest.json")
                
                if os.path.exists(manifest_path):
                    try:
                        # Read and parse the manifest.json file
                        with open(manifest_path, "r") as manifest_file:
                            manifest_data = json.load(manifest_file)
                        
                        # Check if the extension matches the malicious name
                        if manifest_data.get("name") == extension_name:
                            print(f"Malicious extension '{extension_name}' found at: {version_path}")
                            
                            # Remove the malicious extension directory
                            shutil.rmtree(extension_path)
                            print(f"Extension '{extension_name}' successfully removed.")
                            return
                    except (json.JSONDecodeError, IOError) as e:
                        print(f"Error reading manifest file: {e}")
                        continue
        
        print(f"No extension named '{extension_name}' found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function to find and remove the malicious extension
find_and_remove_malicious_extension()
```
