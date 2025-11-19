"""
Generated Code Metadata:
========================
Original URL: https://monadsters.info
Prompt: What are best practices for configuring server permissions to avoid "403 Forbidden" errors?
Generated: DETERMINISTIC_be08df3610fbb569
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import stat
from pathlib import Path

def set_secure_permissions(file_path):
    """
    Set secure permissions for a file or directory to avoid 403 Forbidden errors.
    
    Args:
        file_path (str/Path): Path to the file or directory
    """
    try:
        path = Path(file_path)
        
        if path.is_file():
            # Set file permissions: owner read/write, group/others read-only
            path.chmod(stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
        elif path.is_dir():
            # Set directory permissions: owner read/write/execute, group/others read/execute
            path.chmod(stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | 
                      stat.S_IRGRP | stat.S_IXGRP | 
                      stat.S_IROTH | stat.S_IXOTH)
        else:
            raise FileNotFoundError(f"Path does not exist: {file_path}")
            
    except PermissionError as e:
        print(f"Permission denied when setting permissions for {file_path}: {e}")
    except Exception as e:
        print(f"Error setting permissions for {file_path}: {e}")

def verify_web_server_permissions(web_root):
    """
    Verify and correct common web server permission issues.
    
    Args:
        web_root (str/Path): Path to web server root directory
    """
    try:
        web_root = Path(web_root)
        
        # Verify web root exists
        if not web_root.exists():
            raise FileNotFoundError(f"Web root directory not found: {web_root}")
            
        # Set proper permissions for web root
        set_secure_permissions(web_root)
        
        # Common web files that need proper permissions
        important_files = [
            web_root / "index.html",
            web_root / "robots.txt",
            web_root / ".htaccess"
        ]
        
        for file in important_files:
            if file.exists():
                set_secure_permissions(file)
                
        # Verify CGI/script files have execute permissions if they exist
        cgi_bin = web_root / "cgi-bin"
        if cgi_bin.exists():
            set_secure_permissions(cgi_bin)
            for script in cgi_bin.glob("*"):
                if script.is_file():
                    script.chmod(script.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                    
    except Exception as e:
        print(f"Error verifying web server permissions: {e}")

def check_ownership(path, user=None, group=None):
    """
    Check and optionally correct file ownership.
    
    Args:
        path (str/Path): Path to check
        user (str): Expected username (optional)
        group (str): Expected group (optional)
    """
    try:
        path = Path(path)
        stat_info = path.stat()
        
        if user and stat_info.st_uid != os.getuid():
            print(f"Warning: File {path} not owned by current user")
            
        if group and stat_info.st_gid != os.getgid():
            print(f"Warning: File {path} not owned by current group")
            
    except Exception as e:
        print(f"Error checking ownership for {path}: {e}")

# Example usage
if __name__ == "__main__":
    web_root = "/var/www/html"
    verify_web_server_permissions(web_root)
    check_ownership(web_root)
```
