"""
Generated Code Metadata:
========================
Original URL: https://apkcima.com
Prompt: Write a function to validate APK file compatibility for apps listed on AloApk, such as "CapCut" and "Spotify Premium," based on the file size and version.
Generated: DETERMINISTIC_4a307ab127f300d8
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
from typing import Dict, Optional, Tuple

# Constants for known apps and their compatibility requirements
KNOWN_APPS = {
    "CapCut": {
        "min_version": "8.0.0",
        "max_version": "9.9.9",
        "min_size_mb": 50,
        "max_size_mb": 200
    },
    "Spotify Premium": {
        "min_version": "8.7.0",
        "max_version": "9.9.9",
        "min_size_mb": 30,
        "max_size_mb": 150
    }
}

def validate_apk_compatibility(apk_path: str, app_name: str) -> Tuple[bool, Optional[str]]:
    """
    Validate if an APK file is compatible with the specified app requirements.
    
    Args:
        apk_path: Path to the APK file
        app_name: Name of the app (must match KNOWN_APPS keys)
    
    Returns:
        Tuple of (is_valid, error_message) where error_message is None if valid
    """
    # Check if app is known
    if app_name not in KNOWN_APPS:
        return False, f"Unknown app: {app_name}"
    
    requirements = KNOWN_APPS[app_name]
    
    try:
        # Get file size in MB
        file_size_mb = os.path.getsize(apk_path) / (1024 * 1024)
        
        # Check file size
        if file_size_mb < requirements["min_size_mb"]:
            return False, f"File too small ({file_size_mb:.2f}MB < {requirements['min_size_mb']}MB)"
        if file_size_mb > requirements["max_size_mb"]:
            return False, f"File too large ({file_size_mb:.2f}MB > {requirements['max_size_mb']}MB)"
        
        # Extract version from filename (assuming format: AppName_vX.Y.Z.apk)
        filename = os.path.basename(apk_path)
        version_match = re.search(r'_v(\d+\.\d+\.\d+)\.apk$', filename)
        if not version_match:
            return False, "Could not extract version from filename"
        
        version = version_match.group(1)
        
        # Compare versions
        if version < requirements["min_version"]:
            return False, f"Version too old ({version} < {requirements['min_version']})"
        if version > requirements["max_version"]:
            return False, f"Version too new ({version} > {requirements['max_version']})"
            
        return True, None
        
    except FileNotFoundError:
        return False, "APK file not found"
    except PermissionError:
        return False, "Permission denied when accessing APK file"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"
```
