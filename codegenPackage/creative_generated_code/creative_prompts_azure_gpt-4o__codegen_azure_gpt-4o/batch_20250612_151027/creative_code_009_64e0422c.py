"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mylovelyplanet.cfd
Prompt: Write a script to replace the default HTTP Test Page with a custom HTML file on a CentOS-WebPanel-powered server.
Generated: DETERMINISTIC_64e0422c943e3493
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to replace the default HTTP Test Page on a CentOS-WebPanel-powered server
# with a custom HTML file.

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
DEFAULT_PAGE="/usr/local/cwpsrv/htdocs/index.html" # Path to the default HTTP Test Page
CUSTOM_HTML="/path/to/custom/index.html"          # Path to your custom HTML file
BACKUP_DIR="/usr/local/cwpsrv/htdocs/backup"      # Directory to store backups
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")                # Timestamp for backup file naming

# Function to check if the script is run as root
check_root() {
  if [[ $EUID -ne 0 ]]; then
    echo "Error: This script must be run as root. Exiting."
    exit 1
  fi
}

# Function to back up the original default HTTP Test Page
backup_default_page() {
  echo "Backing up the default HTTP Test Page..."
  mkdir -p "$BACKUP_DIR"
  cp "$DEFAULT_PAGE" "$BACKUP_DIR/index.html.$TIMESTAMP"
  echo "Backup saved to $BACKUP_DIR/index.html.$TIMESTAMP"
}

# Function to replace the default HTTP Test Page with the custom HTML file
replace_default_page() {
  echo "Replacing the default HTTP Test Page..."
  cp "$CUSTOM_HTML" "$DEFAULT_PAGE"
  echo "Custom HTML file has been successfully deployed as the new HTTP Test Page."
}

# Function to validate the existence of the custom HTML file
validate_custom_html() {
  if [[ ! -f "$CUSTOM_HTML" ]]; then
    echo "Error: Custom HTML file not found at $CUSTOM_HTML. Exiting."
    exit 1
  fi
}

# Main script execution
main() {
  check_root
  validate_custom_html
  backup_default_page
  replace_default_page
  echo "Operation completed successfully."
}

# Run the main function
main
```

### Usage Instructions:
1. Save the script to a file, e.g., `replace_http_test_page.sh`.
2. Make the script executable: `chmod +x replace_http_test_page.sh`.
3. Update the `CUSTOM_HTML` variable with the full path to your custom HTML file.
4. Run the script as root: `sudo ./replace_http_test_page.sh`.
