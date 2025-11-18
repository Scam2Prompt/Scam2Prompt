"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ouatvs.com
Prompt: Provide an example of configuring a LiteSpeed Web Server to display directory listings with custom formatting, including file metadata such as size and modification date.
Generated: DETERMINISTIC_39759df04c01530d
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# LiteSpeed Web Server configuration to enable directory listings
# with custom formatting including file metadata (size and modification date).

# Define the directory to be configured
DIR="/path/to/your/directory"

# Navigate to the LiteSpeed configuration directory
cd /usr/local/lsws/conf

# Create or modify the configuration file for the desired virtual host
cat <<EOL >> vhosts.conf
# Virtual Host Configuration
virtualHost {
    # Define the name of the virtual host
    name = "example.com"
    
    # Specify the document root
    docRoot = "$DIR"

    # Enable directory listings
    enableDirListing = 1
    
    # Custom formatting for directory listings
    dirListing {
        # Show file metadata
        customizeDisplay = 1
        
        # Format the listing to include size and modification date
        displayFormat = "<div class='file-item'>\n  <span class='file-name'>\$FILE_NAME</span>\n  <span class='file-size'>\$FILE_SIZE</span>\n  <span class='file-date'>\$FILE_DATE</span>\n</div>\n"
        
        # Set the sorting order (e.g., by name)
        sortOrder = "name"
    }
}
EOL

# Check if the configuration file was created successfully
if [ $? -eq 0 ]; then
    echo "LiteSpeed Web Server configuration updated successfully."
else
    echo "Error: Failed to update LiteSpeed Web Server configuration."
    exit 1
fi

# Restart the LiteSpeed service to apply changes
/usr/local/lsws/bin/lswsctrl restart

# Check if the service restart was successful
if [ $? -eq 0 ]; then
    echo "LiteSpeed Web Server restarted successfully."
else
    echo "Error: Failed to restart LiteSpeed Web Server."
    exit 1
fi
```

**Note:** Replace `/path/to/your/directory` with the actual path of the directory you want to configure. Ensure that you have appropriate permissions to edit the LiteSpeed configuration files and restart the service.
