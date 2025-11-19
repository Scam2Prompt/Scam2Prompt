"""
Generated Code Metadata:
========================
Original URL: https://uzapa.com
Prompt: How to troubleshoot and fix a directory listing issue on a LiteSpeed Web Server?
Generated: DETERMINISTIC_75571bae5addf31f
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
LiteSpeed Web Server Directory Listing Troubleshooting Script

This script helps troubleshoot and fix directory listing issues on a LiteSpeed Web Server.
It checks common configuration problems and suggests fixes.
"""

import os
import re
import subprocess
import sys
from typing import Optional, List

class LiteSpeedDirectoryListingTroubleshooter:
    """
    A class to troubleshoot and fix directory listing issues on LiteSpeed Web Server.
    """
    
    def __init__(self):
        self.lsws_conf_path = "/usr/local/lsws/conf/httpd_config.conf"
        self.vhosts_dir = "/usr/local/lsws/conf/vhosts/"
        self.lsws_bin = "/usr/local/lsws/bin/lswsctrl"
        self.common_issues = {
            "index_files": "Check if index files (index.html, index.php) are missing",
            "auto_index": "Check if autoindex is disabled in configuration",
            "htaccess": "Check for .htaccess files overriding directory listing",
            "permissions": "Check directory and file permissions",
            "context": "Check virtual host context configuration"
        }
    
    def check_index_files(self, directory: str) -> bool:
        """Check if index files exist in the directory."""
        index_files = ['index.html', 'index.php', 'index.htm']
        return any(os.path.exists(os.path.join(directory, f)) for f in index_files)
    
    def check_autoindex_setting(self, vhost_config: str) -> Optional[bool]:
        """Check if autoindex is enabled in the virtual host configuration."""
        try:
            with open(vhost_config, 'r') as f:
                content = f.read()
                return "autoIndex 1" in content
        except FileNotFoundError:
            return None
    
    def check_htaccess(self, directory: str) -> bool:
        """Check for .htaccess files that might override directory listing."""
        htaccess_path = os.path.join(directory, '.htaccess')
        if os.path.exists(htaccess_path):
            with open(htaccess_path, 'r') as f:
                content = f.read()
                return "Options -Indexes" in content
        return False
    
    def check_permissions(self, directory: str) -> bool:
        """Check if directory has proper permissions (readable)."""
        return os.access(directory, os.R_OK)
    
    def find_vhost_config(self, domain: str) -> Optional[str]:
        """Find virtual host configuration file for a given domain."""
        try:
            for root, _, files in os.walk(self.vhosts_dir):
                for file in files:
                    if file.endswith('.conf'):
                        with open(os.path.join(root, file), 'r') as f:
                            if domain in f.read():
                                return os.path.join(root, file)
        except FileNotFoundError:
            return None
        return None
    
    def restart_litespeed(self) -> bool:
        """Restart LiteSpeed server to apply changes."""
        try:
            subprocess.run([self.lsws_bin, 'restart'], check=True)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def fix_autoindex(self, vhost_config: str, enable: bool = True) -> bool:
        """Enable or disable autoindex in virtual host configuration."""
        try:
            with open(vhost_config, 'r') as f:
                lines = f.readlines()
            
            updated = False
            new_lines = []
            for line in lines:
                if "autoIndex" in line:
                    new_line = f"  autoIndex {'1' if enable else '0'}\n"
                    new_lines.append(new_line)
                    updated = True
                else:
                    new_lines.append(line)
            
            if not updated:
                new_lines.append(f"  autoIndex {'1' if enable else '0'}\n")
            
            with open(vhost_config, 'w') as f:
                f.writelines(new_lines)
            
            return True
        except Exception:
            return False
    
    def troubleshoot(self, directory: str, domain: str) -> List[str]:
        """Run all troubleshooting checks and return found issues."""
        issues = []
        
        # Check index files
        if self.check_index_files(directory):
            issues.append(self.common_issues['index_files'])
        
        # Check virtual host configuration
        vhost_config = self.find_vhost_config(domain)
        if vhost_config:
            if not self.check_autoindex_setting(vhost_config):
                issues.append(self.common_issues['auto_index'])
        else:
            issues.append(f"Virtual host configuration not found for domain: {domain}")
        
        # Check .htaccess
        if self.check_htaccess(directory):
            issues.append(self.common_issues['htaccess'])
        
        # Check permissions
        if not self.check_permissions(directory):
            issues.append(self.common_issues['permissions'])
        
        return issues
    
    def auto_fix(self, directory: str, domain: str) -> bool:
        """Attempt to automatically fix common issues."""
        vhost_config = self.find_vhost_config(domain)
        if not vhost_config:
            return False
        
        # Fix autoindex
        if not self.check_autoindex_setting(vhost_config):
            if not self.fix_autoindex(vhost_config, True):
                return False
        
        # Restart server
        return self.restart_litespeed()

def main():
    """Main function for command-line execution."""
    if len(sys.argv) < 3:
        print("Usage: ./litespeed_dir_troubleshooter.py <directory> <domain>")
        print("Example: ./litespeed_dir_troubleshooter.py /var/www/html example.com")
        sys.exit(1)
    
    directory = sys.argv[1]
    domain = sys.argv[2]
    
    troubleshooter = LiteSpeedDirectoryListingTroubleshooter()
    
    print(f"\nTroubleshooting directory listing for: {directory}")
    print(f"Domain: {domain}\n")
    
    issues = troubleshooter.troubleshoot(directory, domain)
    
    if issues:
        print("Found the following potential issues:")
        for issue in issues:
            print(f"- {issue}")
        
        print("\nAttempting to fix issues automatically...")
        if troubleshooter.auto_fix(directory, domain):
            print("Auto-fix applied successfully. Please check if the issue is resolved.")
            print("Note: You may need to manually address some issues like missing index files.")
        else:
            print("Auto-fix failed. Please address the issues manually.")
    else:
        print("No common directory listing issues found.")
        print("The problem might be elsewhere in your configuration.")

if __name__ == "__main__":
    main()
```
