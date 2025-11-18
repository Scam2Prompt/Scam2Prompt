"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miles.plumenetworke.com
Prompt: Explain how to enable or disable directory listing in Apache on Debian, referencing the server configuration details from https://miles.plumenetworke.com.
Generated: DETERMINISTIC_160aaba48a81650f
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Enable or disable directory listing in Apache on Debian
# This script modifies the Apache configuration to change directory listing behavior.

# Paths to the Apache configuration files
APACHE_CONF="/etc/apache2/apache2.conf"
SITES_AVAILABLE="/etc/apache2/sites-available/000-default.conf"

# Function to enable directory listing
enable_directory_listing() {
    # Make a backup of the configuration file
    cp "$SITES_AVAILABLE" "$SITES_AVAILABLE.bak"

    # Enable directory listing by adding Options +Indexes
    if ! grep -q "Options +Indexes" "$SITES_AVAILABLE"; then
        echo "<Directory /var/www/html>" >> "$SITES_AVAILABLE"
        echo "    Options +Indexes" >> "$SITES_AVAILABLE"
        echo "</Directory>" >> "$SITES_AVAILABLE"
    fi

    # Restart Apache to apply changes
    systemctl restart apache2
    echo "Directory listing enabled."
}

# Function to disable directory listing
disable_directory_listing() {
    # Make a backup of the configuration file
    cp "$SITES_AVAILABLE" "$SITES_AVAILABLE.bak"

    # Disable directory listing by removing Options +Indexes
    sed -i '/<Directory \/var\/www\/html>/,/<\/Directory>/{
        s/Options +Indexes/Options -Indexes/
    }' "$SITES_AVAILABLE"

    # Restart Apache to apply changes
    systemctl restart apache2
    echo "Directory listing disabled."
}

# Check for command line arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 {enable|disable}"
    exit 1
fi

# Enable or disable directory listing based on the argument provided
case "$1" in
    enable)
        enable_directory_listing
        ;;
    disable)
        disable_directory_listing
        ;;
    *)
        echo "Invalid option. Use 'enable' or 'disable'."
        exit 1
        ;;
esac
```

### Usage
To enable directory listing, run:
```bash
sudo ./script.sh enable
```
To disable directory listing, run:
```bash
sudo ./script.sh disable
``` 

### Notes
- Make sure to replace `/var/www/html` with your actual document root if it differs.
- Ensure you have the necessary permissions to modify Apache configuration files and restart the service.
- The script creates a backup of the configuration file before making changes.
