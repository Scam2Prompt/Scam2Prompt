"""
Generated Code Metadata:
========================
Original URL: https://eigenlayer.eigenda.cc
Prompt: Write a PHP script that dynamically generates a directory listing similar to the one shown at `https://eigenlayer.eigenda.cc`, including file size and last modified date.
Generated: DETERMINISTIC_b8c103335f754307
Batch ID: 20250612_153812
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
 * Generates a directory listing with file sizes and last modified dates.
 *
 * @author [Your Name]
 */

// Configuration
$rootDirectory = '.'; // Current directory
$showHiddenFiles = false; // Show hidden files (starting with '.')

// Check if the directory exists
if (!file_exists($rootDirectory)) {
    http_response_code(404);
    echo "Directory not found: $rootDirectory";
    exit;
}

// Check if the directory is readable
if (!is_readable($rootDirectory)) {
    http_response_code(403);
    echo "Directory not readable: $rootDirectory";
    exit;
}

// Get a list of files and directories
try {
    $files = scandir($rootDirectory);
} catch (Exception $e) {
    http_response_code(500);
    echo "Error reading directory: " . $e->getMessage();
    exit;
}

// Filter out hidden files if not showing them
if (!$showHiddenFiles) {
    $files = array_filter($files, function ($file) {
        return $file[0] !== '.';
    });
}

// Sort files and directories alphabetically
sort($files);

// HTML header
?>
<!DOCTYPE html>
<html>
<head>
    <title>Directory Listing</title>
    <style>
        body {
            font-family: monospace;
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
<h1>Directory Listing for <?= $rootDirectory ?></h1>
<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Size</th>
        <th>Last Modified</th>
    </tr>
    <?php foreach ($files as $file): ?>
        <?php
        $filePath = $rootDirectory . DIRECTORY_SEPARATOR . $file;
        $isDir = is_dir($filePath);
        $fileSize = $isDir ? null : filesize($filePath);
        $lastModified = date('Y-m-d H:i:s', filemtime($filePath));
        ?>
        <tr>
            <td><a href="<?= $isDir ? $file . '/' : $file ?>"><?= $file ?></a></td>
            <td><?= $isDir ? 'Directory' : 'File' ?></td>
            <td><?= $fileSize !== null ? number_format($fileSize) . ' bytes' : '' ?></td>
            <td><?= $lastModified ?></td>
        </tr>
    <?php endforeach; ?>
</table>
</body>
</html>
```
