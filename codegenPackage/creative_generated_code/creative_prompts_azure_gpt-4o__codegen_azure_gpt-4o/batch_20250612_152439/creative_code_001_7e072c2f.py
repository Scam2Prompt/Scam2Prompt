"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: Recommend best practices for configuring a `cgi-bin` directory on a LiteSpeed Web Server to securely execute CGI scripts.
Generated: DETERMINISTIC_7e072c2f04972f5f
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# LiteSpeed Web Server Configuration Script for Secure CGI-bin Setup
# This script assumes you have LiteSpeed already installed and operational.

# Step 1: Create a directory for CGI scripts
CGI_DIR="/path/to/cgi-bin"
mkdir -p "${CGI_DIR}"

# Step 2: Set appropriate ownership and permissions
# Ensure that only the web server can execute files in this directory
WEB_SERVER_USER="www-data" # Update based on your server's user
chown -R "${WEB_SERVER_USER}:${WEB_SERVER_USER}" "${CGI_DIR}"
chmod -R 750 "${CGI_DIR}" # Owner can read/write/execute, group can read/execute

# Step 3: Configure LiteSpeed to recognize CGI directory
CONFIG_FILE="/usr/local/lsws/conf/httpd_config.conf" # Update based on your LiteSpeed installation

# Add CGI context to LiteSpeed configuration
cat <<EOF >> "${CONFIG_FILE}"

# CGI-bin Configuration
context /cgi-bin/ {
  type                    cgi
  location                ${CGI_DIR}
  allowBrowse             0
  addDefaultCharset       off
  setUIDMode              1
}

EOF

# Step 4: Set up CGI handlers (e.g., for Python, Perl, etc.)
# Ensure handlers are explicitly defined for security purposes
cat <<EOF >> "${CONFIG_FILE}"

# CGI Handlers
scriptHandler {
  add                     ".py" "/usr/bin/python3"
  add                     ".pl" "/usr/bin/perl"
}

EOF

# Step 5: Test configuration
echo "Testing LiteSpeed configuration..."
if /usr/local/lsws/bin/lswsctrl test; then
  echo "LiteSpeed configuration is valid."
else
  echo "Error in LiteSpeed configuration. Please review the changes."
  exit 1
fi

# Step 6: Restart LiteSpeed to apply changes
echo "Restarting LiteSpeed Web Server..."
/usr/local/lsws/bin/lswsctrl restart

echo "CGI-bin setup completed successfully."
```
