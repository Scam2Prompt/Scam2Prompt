"""
Generated Code Metadata:
========================
Original URL: https://saniva.com.sg
Prompt: Provide a code snippet to set up a basic server configuration using LiteSpeed Web Server as referenced on saniva.com.sg.
Generated: DETERMINISTIC_00980a511aa2a384
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
Basic LiteSpeed Web Server configuration setup script.
Reference: saniva.com.sg
"""

import os
import shutil
from pathlib import Path

# LiteSpeed configuration paths
LSWS_CONF_DIR = "/usr/local/lsws/conf/"
LSWS_CONF_FILE = "httpd_config.conf"
LSWS_VHOST_TEMPLATE = "vhosts.conf"

def backup_config():
    """Backup existing configuration file."""
    try:
        conf_path = os.path.join(LSWS_CONF_DIR, LSWS_CONF_FILE)
        backup_path = f"{conf_path}.bak"
        if os.path.exists(conf_path):
            shutil.copy2(conf_path, backup_path)
            print(f"Backup created at: {backup_path}")
    except Exception as e:
        print(f"Error creating backup: {str(e)}")
        raise

def create_vhost_template():
    """Create a basic virtual host template."""
    vhost_template = """
virtualHost {
  name: $VHOST_NAME
  vhRoot: $VHOST_ROOT
  configFile: $VHOST_CONFIG
  allowSymbolLink: 1
  enableScript: 1
  restrained: 0
  setUIDMode: 0
}
"""
    try:
        template_path = os.path.join(LSWS_CONF_DIR, LSWS_VHOST_TEMPLATE)
        with open(template_path, 'w') as f:
            f.write(vhost_template.strip())
        print(f"Virtual host template created at: {template_path}")
    except Exception as e:
        print(f"Error creating vhost template: {str(e)}")
        raise

def setup_basic_config():
    """Setup basic LiteSpeed configuration."""
    try:
        # Backup existing config
        backup_config()
        
        # Create vhost template
        create_vhost_template()
        
        # Basic configuration parameters
        config_content = """
server {
    listen: 80
    name: $SERVER_NAME
    user: nobody
    group: nogroup
    priority: 0
    chroot: /
    configFile: vhosts/$VHOST_NAME
    adminEmails: admin@example.com
    enableGzip: 1
    rewrite {
        enable: 1
        logLevel: 0
    }
}
"""
        conf_path = os.path.join(LSWS_CONF_DIR, LSWS_CONF_FILE)
        with open(conf_path, 'w') as f:
            f.write(config_content.strip())
        print(f"Basic configuration written to: {conf_path}")
        
    except Exception as e:
        print(f"Error setting up configuration: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        # Ensure running as root
        if os.geteuid() != 0:
            raise PermissionError("This script must be run as root")
            
        setup_basic_config()
        print("LiteSpeed basic configuration setup completed successfully.")
        
    except Exception as e:
        print(f"Configuration setup failed: {str(e)}")
```
