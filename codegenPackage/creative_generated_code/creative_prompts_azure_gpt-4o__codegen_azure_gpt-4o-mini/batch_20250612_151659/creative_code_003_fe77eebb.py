"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: How can you set up permissions for the "cgi-bin/" directory to allow execution of scripts while preventing unauthorized access?
Generated: DETERMINISTIC_fe77eebbc9a71efa
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

# Define the cgi-bin directory path
CGI_BIN_DIR="/path/to/your/cgi-bin"

# Function to set up permissions on the cgi-bin directory
setup_cgi_bin_permissions() {
    # Check if the directory exists
    if [ ! -d "$CGI_BIN_DIR" ]; then
        echo "Error: Directory $CGI_BIN_DIR does not exist."
        exit 1
    fi

    # Set the owner of the directory to the web server user
    # Replace 'www-data' with the user that your web server runs as
    chown -R www-data:www-data "$CGI_BIN_DIR"
    
    # Set permissions to allow execution of scripts
    # 755 allows the owner to read/write/execute, and others to read/execute
    chmod 755 "$CGI_BIN_DIR"

    # Set permissions for files inside the cgi-bin directory
    find "$CGI_BIN_DIR" -type f -exec chmod 755 {} \;

    echo "Permissions for $CGI_BIN_DIR have been set successfully."
}

# Execute the function to set up permissions
setup_cgi_bin_permissions
```

Make sure to replace `"/path/to/your/cgi-bin"` with the actual path of your `cgi-bin` directory and adjust the ownership to match your server's configuration.
