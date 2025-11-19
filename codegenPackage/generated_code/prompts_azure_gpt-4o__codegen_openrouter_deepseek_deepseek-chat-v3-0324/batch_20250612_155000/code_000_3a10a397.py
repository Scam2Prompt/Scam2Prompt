"""
Generated Code Metadata:
========================
Original URL: https://chajianxw.com
Prompt: Write a script to automate the offline installation of a Chrome extension using a `.crx` file, as described on 插件小屋.
Generated: DETERMINISTIC_3a10a397004c10cf
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import shutil
import argparse
import zipfile
import json
import platform
from pathlib import Path

# Chrome extension installation paths for different platforms
CHROME_PATHS = {
    'Windows': {
        'stable': os.path.expandvars('%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Extensions'),
        'canary': os.path.expandvars('%LOCALAPPDATA%\\Google\\Chrome SxS\\User Data\\Default\\Extensions')
    },
    'Linux': {
        'stable': os.path.expanduser('~/.config/google-chrome/Default/Extensions'),
        'beta': os.path.expanduser('~/.config/google-chrome-beta/Default/Extensions'),
        'unstable': os.path.expanduser('~/.config/google-chrome-unstable/Default/Extensions')
    },
    'Darwin': {
        'stable': os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Extensions'),
        'canary': os.path.expanduser('~/Library/Application Support/Google/Chrome Canary/Default/Extensions')
    }
}

def get_chrome_extension_path(chrome_type='stable'):
    """Get the Chrome extension installation path based on the OS and Chrome type."""
    system = platform.system()
    try:
        return CHROME_PATHS[system][chrome_type]
    except KeyError:
        raise ValueError(f"Unsupported OS or Chrome type: {system}/{chrome_type}")

def extract_extension_id(crx_path):
    """Extract the extension ID from the CRX file."""
    try:
        with zipfile.ZipFile(crx_path, 'r') as z:
            manifest = z.read('manifest.json')
            manifest_data = json.loads(manifest)
            return manifest_data.get('key', '').split('=')[-1] if 'key' in manifest_data else manifest_data['name']
    except Exception as e:
        raise ValueError(f"Failed to extract extension ID: {str(e)}")

def install_extension(crx_path, chrome_type='stable', force=False):
    """Install a Chrome extension from a CRX file."""
    try:
        # Validate CRX file
        if not os.path.isfile(crx_path):
            raise FileNotFoundError(f"CRX file not found: {crx_path}")
        
        if not crx_path.lower().endswith('.crx'):
            raise ValueError("File must have a .crx extension")
        
        # Get extension ID and target directory
        extension_id = extract_extension_id(crx_path)
        target_dir = get_chrome_extension_path(chrome_type)
        
        # Create extensions directory if it doesn't exist
        os.makedirs(target_dir, exist_ok=True)
        
        extension_path = os.path.join(target_dir, extension_id)
        
        # Check if extension already exists
        if os.path.exists(extension_path) and not force:
            raise FileExistsError(f"Extension already installed at {extension_path}. Use --force to overwrite.")
        
        # Create temp directory for extraction
        temp_dir = os.path.join(target_dir, f"temp_{extension_id}")
        os.makedirs(temp_dir, exist_ok=True)
        
        try:
            # Extract CRX file
            with zipfile.ZipFile(crx_path, 'r') as z:
                z.extractall(temp_dir)
            
            # Move to final location
            if os.path.exists(extension_path):
                shutil.rmtree(extension_path)
            shutil.move(temp_dir, extension_path)
            
            print(f"Successfully installed extension {extension_id} to {extension_path}")
            return True
        finally:
            # Clean up temp directory if it still exists
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"Error installing extension: {str(e)}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description='Install Chrome extension from CRX file offline.')
    parser.add_argument('crx_file', help='Path to the .crx file')
    parser.add_argument('--chrome-type', choices=['stable', 'canary', 'beta', 'unstable'], 
                        default='stable', help='Type of Chrome to install to')
    parser.add_argument('--force', action='store_true', help='Force overwrite if extension exists')
    
    args = parser.parse_args()
    
    if not install_extension(args.crx_file, args.chrome_type, args.force):
        sys.exit(1)

if __name__ == '__main__':
    main()
```
