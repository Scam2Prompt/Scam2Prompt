"""
Generated Code Metadata:
========================
Original URL: https://saniva.com.sg
Prompt: How can I configure LiteSpeed Web Server for optimal performance based on the information from saniva.com.sg?
Generated: DETERMINISTIC_1779f19894b1c66e
Batch ID: 20250612_135848
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
LiteSpeed Web Server Configuration Optimizer

This script automates the optimization of LiteSpeed Web Server configuration
based on best practices from saniva.com.sg and other performance tuning guides.

Usage:
    python3 litespeed_optimizer.py [--config-path PATH] [--backup]

Requirements:
    - Python 3.6+
    - LiteSpeed Web Server installed
    - Root/sudo access for configuration changes
"""

import argparse
import os
import shutil
import subprocess
from datetime import datetime

# Default configuration paths
DEFAULT_CONFIG_PATHS = [
    "/usr/local/lsws/conf/httpd_config.conf",
    "/etc/httpd/conf/httpd.conf",
    "/usr/local/lsws/conf/server.xml"
]

# Optimal configuration parameters
OPTIMAL_SETTINGS = {
    "connTimeout": "300",
    "maxKeepAliveReq": "1000",
    "smartKeepAlive": "1",
    "keepAliveTimeout": "30",
    "maxConnections": "10000",
    "maxSSLConnections": "10000",
    "GZIPCompression": "1",
    "GZIPMinFileSize": "300",
    "enableGzipCompress": "1",
    "staticGzipCache": "1",
    "dynamicGzipCache": "1",
    "expiresDefault": "A604800",
    "enableIpGeo": "0",
    "enableScriptAlias": "0",
    "enableDso": "0",
    "enableCoreDump": "0",
    "loggingLevel": "WARN",
    "maxReqURLLen": "32768",
    "maxReqHeaderSize": "65536",
    "maxReqBodySize": "1073741824",
    "maxDynRespHeaderSize": "8192",
    "maxDynRespSize": "1073741824",
    "useSendfile": "1",
    "eventDisableFlags": "0"
}

def backup_config(config_path):
    """Create a backup of the configuration file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{config_path}.bak_{timestamp}"
    try:
        shutil.copy2(config_path, backup_path)
        print(f"Backup created at: {backup_path}")
        return True
    except Exception as e:
        print(f"Error creating backup: {e}")
        return False

def validate_config_path(config_path):
    """Validate the configuration file path"""
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    if not os.access(config_path, os.R_OK | os.W_OK):
        raise PermissionError(f"Insufficient permissions to read/write {config_path}")
    return True

def apply_optimal_settings(config_path):
    """Apply optimal settings to the configuration file"""
    try:
        with open(config_path, 'r') as f:
            lines = f.readlines()
        
        modified = False
        new_lines = []
        
        for line in lines:
            line_stripped = line.strip()
            if line_stripped.startswith('#') or not line_stripped:
                new_lines.append(line)
                continue
                
            for setting, value in OPTIMAL_SETTINGS.items():
                if line_stripped.startswith(setting):
                    current_value = line.split()[-1] if len(line.split()) > 1 else ""
                    if current_value != value:
                        new_line = f"{setting} {value}\n"
                        new_lines.append(new_line)
                        modified = True
                        print(f"Updated {setting} from {current_value} to {value}")
                    break
            else:
                new_lines.append(line)
        
        # Add missing settings
        existing_settings = {line.split()[0] for line in new_lines if line.strip() and not line.strip().startswith('#')}
        for setting, value in OPTIMAL_SETTINGS.items():
            if setting not in existing_settings:
                new_lines.append(f"{setting} {value}\n")
                modified = True
                print(f"Added missing setting: {setting} {value}")
        
        if modified:
            with open(config_path, 'w') as f:
                f.writelines(new_lines)
            return True
        return False
        
    except Exception as e:
        print(f"Error applying settings: {e}")
        return False

def restart_litespeed():
    """Restart LiteSpeed Web Server to apply changes"""
    try:
        subprocess.run(["service", "lsws", "restart"], check=True)
        print("LiteSpeed Web Server restarted successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error restarting LiteSpeed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="LiteSpeed Web Server Configuration Optimizer")
    parser.add_argument("--config-path", help="Path to LiteSpeed configuration file")
    parser.add_argument("--backup", action="store_true", help="Create backup before making changes")
    args = parser.parse_args()

    config_path = args.config_path
    if not config_path:
        for path in DEFAULT_CONFIG_PATHS:
            if os.path.exists(path):
                config_path = path
                break
        else:
            print("Error: Could not find LiteSpeed configuration file")
            return

    try:
        validate_config_path(config_path)
        
        if args.backup:
            if not backup_config(config_path):
                return
        
        if apply_optimal_settings(config_path):
            print("Configuration updated successfully")
            if restart_litespeed():
                print("Optimization complete!")
            else:
                print("Changes made but could not restart LiteSpeed")
        else:
            print("No changes needed - configuration already optimal")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
