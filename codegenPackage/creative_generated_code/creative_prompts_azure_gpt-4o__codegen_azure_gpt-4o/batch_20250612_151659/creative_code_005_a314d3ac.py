"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Generate a Bash script to automate the creation and setup of a "cgi-bin/" directory with proper permissions and sample CGI scripts.
Generated: DETERMINISTIC_a314d3acde6fa09c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Bash script to automate creation and setup of cgi-bin/ directory with proper permissions and sample CGI scripts.

# Exit immediately if a command exits with a non-zero status
set -e

# Define the cgi-bin directory path
CGI_BIN_DIR="cgi-bin"

# Function to create the cgi-bin directory
create_cgi_bin() {
    echo "Creating ${CGI_BIN_DIR} directory..."
    
    # Check if the directory already exists
    if [ -d "${CGI_BIN_DIR}" ]; then
        echo "Directory ${CGI_BIN_DIR} already exists. Skipping creation."
    else
        mkdir -p "${CGI_BIN_DIR}"
        echo "${CGI_BIN_DIR} directory created successfully."
    fi
}

# Function to set proper permissions for the cgi-bin directory
set_permissions() {
    echo "Setting permissions for ${CGI_BIN_DIR} directory..."
    
    # Set the directory to be readable and executable by everyone, writable by the owner
    chmod 755 "${CGI_BIN_DIR}"
    echo "Permissions set: 755 (rwxr-xr-x)"
}

# Function to create a sample CGI script
create_sample_scripts() {
    echo "Creating sample CGI scripts in ${CGI_BIN_DIR}..."
    
    # Sample Bash CGI script
    cat << 'EOF' > "${CGI_BIN_DIR}/hello.sh"
#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><body><h1>Hello, CGI World!</h1></body></html>"
EOF
    chmod 755 "${CGI_BIN_DIR}/hello.sh"
    echo "Sample Bash CGI script created: hello.sh"

    # Sample Python CGI script
    cat << 'EOF' > "${CGI_BIN_DIR}/hello.py"
#!/usr/bin/env python3

print("Content-type: text/html")
print("")
print("<html><body><h1>Hello, CGI World!</h1></body></html>")
EOF
    chmod 755 "${CGI_BIN_DIR}/hello.py"
    echo "Sample Python CGI script created: hello.py"
}

# Main execution block
echo "Starting cgi-bin setup script..."

create_cgi_bin
set_permissions
create_sample_scripts

echo "cgi-bin setup completed successfully."
```
