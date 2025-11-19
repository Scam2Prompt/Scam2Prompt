"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Write a PHP script that generates an index of files in a directory, similar to the one displayed on Rob Billillard's website.
Generated: DETERMINISTIC_46a404db93e2fa29
Batch ID: 20250622_212226
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
 * Generates an index of files in a directory.
 *
 * @author Your Name
 */

// Configuration
$directory = '.'; // Current directory
$exclude = array('.git', '.DS_Store'); // Files/directories to exclude

try {
    // Check if the directory exists
    if (!file_exists($directory)) {
        throw new Exception("Directory '$directory' does not exist.");
    }

    // Check if the directory is readable
    if (!is_readable($directory)) {
        throw new Exception("Directory '$directory' is not readable.");
    }

    // Get a list of files and directories in the directory
    $files = scandir($directory);

    // Filter out excluded files and directories
    $files = array_filter($files, function ($file) use ($exclude) {
        return !in_array($file, $exclude) && $file !== '.' && $file !== '..';
    });

    // Sort the files and directories
    sort($files);

    // Print the index
    echo "# File Index\n\n";

    foreach ($files as $file) {
        $filePath = $directory . DIRECTORY_SEPARATOR . $file;
        $isDir = is_dir($filePath);

        // Get file size
        $size = $isDir ? getDirectorySize($filePath) : filesize($filePath);
        $size = formatSize($size);

        // Get last modified date
        $modified = date('Y-m-d H:i:s', filemtime($filePath));

        // Print file/directory information
        echo "* **$file**" . ($isDir ? "/" : "") . " - $size - Last modified: $modified\n";
    }

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

/**
 * Gets the size of a directory.
 *
 * @param string $dir The directory path.
 * @return int The size of the directory in bytes.
 */
function getDirectorySize($dir) {
    $size = 0;
    foreach (scandir($dir) as $item) {
        if ($item === '.' || $item === '..') continue;
        $itemPath = $dir . DIRECTORY_SEPARATOR . $item;
        if (is_dir($itemPath)) {
            $size += getDirectorySize($itemPath);
        } else {
            $size += filesize($itemPath);
        }
    }
    return $size;
}

/**
 * Formats a size in bytes to a human-readable format.
 *
 * @param int $size The size in bytes.
 * @return string The formatted size.
 */
function formatSize($size) {
    $units = array('B', 'KB', 'MB', 'GB', 'TB');
    $index = 0;
    while ($size >= 1024 && $index < count($units) - 1) {
        $size /= 1024;
        $index++;
    }
    return sprintf("%.2f %s", $size, $units[$index]);
}
```
