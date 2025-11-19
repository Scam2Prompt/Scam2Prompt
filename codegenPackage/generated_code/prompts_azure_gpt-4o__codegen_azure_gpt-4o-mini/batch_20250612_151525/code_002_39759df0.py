"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Provide an example of configuring a LiteSpeed Web Server to display directory listings with custom formatting, including file metadata such as size and modification date.
Generated: DETERMINISTIC_39759df04c01530d
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# This script configures the LiteSpeed Web Server to enable directory listings
# with custom formatting, including file metadata such as size and modification date.

# Define the path to the LiteSpeed configuration file
CONFIG_FILE="/usr/local/lsws/conf/httpd_config.conf"

# Function to enable directory listings with custom formatting
enable_directory_listings() {
    # Check if the configuration file exists
    if [ ! -f "$CONFIG_FILE" ]; then
        echo "Error: Configuration file not found at $CONFIG_FILE"
        exit 1
    fi

    # Backup the original configuration file
    cp "$CONFIG_FILE" "$CONFIG_FILE.bak"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create a backup of the configuration file."
        exit 1
    fi

    # Append custom directory listing configuration
    cat <<EOL >> "$CONFIG_FILE"

# Custom Directory Listing Configuration
<Directory /path/to/your/directory>
    Options +Indexes
    IndexOptions FancyIndexing HTMLTable VersionSort
    HeaderName HEADER.html
    ReadmeName README.html
    IndexStyleSheet /path/to/your/stylesheet.css
</Directory>
EOL

    # Check if the configuration was added successfully
    if grep -q "<Directory /path/to/your/directory>" "$CONFIG_FILE"; then
        echo "Directory listings enabled with custom formatting."
    else
        echo "Error: Failed to enable directory listings."
        exit 1
    fi
}

# Function to restart LiteSpeed server to apply changes
restart_litespeed() {
    /usr/local/lsws/bin/lswsctrl restart
    if [ $? -ne 0 ]; then
        echo "Error: Failed to restart LiteSpeed server."
        exit 1
    fi
    echo "LiteSpeed server restarted successfully."
}

# Main execution
enable_directory_listings
restart_litespeed
```

**Note:** Replace `/path/to/your/directory` and `/path/to/your/stylesheet.css` with the actual paths you want to configure. Ensure that the LiteSpeed Web Server is installed and the script is executed with appropriate permissions.
