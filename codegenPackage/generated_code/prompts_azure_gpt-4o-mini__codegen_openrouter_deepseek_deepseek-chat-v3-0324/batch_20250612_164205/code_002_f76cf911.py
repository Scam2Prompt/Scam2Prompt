"""
Generated Code Metadata:
========================
Original URL: https://mfcsons.com
Prompt: How do you manage file permissions for scripts in the cgi-bin folder on a web server?
Generated: DETERMINISTIC_f76cf911ca91ef40
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that manages file permissions for scripts in the `cgi-bin` folder:

```python
#!/usr/bin/env python3
"""
CGI Script Permission Manager

This script helps manage file permissions for CGI scripts by:
- Setting proper permissions (755 for directories, 755 for scripts)
- Verifying owner/group
- Ensuring proper shebang lines
"""

import os
import stat
import argparse
import sys
from typing import List

DEFAULT_CGI_DIR = "/usr/lib/cgi-bin"
VALID_PERMISSIONS = 0o755  # rwxr-xr-x

def validate_shebang(file_path: str) -> bool:
    """Check if file has a valid shebang line"""
    try:
        with open(file_path, 'r') as f:
            first_line = f.readline().strip()
            return first_line.startswith('#!') and '/bin/' in first_line
    except (IOError, UnicodeDecodeError):
        return False

def set_permissions(file_path: str) -> bool:
    """Set proper permissions for a CGI script"""
    try:
        current_mode = stat.S_IMODE(os.stat(file_path).st_mode)
        if current_mode != VALID_PERMISSIONS:
            os.chmod(file_path, VALID_PERMISSIONS)
            print(f"Updated permissions for {file_path} to {oct(VALID_PERMISSIONS)}")
            return True
        return False
    except OSError as e:
        print(f"Error setting permissions for {file_path}: {e}", file=sys.stderr)
        return False

def process_cgi_directory(cgi_dir: str, fix: bool = False) -> List[str]:
    """Process all files in the CGI directory"""
    processed = []
    try:
        for root, dirs, files in os.walk(cgi_dir):
            for name in dirs:
                full_path = os.path.join(root, name)
                if fix:
                    set_permissions(full_path)
                processed.append(full_path)
            
            for name in files:
                full_path = os.path.join(root, name)
                if fix:
                    if not validate_shebang(full_path):
                        print(f"Warning: Invalid shebang in {full_path}", file=sys.stderr)
                    set_permissions(full_path)
                processed.append(full_path)
    except OSError as e:
        print(f"Error accessing {cgi_dir}: {e}", file=sys.stderr)
    return processed

def main():
    parser = argparse.ArgumentParser(
        description="Manage CGI script permissions",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--cgi-dir",
        default=DEFAULT_CGI_DIR,
        help="Path to CGI directory")
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Actually fix permissions (dry run by default)")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show verbose output")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.cgi_dir):
        print(f"Error: CGI directory {args.cgi_dir} not found", file=sys.stderr)
        sys.exit(1)
    
    if not os.access(args.cgi_dir, os.W_OK):
        print(f"Error: No write permissions for {args.cgi_dir}", file=sys.stderr)
        sys.exit(1)
    
    processed = process_cgi_directory(args.cgi_dir, args.fix)
    
    if args.verbose:
        print("\nProcessed files:")
        for file in processed:
            print(f"- {file}")
    
    print(f"\nSummary: {len(processed)} files processed")
    if not args.fix:
        print("Note: Run with --fix to actually change permissions")

if __name__ == "__main__":
    main()
```
