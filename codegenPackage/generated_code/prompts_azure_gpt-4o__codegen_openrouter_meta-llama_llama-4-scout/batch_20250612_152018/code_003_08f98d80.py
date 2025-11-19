"""
Generated Code Metadata:
========================
Original URL: https://refconegypt.net
Prompt: Generate a script using PHP to dynamically display a directory listing with file details, inspired by the structure on https://refconegypt.net.
Generated: DETERMINISTIC_08f98d80387ea81f
Batch ID: 20250612_152018
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
 * Dynamically displays a directory listing with file details.
 * 
 * @author [Your Name]
 */

// Configuration
$rootDir = './'; // root directory to list
$maxFileSize = 10; // max file size in MB to display

// Check if directory exists
if (!file_exists($rootDir)) {
    throw new Exception("Directory '$rootDir' does not exist.");
}

// Check if directory is readable
if (!is_readable($rootDir)) {
    throw new Exception("Directory '$rootDir' is not readable.");
}

// Get directory contents
try {
    $dirContents = scandir($rootDir);
} catch (Exception $e) {
    throw new Exception("Error reading directory '$rootDir': " . $e->getMessage());
}

// Filter out . and ..
$dirContents = array_filter($dirContents, function($item) {
    return $item !== '.' && $item !== '..';
});

// Sort directory contents
sort($dirContents);

// HTML header
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        /* Simple styling */
        body {
            font-family: Arial, sans-serif;
        }
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Size</th>
            <th>Modified</th>
        </tr>
        <?php
        foreach ($dirContents as $item) {
            $itemPath = $rootDir . $item;
            $fileInfo = new SplFileInfo($itemPath);

            // Get file size in MB
            $fileSize = $fileInfo->getSize() / (1024 * 1024);
            if ($fileSize > $maxFileSize) {
                continue; // skip large files
            }

            // Get file modification date
            $modifiedDate = $fileInfo->getMTime();
            $modifiedDateStr = date('Y-m-d H:i:s', $modifiedDate);

            // Determine file type
            $fileType = $fileInfo->isDir() ? 'Directory' : 'File';

            // Display file info
            ?>
            <tr>
                <td><?= $item ?></td>
                <td><?= $fileType ?></td>
                <td><?= number_format($fileSize, 2) ?> MB</td>
                <td><?= $modifiedDateStr ?></td>
            </tr>
            <?php
        }
        ?>
    </table>
</body>
</html>
```
