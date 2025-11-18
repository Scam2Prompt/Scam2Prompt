"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://destiro.com
Prompt: How can I use Apache server directives to customize the description and file details shown in a directory listing?
Generated: DETERMINISTIC_4383a777bdc521b3
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```apache
# Enable the use of directory indexing
Options +Indexes

# Customize the appearance of the directory listing
IndexOptions FancyIndexing # Enables enhanced indexing options
IndexOptions +IgnoreCase # Makes sorting case insensitive
IndexOptions +FoldersFirst # Directories will be listed before files

# Set a custom header for the directory listing
HeaderName HEADER.html # Use a custom HTML file for the header

# Set a custom footer for the directory listing
ReadmeName README.html # Use a custom HTML file for the footer

# Customize the description of files
AddDescription "This is a document file" .doc
AddDescription "This is a PDF document" .pdf
AddDescription "This is an image file" .jpg .jpeg .png
AddDescription "This is a text file" .txt

# Enable the use of custom icons for files
IconHeight 16 # Set height for icons
IconWidth 16 # Set width for icons
DefaultIcon /icons/default.png # Default icon for files without custom icons
DirIcon /icons/folder.png # Custom icon for directories

# Error handling for missing files
ErrorDocument 404 /error/404.html # Custom error page for 404 Not Found

# Allow users to view the directory with a custom file structure
Options +MultiViews # Enable content negotiation
```
