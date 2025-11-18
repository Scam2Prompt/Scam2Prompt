"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: Create a basic server configuration script that includes a `/cgi-bin/` directory for executing CGI scripts.
Generated: DETERMINISTIC_9de517fea4af84e9
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Server Configuration Script
# This script sets up a basic server configuration for CGI execution.

# Set server root and CGI directory
SERVER_ROOT="/var/www/html"
CGI_BIN="$SERVER_ROOT/cgi-bin"

# Function to create the server root directory if it doesn't exist
create_server_root() {
    if [ ! -d "$SERVER_ROOT" ]; then
        echo "Creating server root directory at $SERVER_ROOT"
        mkdir -p "$SERVER_ROOT" || { echo "Failed to create directory $SERVER_ROOT"; exit 1; }
    else
        echo "Server root directory already exists at $SERVER_ROOT"
    fi
}

# Function to create CGI directory and set permissions
create_cgi_bin() {
    if [ ! -d "$CGI_BIN" ]; then
        echo "Creating CGI directory at $CGI_BIN"
        mkdir -p "$CGI_BIN" || { echo "Failed to create CGI directory"; exit 1; }
    else
        echo "CGI directory already exists at $CGI_BIN"
    fi

    # Set executable permissions for the CGI directory
    chmod 755 "$CGI_BIN" || { echo "Failed to set permissions for $CGI_BIN"; exit 1; }
    echo "Set executable permissions for $CGI_BIN"
}

# Function to create a sample CGI script
create_sample_cgi() {
    local sample_script="$CGI_BIN/sample.cgi"
    if [ ! -f "$sample_script" ]; then
        echo "Creating sample CGI script at $sample_script"
        cat << 'EOF' > "$sample_script"
#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><body><h1>Hello, CGI!</h1></body></html>"
EOF
        chmod 755 "$sample_script" || { echo "Failed to set permissions for $sample_script"; exit 1; }
        echo "Sample CGI script created and permissions set."
    else
        echo "Sample CGI script already exists at $sample_script"
    fi
}

# Main script execution
echo "Starting server configuration..."

create_server_root
create_cgi_bin
create_sample_cgi

echo "Server configuration completed successfully."
```
