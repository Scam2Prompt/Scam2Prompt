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
# Apache configuration file for customizing directory listings
# Save this configuration in /etc/apache2/sites-available/000-default.conf or your specific site configuration file

<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html

    # Enable directory listing for a specific directory
    <Directory /var/www/html/files>
        Options +Indexes

        # Customizing the directory listing page
        IndexOptions +FancyIndexing +FoldersFirst +IgnoreCase
        HeaderName HEADER.html
        ReadmeName README.html

        # Enable the use of a custom file description
        AddDescription "Logo file" logo.png
        AddDescription "User guide document" user_guide.pdf
        AddDescription "Sample image" sample_image.jpg

        # Security settings
        AllowOverride None
        Require all granted
    </Directory>

    # Error handling
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    # Include the default error documents
    ErrorDocument 403 "Access denied!"
    ErrorDocument 404 "Page not found!"
</VirtualHost>
```

```html
<!-- HEADER.html -->
<h1>Directory Listing</h1>
<p>Welcome to the custom directory listing page.</p>
```

```html
<!-- README.html -->
<p>This directory contains various files. Below you will find a list of files with their descriptions.</p>
``` 

### Note:
- Ensure that the files `HEADER.html` and `README.html` are placed in the `/var/www/html/files` directory.
- After making changes to the configuration, restart Apache with the following command:
  ```bash
  sudo systemctl restart apache2
  ```
