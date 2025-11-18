"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanillagift.remadet.com
Prompt: Write a script to configure a LiteSpeed Web Server to prevent directory indexing and display a custom error page instead.
Generated: DETERMINISTIC_a2bd9af35ef97209
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to configure LiteSpeed Web Server to prevent directory indexing
# and display a custom error page.

# Exit immediately if a command fails
set -e

# Variables
LITESPEED_CONF_DIR="/usr/local/lsws/conf"
CUSTOM_ERROR_PAGE="/usr/local/lsws/conf/custom_403.html"

# Create a custom error page
cat <<EOF > "${CUSTOM_ERROR_PAGE}"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access Forbidden</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f8f9fa;
            color: #343a40;
            padding: 50px;
        }
        h1 {
            font-size: 2em;
            margin: 20px 0;
        }
        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <h1>403 - Access Forbidden</h1>
    <p>You are not permitted to access this directory.</p>
</body>
</html>
EOF

# Ensure the LiteSpeed configuration directory exists
if [ ! -d "${LITESPEED_CONF_DIR}" ]; then
    echo "Error: LiteSpeed configuration directory '${LITESPEED_CONF_DIR}' not found."
    exit 1
fi

# Append directory indexing prevention to the server configuration
LITESPEED_CONF_FILE="${LITESPEED_CONF_DIR}/httpd_config.conf"

if grep -q "IndexFiles" "${LITESPEED_CONF_FILE}"; then
    echo "Directory indexing is already configured in '${LITESPEED_CONF_FILE}'."
else
    echo "Configuring LiteSpeed to prevent directory indexing..."
    cat <<EOF >> "${LITESPEED_CONF_FILE}"

# Prevent directory indexing
IndexFiles ""
AutoIndex off

# Custom error page for 403
ErrorDocument 403 ${CUSTOM_ERROR_PAGE}

EOF
    echo "Configuration updated in '${LITESPEED_CONF_FILE}'."
fi

# Restart LiteSpeed server to apply changes
echo "Restarting LiteSpeed Web Server..."
/usr/local/lsws/bin/lswsctrl restart

echo "LiteSpeed Web Server has been configured successfully."
```
