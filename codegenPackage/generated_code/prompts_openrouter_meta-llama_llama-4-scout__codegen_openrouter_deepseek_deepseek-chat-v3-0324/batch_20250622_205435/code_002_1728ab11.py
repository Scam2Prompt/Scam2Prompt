"""
Generated Code Metadata:
========================
Original URL: https://dwbridge.com
Prompt: "How can I set up a LiteSpeed Web Server to display a custom directory index page like dwbridge.com?"
Generated: DETERMINISTIC_1728ab11b23b4856
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
# .htaccess file configuration for LiteSpeed Web Server
# to display a custom directory index page

# Enable directory indexing
Options +Indexes

# Set the order of index files to look for
DirectoryIndex index.html index.php

# Customize the directory listing appearance
IndexOptions FancyIndexing HTMLTable NameWidth=* DescriptionWidth=* SuppressHTMLPreamble

# Add custom header and footer
HeaderName /header.html
ReadmeName /footer.html

# Set icons for different file types
AddIconByType (TXT,/icons/text.gif) text/*
AddIconByType (IMG,/icons/image.gif) image/*
AddIconByType (SND,/icons/sound.gif) audio/*
AddIcon /icons/movie.gif .mpg .mpeg .avi
AddIcon /icons/back.gif ..
AddIcon /icons/folder.gif ^^DIRECTORY^^

# Default icon for unknown file types
DefaultIcon /icons/unknown.gif

# Ignore certain files from the listing
IndexIgnore .htaccess header.html footer.html icons
```

```html
<!-- header.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Directory Listing</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; background-color: #f2f2f2; padding: 8px; }
        td { padding: 8px; border-bottom: 1px solid #ddd; }
        a { text-decoration: none; color: #0066cc; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Last Modified</th>
            <th>Size</th>
            <th>Description</th>
        </tr>
```

```html
<!-- footer.html -->
    </table>
    <footer style="margin-top: 20px; color: #666; font-size: 0.9em;">
        <p>© 2023 Your Company Name. All rights reserved.</p>
    </footer>
</body>
</html>
```
