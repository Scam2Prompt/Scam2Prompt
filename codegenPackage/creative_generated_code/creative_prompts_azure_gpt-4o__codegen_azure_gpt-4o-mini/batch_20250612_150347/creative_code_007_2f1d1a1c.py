"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abelltodoit.com.au
Prompt: Write a tutorial on setting up LiteSpeed Web Server to serve directories like those shown on https://abelltodoit.com.au, including `css`, `img`, and `js`.
Generated: DETERMINISTIC_2f1d1a1ca87b0961
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# This script sets up the LiteSpeed Web Server to serve static files from specified directories.
# It assumes that LiteSpeed is already installed on the server.

# Define the directories to be served
DOC_ROOT="/var/www/html"  # Change this to your document root if different
CSS_DIR="$DOC_ROOT/css"    # Directory for CSS files
IMG_DIR="$DOC_ROOT/img"    # Directory for image files
JS_DIR="$DOC_ROOT/js"      # Directory for JavaScript files

# Function to create a directory if it doesn't exist
create_directory() {
    local dir="$1"
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir" && echo "Created directory: $dir"
    else
        echo "Directory already exists: $dir"
    fi
}

# Create necessary directories
create_directory "$CSS_DIR"
create_directory "$IMG_DIR"
create_directory "$JS_DIR"

# Set proper permissions for the directories
set_permissions() {
    local dir="$1"
    chown -R www-data:www-data "$dir"  # Change ownership to the web server user
    chmod -R 755 "$dir"  # Set read and execute permissions
    echo "Set permissions for directory: $dir"
}

# Apply permissions to each directory
set_permissions "$CSS_DIR"
set_permissions "$IMG_DIR"
set_permissions "$JS_DIR"

# Update LiteSpeed configuration to serve static files
update_litespeed_config() {
    local config_file="/usr/local/lsws/conf/httpd_config.conf"

    # Backup the existing configuration
    cp "$config_file" "${config_file}.bak"

    # Append static file serving configuration
    cat <<EOL >> "$config_file"

# Serve static files directly
<Directory $DOC_ROOT>
    AllowOverride All
    Options Indexes FollowSymLinks
    Require all granted
</Directory>
EOL

    echo "Updated LiteSpeed configuration to serve static files."
}

# Restart LiteSpeed to apply changes
restart_litespeed() {
    /usr/local/lsws/bin/lswsctrl restart
    echo "LiteSpeed Web Server has been restarted."
}

# Execute functions
update_litespeed_config
restart_litespeed

# Print completion message
echo "LiteSpeed Web Server setup completed successfully."
```

### Important Notes:
- Ensure that this script is run with root privileges to have permission to create directories and change ownership.
- Modify the `DOC_ROOT` variable if your document root differs from `/var/www/html`.
- Before running the script, ensure that the path to the LiteSpeed binary (`/usr/local/lsws/bin/lswsctrl`) is correct for your installation.
- Always back up configuration files before making changes.
