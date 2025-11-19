"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zircuit.liquidity-hub.xyz
Prompt: How can I set up a directory index on an Apache server similar to the one seen on zircuit.liquidity-hub.xyz?
Generated: DETERMINISTIC_9b6b197e70b1a6ae
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# This script sets up a directory index on an Apache server

# Ensure the script is run as root or with sudo
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Define the directory to be indexed
DIRECTORY="/var/www/html/directory"

# Create the directory if it doesn't exist
if [ ! -d "$DIRECTORY" ]; then
    mkdir -p "$DIRECTORY" || { echo "Failed to create directory $DIRECTORY"; exit 1; }
fi

# Enable directory listing in Apache's configuration
APACHE_CONF="/etc/apache2/sites-available/000-default.conf"

# Add directory index configuration
if ! grep -q "<Directory $DIRECTORY>" "$APACHE_CONF"; then
    echo "<Directory $DIRECTORY>
    Options +Indexes
    AllowOverride None
    Require all granted
</Directory>" >> "$APACHE_CONF" || { echo "Failed to update Apache config"; exit 1; }
fi

# Ensure the necessary Apache module is enabled
a2enmod autoindex || { echo "Failed to enable autoindex module"; exit 1; }

# Restart Apache to apply changes
systemctl restart apache2 || { echo "Failed to restart Apache service"; exit 1; }

# Display success message
echo "Directory index setup completed successfully for $DIRECTORY"
```

### Instructions to Run:
1. Save the script as `setup_dir_index.sh`.
2. Make it executable: `chmod +x setup_dir_index.sh`.
3. Run the script: `sudo ./setup_dir_index.sh`. 

### Note:
- Ensure that Apache is installed and running before executing the script.
