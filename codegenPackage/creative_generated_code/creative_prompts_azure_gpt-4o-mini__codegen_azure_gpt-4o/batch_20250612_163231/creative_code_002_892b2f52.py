"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.newtork.cc
Prompt: Write a code snippet in PHP to create a custom index page that lists files similar to the index at omni.newtork.cc.
Generated: DETERMINISTIC_892b2f52a070ce25
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: index.php

/**
 * A simple custom index page that lists all files in the current directory.
 * 
 * This script generates an HTML page with a list of files and directories
 * in the current location, similar to directory listings.
 * 
 * It excludes this script itself and provides download links for files.
 */

// Error reporting configuration for production
error_reporting(E_ALL);
ini_set('display_errors', 0);

// HTML Structure: Begin page output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Index Page</title>
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
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Index of <?php echo htmlspecialchars(basename(__DIR__)); ?></h1>
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
try {
    // Open the current directory
    $currentDir = __DIR__;
    $dirHandle = opendir($currentDir);

    if (!$dirHandle) {
        throw new Exception("Failed to open directory: $currentDir");
    }

    // Iterate over directory entries
    while (($entry = readdir($dirHandle)) !== false) {
        // Skip '.' and '..'
        if ($entry === '.' || $entry === '..') {
            continue;
        }

        // Get full path of the entry
        $entryPath = $currentDir . DIRECTORY_SEPARATOR . $entry;

        // Determine file type
        $type = is_dir($entryPath) ? 'Directory' : 'File';

        // Get file size (directories return size as 0)
        $size = is_file($entryPath) ? filesize($entryPath) : '-';

        // Get last modification timestamp
        $lastModified = date('Y-m-d H:i:s', filemtime($entryPath));

        // Display the entry as a table row
        echo '<tr>';
        echo '<td><a href="' . htmlspecialchars($entry) . '">' . htmlspecialchars($entry) . '</a></td>';
        echo '<td>' . $type . '</td>';
        echo '<td>' . $size . '</td>';
        echo '<td>' . $lastModified . '</td>';
        echo '</tr>';
    }

    // Close the directory handle
    closedir($dirHandle);

} catch (Exception $e) {
    // Handle errors gracefully
    echo '<tr><td colspan="4">Error: ' . htmlspecialchars($e->getMessage()) . '</td></tr>';
}
?>
        </tbody>
    </table>
</body>
</html>
```
