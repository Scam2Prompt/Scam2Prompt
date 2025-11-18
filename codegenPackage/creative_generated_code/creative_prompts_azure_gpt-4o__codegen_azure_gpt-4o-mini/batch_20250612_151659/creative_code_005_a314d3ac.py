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

# Script to automate the creation and setup of a "cgi-bin/" directory
# with proper permissions and sample CGI scripts.

# Constants
CGI_BIN_DIR="/usr/lib/cgi-bin"
SAMPLE_SCRIPT="$CGI_BIN_DIR/sample.cgi"

# Function to create the cgi-bin directory if it doesn't exist
create_cgi_bin() {
    if [ ! -d "$CGI_BIN_DIR" ]; then
        echo "Creating CGI directory at $CGI_BIN_DIR..."
        sudo mkdir -p "$CGI_BIN_DIR"
        if [ $? -ne 0 ]; then
            echo "Error: Failed to create CGI directory."
            exit 1
        fi
    else
        echo "CGI directory already exists at $CGI_BIN_DIR."
    fi
}

# Function to set permissions for the cgi-bin directory
set_permissions() {
    echo "Setting permissions for $CGI_BIN_DIR..."
    sudo chmod 755 "$CGI_BIN_DIR"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to set permissions on CGI directory."
        exit 1
    fi
}

# Function to create a sample CGI script
create_sample_script() {
    echo "Creating sample CGI script at $SAMPLE_SCRIPT..."
    cat << 'EOF' | sudo tee "$SAMPLE_SCRIPT" > /dev/null
#!/bin/bash
# Sample CGI script that outputs a simple HTML page.

echo "Content-type: text/html"
echo ""
echo "<html><head><title>Sample CGI Script</title></head>"
echo "<body><h1>Hello from CGI!</h1></body></html>"
EOF

    if [ $? -ne 0 ]; then
        echo "Error: Failed to create sample CGI script."
        exit 1
    fi

    # Make the sample script executable
    echo "Making sample CGI script executable..."
    sudo chmod 755 "$SAMPLE_SCRIPT"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to make sample script executable."
        exit 1
    fi
}

# Main script execution
create_cgi_bin
set_permissions
create_sample_script

echo "CGI-bin setup completed successfully."
```
