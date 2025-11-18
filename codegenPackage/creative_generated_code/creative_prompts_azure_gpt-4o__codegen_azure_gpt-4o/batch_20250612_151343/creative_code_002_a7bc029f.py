"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-game7.xyz
Prompt: Provide an example of an Apache configuration file that displays a custom success message when the server is accessed.
Generated: DETERMINISTIC_a7bc029f86dc5011
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```apache
# Apache Configuration File: Custom Success Message
# This configuration serves a custom success message when the server is accessed.
# Place this configuration in your Apache virtual host file or main configuration file.

<VirtualHost *:80>
    # Server Admin email for error notifications
    ServerAdmin admin@example.com

    # Server Name or domain (ensure DNS points to this server)
    ServerName www.example.com
    ServerAlias example.com

    # Document root directory where the website files are stored
    DocumentRoot /var/www/html

    # Custom success message to be displayed on the root path of the server
    <Location />
        # Set custom response headers
        Header set Content-Type "text/plain"

        # Use mod_rewrite to rewrite the root path request to a custom message
        RewriteEngine On
        RewriteRule ^$ /success-message.txt [L]
    </Location>

    # Define the custom success message file
    Alias /success-message.txt /var/www/html/success-message.txt

    # Provide permissions for the file
    <Files "success-message.txt">
        Require all granted
    </Files>

    # Error handling: Log errors and access logs
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    # Ensure directory permissions for security
    <Directory /var/www/html>
        Options -Indexes +FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>

# Create the success-message.txt file in the /var/www/html directory
# with the following content:
# "Success! The server is functioning as expected."
```
