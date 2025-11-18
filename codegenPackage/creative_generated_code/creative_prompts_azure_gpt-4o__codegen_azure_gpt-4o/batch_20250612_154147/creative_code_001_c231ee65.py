"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abset.org
Prompt: Provide a configuration example for an Apache server running on Debian to customize the directory listing page, including adding descriptions for files like "logo.png."
Generated: DETERMINISTIC_c231ee65ef71cbcf
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```apache
# Apache Configuration Example for Customizing Directory Listings
# Save this file as `/etc/apache2/conf-available/custom-directory-listing.conf`
# Enable it using `sudo a2enconf custom-directory-listing`

<IfModule mod_autoindex.c>
    # Enable directory listings
    Options +Indexes

    # Customize the header and footer for directory listings
    HeaderName /custom-header.html
    ReadmeName /custom-footer.html

    # Enable file descriptions
    IndexOptions DescriptionWidth=*

    # Specify custom file descriptions
    # Add descriptions for specific files
    IndexIgnore .htaccess
    AddDescription "Company Logo" logo.png
    AddDescription "Sample Document" sample.pdf
    AddDescription "Backup File" backup.zip
    
    # Define sorting order (name ascending)
    IndexOrderDefault Ascending Name
</IfModule>

# Ensure the custom header and footer files exist and are readable
Alias /custom-header.html /var/www/html/custom-header.html
Alias /custom-footer.html /var/www/html/custom-footer.html

<Directory "/var/www/html">
    # Allow access to the directory
    Require all granted

    # Specify default directory index file
    DirectoryIndex index.html
</Directory>

# Error handling
ErrorDocument 403 /error/403.html
ErrorDocument 404 /error/404.html
ErrorDocument 500 /error/500.html
```

### Additional Notes:
1. After placing this configuration file, make sure you reload the Apache service to apply changes:
   ```
   sudo systemctl reload apache2
   ```

2. Create the `custom-header.html` and `custom-footer.html` files in `/var/www/html` with custom HTML content for the directory listing.
