"""
Generated Code Metadata:
========================
Original URL: https://destiro.com
Prompt: How can I use Apache server directives to customize the description and file details shown in a directory listing?
Generated: DETERMINISTIC_4383a777bdc521b3
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
# Apache configuration for customizing directory listings
<Directory "/var/www/html">
    # Enable directory listings
    Options +Indexes

    # Customize the directory listing appearance
    IndexOptions FancyIndexing HTMLTable VersionSort NameWidth=* DescriptionWidth=* Charset=UTF-8

    # Add custom header and footer
    HeaderName /header.html
    ReadmeName /footer.html

    # Set default icon
    DefaultIcon /icons/unknown.png

    # Custom icons for specific file types
    AddIcon /icons/text.png .txt .md .log
    AddIcon /icons/archive.png .zip .tar .gz
    AddIcon /icons/image.png .jpg .png .gif
    AddIcon /icons/code.png .php .html .js .css
    AddIcon /icons/pdf.png .pdf

    # Custom file descriptions
    AddDescription "Text document" .txt
    AddDescription "Markdown file" .md
    AddDescription "Log file" .log
    AddDescription "ZIP archive" .zip
    AddDescription "TAR archive" .tar
    AddDescription "GZIP archive" .gz
    AddDescription "JPEG image" .jpg
    AddDescription "PNG image" .png
    AddDescription "GIF image" .gif
    AddDescription "PHP script" .php
    AddDescription "HTML document" .html
    AddDescription "JavaScript file" .js
    AddDescription "Stylesheet" .css
    AddDescription "PDF document" .pdf

    # Ignore certain files from listing
    IndexIgnore .htaccess *.bak ~* .gitignore

    # Custom sort order (name ascending)
    IndexOrderDefault Ascending Name
</Directory>
```
