"""
Generated Code Metadata:
========================
Original URL: https://mfcsons.com
Prompt: How can I properly configure and secure CGI scripts on my website, specifically on a server that uses a directory structure like the one shown on mfcsons.com?
Generated: DETERMINISTIC_37a1ab67faf29c00
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Secure CGI Script Configuration for mfcsons.com-like directory structure

This script demonstrates secure CGI configuration practices including:
- Proper file permissions
- Input validation
- Output sanitization
- Error handling
"""

import os
import cgi
import cgitb
import sys
from pathlib import Path

# Enable detailed error reporting for development (disable in production)
cgitb.enable()

# Configuration
CGI_BIN_DIR = "/var/www/mfcsons.com/cgi-bin"  # Example directory
LOG_FILE = "/var/log/cgi_errors.log"

def setup_environment():
    """Configure secure environment for CGI execution"""
    try:
        # Set secure umask
        os.umask(0o077)
        
        # Verify CGI directory exists and is secure
        cgi_dir = Path(CGI_BIN_DIR)
        if not cgi_dir.exists():
            raise FileNotFoundError(f"CGI directory {CGI_BIN_DIR} not found")
            
        if cgi_dir.stat().st_mode & 0o777 != 0o750:
            raise PermissionError(f"Insecure permissions on {CGI_BIN_DIR}")
            
        # Change to CGI directory
        os.chdir(CGI_BIN_DIR)
        
    except Exception as e:
        log_error(f"Environment setup failed: {str(e)}")
        sys.exit(1)

def log_error(message):
    """Log errors securely"""
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(f"{os.getpid()}: {message}\n")
    except IOError:
        sys.stderr.write(f"Failed to log error: {message}\n")

def sanitize_input(input_str):
    """Sanitize user input to prevent XSS and injection attacks"""
    if not input_str:
        return ""
    return cgi.escape(input_str)

def validate_form_data(form):
    """Validate and sanitize form data"""
    validated = {}
    for field in form:
        if field not in ['name', 'email', 'message']:  # Allowed fields
            continue
        value = form.getvalue(field, '')
        validated[field] = sanitize_input(value)
    return validated

def main():
    """Main CGI handler"""
    print("Content-Type: text/html\n")
    
    try:
        setup_environment()
        
        form = cgi.FieldStorage()
        validated_data = validate_form_data(form)
        
        # Process validated data securely
        response = f"""
        <html>
        <head><title>Form Submission</title></head>
        <body>
            <h1>Form Received</h1>
            <p>Name: {validated_data.get('name', '')}</p>
            <p>Email: {validated_data.get('email', '')}</p>
            <p>Message: {validated_data.get('message', '')}</p>
        </body>
        </html>
        """
        print(response)
        
    except Exception as e:
        log_error(f"CGI execution failed: {str(e)}")
        print("<h1>500 Internal Server Error</h1>")
        print("<p>An error occurred while processing your request.</p>")

if __name__ == "__main__":
    main()
```

```bash
#!/bin/bash
# Server configuration for secure CGI scripts

# Set proper permissions for CGI directory
chmod 750 /var/www/mfcsons.com/cgi-bin
chown www-data:www-data /var/www/mfcsons.com/cgi-bin

# Create secure log file
touch /var/log/cgi_errors.log
chmod 640 /var/log/cgi_errors.log
chown www-data:adm /var/log/cgi_errors.log

# Apache configuration snippet for CGI security
cat > /etc/apache2/conf-available/cgi-security.conf << 'EOL'
<Directory "/var/www/mfcsons.com/cgi-bin">
    Options +ExecCGI -Indexes -Includes
    AddHandler cgi-script .cgi .py
    AllowOverride None
    Require all granted
    
    # Security headers
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Frame-Options "DENY"
    Header always set Content-Security-Policy "default-src 'self'"
    
    # Limit HTTP methods
    <LimitExcept GET POST>
        Deny from all
    </LimitExcept>
</Directory>
EOL

# Enable the configuration
a2enconf cgi-security
systemctl reload apache2
```
