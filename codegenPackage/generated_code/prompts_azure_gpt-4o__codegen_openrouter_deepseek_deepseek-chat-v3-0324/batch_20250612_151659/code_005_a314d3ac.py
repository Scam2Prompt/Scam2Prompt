"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Generate a Bash script to automate the creation and setup of a "cgi-bin/" directory with proper permissions and sample CGI scripts.
Generated: DETERMINISTIC_a314d3acde6fa09c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to automate the creation and setup of a cgi-bin directory with proper permissions and sample CGI scripts

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" >&2
    exit 1
fi

# Default configuration
CGI_BIN_DIR="/var/www/cgi-bin"
APACHE_USER="www-data"
APACHE_GROUP="www-data"
SAMPLE_SCRIPTS=true

# Function to create directory and set permissions
setup_cgi_bin() {
    echo "Setting up CGI directory at $CGI_BIN_DIR..."
    
    # Create directory if it doesn't exist
    if [ ! -d "$CGI_BIN_DIR" ]; then
        mkdir -p "$CGI_BIN_DIR"
        if [ $? -ne 0 ]; then
            echo "Failed to create directory $CGI_BIN_DIR" >&2
            exit 1
        fi
    fi
    
    # Set ownership and permissions
    chown -R $APACHE_USER:$APACHE_GROUP "$CGI_BIN_DIR"
    chmod -R 755 "$CGI_BIN_DIR"
    
    echo "Directory permissions set successfully."
}

# Function to create sample CGI scripts
create_sample_scripts() {
    echo "Creating sample CGI scripts..."
    
    # Sample Bash CGI script
    cat > "$CGI_BIN_DIR/test.sh" << 'EOF'
#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Bash CGI Test</title></head>"
echo "<body>"
echo "<h1>Hello from Bash CGI!</h1>"
echo "<p>Current time: $(date)</p>"
echo "<p>Server name: $(hostname)</p>"
echo "</body></html>"
EOF
    
    # Sample Python CGI script
    cat > "$CGI_BIN_DIR/test.py" << 'EOF'
#!/usr/bin/env python3
print("Content-type: text/html\n")
print("""
<html>
<head><title>Python CGI Test</title></head>
<body>
<h1>Hello from Python CGI!</h1>
<p>Current time: %s</p>
</body>
</html>
""" % __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
EOF
    
    # Set executable permissions
    chmod +x "$CGI_BIN_DIR/test.sh"
    chmod +x "$CGI_BIN_DIR/test.py"
    
    echo "Sample scripts created successfully."
}

# Main execution
setup_cgi_bin

if [ "$SAMPLE_SCRIPTS" = true ]; then
    create_sample_scripts
fi

echo "CGI-bin setup completed successfully."
```
