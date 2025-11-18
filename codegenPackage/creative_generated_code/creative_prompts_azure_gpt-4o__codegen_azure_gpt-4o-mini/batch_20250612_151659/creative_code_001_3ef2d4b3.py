"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Explain how to configure a web server to properly serve files from a "cgi-bin/" directory, ensuring security and functionality.
Generated: DETERMINISTIC_3ef2d4b3a0b3ac2f
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# This script configures an Apache web server to serve files from the cgi-bin directory securely.

# Define the location of the Apache configuration file.
APACHE_CONF_FILE="/etc/apache2/sites-available/000-default.conf"

# Backup the original configuration file for safety.
cp "$APACHE_CONF_FILE" "${APACHE_CONF_FILE}.bak" || {
    echo "Error: Unable to backup the configuration file."
    exit 1
}

# Function to add CGI configuration to Apache
configure_cgi_bin() {
    # Check if the cgi-bin directory exists
    if [ ! -d "/usr/lib/cgi-bin" ]; then
        echo "Creating cgi-bin directory."
        mkdir -p /usr/lib/cgi-bin || {
            echo "Error: Unable to create cgi-bin directory."
            exit 1
        }
    fi

    # Update the Apache configuration to include CGI settings
    echo "Configuring Apache to serve CGI scripts."

    # Append CGI configuration to the Apache config file
    cat <<EOL >> "$APACHE_CONF_FILE"

# CGI configuration for cgi-bin
<Directory "/usr/lib/cgi-bin">
    AllowOverride None
    Options +ExecCGI
    AddHandler cgi-script .cgi .pl .py
    Require all granted
</Directory>

EOL

    # Restart the Apache service to apply changes
    echo "Restarting Apache service to apply changes."
    systemctl restart apache2 || {
        echo "Error: Unable to restart Apache service."
        exit 1
    }

    echo "CGI configuration completed successfully."
}

# Run the CGI configuration function
configure_cgi_bin
```

```python
# Example CGI script to be placed in the cgi-bin directory.
#!/usr/bin/env python3
import cgi
import os

# Set the content type to text/html
print("Content-Type: text/html")    # HTML is following
print()                              # End of headers

# Simple HTML output
print("<html><head><title>CGI Example</title></head>")
print("<body><h1>CGI Script Output</h1>")
print("<p>Hello, World! This is a CGI script.</p>")
print("</body></html>")
```

Make sure to place the above Python script in the `/usr/lib/cgi-bin/` directory and give it execute permissions using the command: 

```bash
chmod +x /usr/lib/cgi-bin/your_script.py
```

This configuration provides a basic setup for serving CGI scripts while ensuring security through the proper Apache configurations.
