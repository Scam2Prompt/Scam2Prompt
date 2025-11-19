"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Provide an example of configuring a LiteSpeed Web Server to display directory listings with custom formatting, including file metadata such as size and modification date.
Generated: DETERMINISTIC_39759df04c01530d
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**LiteSpeed Web Server Configuration Example**
====================================================

**Directory Listing Configuration**
---------------------------------

```bash
# Enable directory listings
<Directory /path/to/directory>
    Options +Indexes

    # Set custom directory listing template
    DirectoryIndex disabled
    AddHandler lsphp-file .php

    # LiteSpeed directory listing configuration
    <IfModule litespeed.c>
        LitespeedDirListing on
        LitespeedDirListingTemplate /path/to/custom/dirlisting.tpl
    </IfModule>
</Directory>
```

**Custom Directory Listing Template**
--------------------------------------

```smarty
{* dirlisting.tpl *}

<!DOCTYPE html>
<html>
<head>
    <title>Directory Listing</title>
    <style>
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Size</th>
            <th>Last Modified</th>
        </tr>
        {foreach $files as $file}
        <tr>
            <td><a href="{$file.url}">{$file.name}</a></td>
            <td>{$file.size}</td>
            <td>{$file.modified}</td>
        </tr>
        {/foreach}
    </table>
</body>
</html>
```

**LiteSpeed Configuration File (lsws.conf)**
-------------------------------------------

```bash
# lsws.conf

# Enable directory listings
<VirtualHost *:80>
    <Directory /path/to/directory>
        enableDirectoryListing 1
        directoryListingTemplate /path/to/custom/dirlisting.tpl
    </Directory>
</VirtualHost>
```

**PHP Script for Directory Listing (Optional)**
-----------------------------------------------

```php
<?php
/**
 * Directory listing script
 */

// Set directory path
$dirPath = '/path/to/directory';

// Check if directory exists
if (!file_exists($dirPath)) {
    http_response_code(404);
    echo "Directory not found.";
    exit;
}

// Get directory contents
$files = scandir($dirPath);

// Create array to store file metadata
$fileMetadata = [];

// Loop through directory contents
foreach ($files as $file) {
    // Skip current and parent directories
    if ($file == '.' || $file == '..') {
        continue;
    }

    // Get file path
    $filePath = $dirPath . '/' . $file;

    // Get file metadata
    $fileSize = filesize($filePath);
    $fileModified = date('Y-m-d H:i:s', filemtime($filePath));

    // Add file metadata to array
    $fileMetadata[] = [
        'name' => $file,
        'size' => $fileSize,
        'modified' => $fileModified,
        'url' => $dirPath . '/' . $file,
    ];
}

// Sort file metadata by name
usort($fileMetadata, function($a, $b) {
    return strcmp($a['name'], $b['name']);
});

// Render directory listing template
$template = new Smarty();
$template->assign('files', $fileMetadata);
$template->display('dirlisting.tpl');
```

**Error Handling**
------------------

```php
try {
    // Code to generate directory listing
} catch (Exception $e) {
    http_response_code(500);
    echo "Error generating directory listing: " . $e->getMessage();
}
```
