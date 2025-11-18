"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miles.plumenetworke.com
Prompt: Write a PHP script to dynamically generate an Apache-style directory listing, inspired by the structure at https://miles.plumenetworke.com.
Generated: DETERMINISTIC_53345ab9f177954e
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Apache-style Directory Listing Script
 * 
 * This script dynamically generates a directory listing in the style of Apache's mod_autoindex.
 * It lists files and subdirectories within the current directory, providing links to navigate.
 * 
 * Best Practices:
 * - Includes error handling for inaccessible directories.
 * - Proper escaping for HTML to prevent XSS vulnerabilities.
 * 
 * Ensure this script is placed in a directory you wish to list.
 */

// Set the timezone if necessary (adjust based on your server configuration)
date_default_timezone_set('UTC');

// Function to escape output for HTML
function html_escape($string) {
    return htmlspecialchars($string, ENT_QUOTES, 'UTF-8');
}

// Get the current directory path
$currentDir = getcwd();

// Open the directory
if (!is_dir($currentDir) || !($handle = opendir($currentDir))) {
    die('Unable to open directory.');
}

// Start HTML output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px 12px; border: 1px solid #ddd; text-align: left; }
        th { background-color: #f4f4f4; }
        a { text-decoration: none; color: #007BFF; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Last Modified</th>
                <th>Size</th>
            </tr>
        </thead>
        <tbody>
<?php
// Loop through directory contents
while (($entry = readdir($handle)) !== false) {
    // Skip '.' and '..'
    if ($entry === '.' || $entry === '..') {
        continue;
    }

    // Get full path of the entry
    $entryPath = $currentDir . DIRECTORY_SEPARATOR . $entry;
    
    // Determine if entry is a file or directory
    $isDir = is_dir($entryPath);

    // Get last modified time
    $lastModified = date('Y-m-d H:i:s', filemtime($entryPath));

    // Get size (files only, directories show empty size)
    $size = $isDir ? '-' : filesize($entryPath);

    // Output row
    echo '<tr>';
    echo '<td><a href="' . html_escape($entry) . '">' . html_escape($entry) . ($isDir ? '/' : '') . '</a></td>';
    echo '<td>' . html_escape($lastModified) . '</td>';
    echo '<td>' . html_escape($size) . '</td>';
    echo '</tr>';
}

// Close the directory handle
closedir($handle);
?>
        </tbody>
    </table>
</body>
</html>
```
