"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivasikurirtokopedia.hstn.me
Prompt: Explain how to transfer an existing website to iFastNet hosting, including any necessary code or configurations.
Generated: DETERMINISTIC_97f8cad64598b3c1
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to transfer an existing website to iFastNet hosting
# Make sure to update the variables below with your specific details

# Variables
SOURCE_DIR="/path/to/your/website"  # Local directory containing your website files
DEST_DIR="/home/username/public_html"  # Destination directory on iFastNet
FTP_SERVER="ftp.your-ifastnet-domain.com"  # iFastNet FTP server
FTP_USER="your_ifastnet_username"  # iFastNet FTP username
FTP_PASS="your_ifastnet_password"  # iFastNet FTP password

# Function for error handling
handle_error() {
    echo "Error: $1"
    exit 1
}

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    handle_error "Source directory does not exist: $SOURCE_DIR"
fi

# Upload files using FTP
echo "Starting file transfer to iFastNet..."

# Using lftp for a more robust FTP transfer
lftp -u "$FTP_USER","$FTP_PASS" "$FTP_SERVER" << EOF
set ftp:ssl-allow no
mirror -R "$SOURCE_DIR" "$DEST_DIR" --verbose
bye
EOF

# Check if the transfer was successful
if [ $? -ne 0 ]; then
    handle_error "File transfer failed!"
else
    echo "File transfer completed successfully!"
fi

# Optional: Clear cache if applicable
# Uncomment the following lines if your website uses caching
# echo "Clearing cache..."
# /path/to/cache/clear_script.sh

echo "Website transfer to iFastNet hosting completed!"
```

### Instructions to Run the Script:
1. Update the variables at the beginning of the script with your specific details.
2. Make the script executable:
   ```bash
   chmod +x transfer_website.sh
   ```
3. Run the script:
   ```bash
   ./transfer_website.sh
   ```

### Note:
- Ensure you have `lftp` installed on your system for FTP transfers. You can install it via your package manager (e.g., `apt install lftp` for Debian/Ubuntu).
- This script assumes a Unix-like environment. Adjustments may be required for other systems.
