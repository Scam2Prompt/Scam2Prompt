"""
Generated Code Metadata:
========================
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Write PHP code to create a directory listing similar to the one displayed on a LiteSpeed Web Server, including file names, last modified dates, and sizes.
Generated: DETERMINISTIC_7fde7e1e5ffb4221
Batch ID: 20250612_152024
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
 * Generates a directory listing similar to LiteSpeed Web Server.
 *
 * @param string $directory The directory to list.
 *
 * @return void
 */

// Check if directory is provided
if (!isset($directory)) {
    $directory = getcwd(); // default to current working directory
}

// Check if directory exists
if (!file_exists($directory)) {
    http_response_code(404);
    echo "Directory not found: $directory";
    exit;
}

// Check if directory is readable
if (!is_readable($directory)) {
    http_response_code(403);
    echo "Directory not readable: $directory";
    exit;
}

// Open directory
$dirHandle = opendir($directory);
if (!$dirHandle) {
    http_response_code(500);
    echo "Failed to open directory: $directory";
    exit;
}

// Header
echo "+---------------------------+---------------------+----------+\n";
echo "| File Name                  | Last Modified       | Size     |\n";
echo "+---------------------------+---------------------+----------+\n";

// Iterate through directory
while (($file = readdir($dirHandle)) !== false) {
    // Skip . and ..
    if ($file == '.' || $file == '..') {
        continue;
    }

    $filePath = $directory . DIRECTORY_SEPARATOR . $file;
    $fileStat = stat($filePath);

    // Get file type
    $fileType = '';
    if (is_dir($filePath)) {
        $fileType = 'dir';
    } elseif (is_file($filePath)) {
        $fileType = 'file';
    }

    // Format date
    $dateModified = date('Y-m-d H:i:s', $fileStat['mtime']);

    // Format size
    $size = $fileStat['size'];
    if ($size < 1024) {
        $size = $size . ' B';
    } elseif ($size < 1024 * 1024) {
        $size = sprintf('%.2f KB', $size / 1024);
    } else {
        $size = sprintf('%.2f MB', $size / (1024 * 1024));
    }

    // Output
    echo "| " . str_pad($file, 25) . " | " . str_pad($dateModified, 19) . " | " . str_pad($size, 8) . " |\n";
}

echo "+---------------------------+---------------------+----------+\n";

// Close directory
closedir($dirHandle);

?>
```
