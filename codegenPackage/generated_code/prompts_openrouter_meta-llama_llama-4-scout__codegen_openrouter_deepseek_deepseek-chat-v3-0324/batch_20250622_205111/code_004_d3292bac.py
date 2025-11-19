"""
Generated Code Metadata:
========================
Original URL: https://thekygrand.com
Prompt: What security features does LiteSpeed Web Server offer that could be particularly beneficial for a website with a directory index like thekygrand.com?
Generated: DETERMINISTIC_d3292bac24e1133b
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates how to leverage LiteSpeed Web Server's security features
# for a website with directory indexing like thekygrand.com.

import os
import subprocess
from pathlib import Path

class LiteSpeedSecurityConfigurator:
    """
    A class to configure LiteSpeed Web Server security features for directory indexing.
    """
    
    def __init__(self, config_path='/usr/local/lsws/conf/httpd_config.conf'):
        """
        Initialize with the path to LiteSpeed configuration file.
        
        Args:
            config_path (str): Path to LiteSpeed main configuration file.
        """
        self.config_path = config_path
        self.backup_path = f"{config_path}.bak"
        
    def backup_config(self):
        """Create a backup of the current configuration file."""
        try:
            Path(self.config_path).rename(self.backup_path)
            print(f"Configuration backed up to {self.backup_path}")
            return True
        except Exception as e:
            print(f"Backup failed: {str(e)}")
            return False
    
    def restore_config(self):
        """Restore configuration from backup."""
        try:
            Path(self.backup_path).rename(self.config_path)
            print(f"Configuration restored from {self.backup_path}")
            return True
        except Exception as e:
            print(f"Restore failed: {str(e)}")
            return False
    
    def enable_modsecurity(self):
        """Enable ModSecurity web application firewall."""
        try:
            with open(self.config_path, 'a') as f:
                f.write("\nmodule mod_security {\n")
                f.write("  enable                  1\n")
                f.write("  logLevel                INFO\n")
                f.write("  ruleEngine              On\n")
                f.write("  auditEngine             On\n")
                f.write("  auditLog                logs/modsec_audit.log\n")
                f.write("}\n")
            print("ModSecurity enabled")
            return True
        except Exception as e:
            print(f"Failed to enable ModSecurity: {str(e)}")
            return False
    
    def configure_directory_indexing(self, allow_indexing=False):
        """
        Configure directory indexing security settings.
        
        Args:
            allow_indexing (bool): Whether to allow directory indexing.
        """
        try:
            with open(self.config_path, 'a') as f:
                f.write("\ncontext / {\n")
                f.write(f"  allowBrowse              {'1' if allow_indexing else '0'}\n")
                f.write("  directoryIndex           index.html,index.php\n")
                f.write("  forbiddenDir             .git,.svn\n")
                f.write("  hotlinkProtection        {\n")
                f.write("    enabled                1\n")
                f.write("    allowDirectRequest     1\n")
                f.write("    allowedHosts           *\n")
                f.write("    fileTypes              jpg,jpeg,gif,png\n")
                f.write("  }\n")
                f.write("}\n")
            print(f"Directory indexing {'enabled' if allow_indexing else 'disabled'}")
            return True
        except Exception as e:
            print(f"Failed to configure directory indexing: {str(e)}")
            return False
    
    def enable_brute_force_protection(self):
        """Enable brute force protection."""
        try:
            with open(self.config_path, 'a') as f:
                f.write("\nmodule mod_bf {\n")
                f.write("  enable                  1\n")
                f.write("  maxRetry                5\n")
                f.write("  banInterval             300\n")
                f.write("  logLevel                INFO\n")
                f.write("}\n")
            print("Brute force protection enabled")
            return True
        except Exception as e:
            print(f"Failed to enable brute force protection: {str(e)}")
            return False
    
    def enable_ssl(self, cert_path, key_path):
        """
        Enable SSL/TLS encryption.
        
        Args:
            cert_path (str): Path to SSL certificate
            key_path (str): Path to SSL private key
        """
        try:
            with open(self.config_path, 'a') as f:
                f.write("\nlistener SSL {\n")
                f.write("  address                 *:443\n")
                f.write("  secure                  1\n")
                f.write("  keyFile                 " + key_path + "\n")
                f.write("  certFile                " + cert_path + "\n")
                f.write("  sslProtocol             24\n")  # TLS 1.2 and 1.3
                f.write("  enableECDHE             1\n")
                f.write("  enableDHE               1\n")
                f.write("  cipherSuite             EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH\n")
                f.write("}\n")
            print("SSL/TLS enabled")
            return True
        except Exception as e:
            print(f"Failed to enable SSL: {str(e)}")
            return False
    
    def restart_litespeed(self):
        """Restart LiteSpeed to apply changes."""
        try:
            subprocess.run(['/usr/local/lsws/bin/lswsctrl', 'restart'], check=True)
            print("LiteSpeed restarted successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to restart LiteSpeed: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    configurator = LiteSpeedSecurityConfigurator()
    
    # Backup current config
    if not configurator.backup_config():
        exit(1)
    
    try:
        # Apply security configurations
        configurator.enable_modsecurity()
        configurator.configure_directory_indexing(allow_indexing=False)
        configurator.enable_brute_force_protection()
        configurator.enable_ssl('/path/to/cert.pem', '/path/to/key.pem')
        
        # Restart to apply changes
        configurator.restart_litespeed()
    except Exception as e:
        print(f"Configuration failed: {str(e)}")
        print("Restoring original configuration...")
        configurator.restore_config()
        configurator.restart_litespeed()
```
