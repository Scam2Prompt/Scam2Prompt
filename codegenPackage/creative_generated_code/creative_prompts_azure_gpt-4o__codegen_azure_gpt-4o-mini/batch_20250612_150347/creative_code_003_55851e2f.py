"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abelltodoit.com.au
Prompt: Recommend a method to secure directories like `cgi-bin` on a LiteSpeed Web Server, as seen on https://abelltodoit.com.au.
Generated: DETERMINISTIC_55851e2f871561bd
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# This script provides a method to secure the `cgi-bin` directory on a LiteSpeed Web Server
# by utilizing `.htaccess` for access control and security measures.

# Ensure you are in the root directory of your web server
cd /path/to/your/web/root || {
    echo "Failed to change directory to web root."
    exit 1
}

# Create or modify the .htaccess file in the cgi-bin directory
cat << EOF > cgi-bin/.htaccess
# Deny access to the cgi-bin directory from all users
Order Deny,Allow
Deny from all

# Allow access only from specific IP addresses (replace with your own)
# Allow from 192.168.1.1
# Allow from 203.0.113.0

# Enable password protection (optional)
AuthType Basic
AuthName "Restricted Access"
AuthUserFile /path/to/.htpasswd
Require valid-user
EOF

# Create a .htpasswd file for storing authorized users (if using password protection)
htpasswd -c /path/to/.htpasswd username || {
    echo "Failed to create .htpasswd file. Ensure the htpasswd command is available and permissions are correct."
    exit 1
}

echo "Secured the cgi-bin directory successfully."
```

### Notes:
- Replace `/path/to/your/web/root` with the actual path to your web server's root directory.
- Uncomment and replace the IP addresses with the ones you want to allow access, if needed.
- Ensure that the path to `.htpasswd` is writable by the web server process and not publicly accessible.
- The `htpasswd` command may require installation of Apache utilities if not already available.
