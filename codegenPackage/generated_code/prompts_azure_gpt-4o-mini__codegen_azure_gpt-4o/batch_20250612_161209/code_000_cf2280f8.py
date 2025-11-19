"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Generate a PHP script that retrieves and displays the contents of a directory similar to the index found on robilliardag.com.
Generated: DETERMINISTIC_cf2280f8475eea3c
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Directory Listing Script
 * 
 * This script retrieves and displays the contents of a directory
 * in a clean and user-friendly format. It mimics a basic directory
 * index similar to what is found on some web servers.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Set the directory to be listed (default is the current directory)
$directory = __DIR__;

// Error handling: Check if the directory exists and is readable
if (!is_dir($directory) || !is_readable($directory)) {
    http_response_code(500);
    echo "Error: Unable to access the directory.";
    exit;
}

// Retrieve the list of files and directories
$items = scandir($directory);

// Error handling: Check if scandir succeeded
if ($items === false) {
    http_response_code(500);
    echo "Error: Unable to read the directory contents.";
    exit;
}

// Helper function to format file sizes
function formatFileSize($bytes) {
    if ($bytes < 1024) return $bytes . ' B';
    if ($bytes < 1048576) return round($bytes / 1024, 2) . ' KB';
    if ($bytes < 1073741824) return round($bytes / 1048576, 2) . ' MB';
    return round($bytes / 1073741824, 2) . ' GB';
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
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        a {
            text-decoration: none;
            color: #007BFF;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Loop through each item in the directory
            foreach ($items as $item) {
                // Skip the current and parent directory links
                if ($item === '.' || $item === '..') {
                    continue;
                }

                // Get the full path of the item
                $itemPath = $directory . DIRECTORY_SEPARATOR . $item;

                // Determine if the item is a file or directory
                $isDir = is_dir($itemPath);
                $type = $isDir ? 'Directory' : 'File';

                // Get the file size (if it's a file)
                $size = $isDir ? '-' : formatFileSize(filesize($itemPath));

                // Get the last modified time
                $lastModified = date("Y-m-d H:i:s", filemtime($itemPath));

                // Display the item in the table
                echo '<tr>';
                echo '<td><a href="' . htmlspecialchars($item) . '">' . htmlspecialchars($item) . '</a></td>';
                echo '<td>' . $type . '</td>';
                echo '<td>' . $size . '</td>';
                echo '<td>' . $lastModified . '</td>';
                echo '</tr>';
            }
            ?>
        </tbody>
    </table>
</body>
</html>
```
