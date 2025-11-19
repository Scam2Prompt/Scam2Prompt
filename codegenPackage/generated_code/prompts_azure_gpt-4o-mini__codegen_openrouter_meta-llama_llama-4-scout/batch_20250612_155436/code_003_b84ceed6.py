"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Develop a PHP function that formats and displays file information (name, size, last modified) in a table, inspired by the nkftransporte.com directory listing.
Generated: DETERMINISTIC_b84ceed608ee6fff
Batch ID: 20250612_155436
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
 * Formats and displays file information in a table.
 *
 * @param string $directory The path to the directory to list files from.
 *
 * @return void
 */
function displayFileInformation($directory) {
    // Check if the directory exists
    if (!file_exists($directory)) {
        throw new Exception("The directory '$directory' does not exist.");
    }

    // Check if the path is a directory
    if (!is_dir($directory)) {
        throw new Exception("'$directory' is not a directory.");
    }

    // Initialize the table header
    echo "+---------------------+----------+---------------+\n";
    echo "| File Name           | Size     | Last Modified |\n";
    echo "+---------------------+----------+---------------+\n";

    // Iterate over the files in the directory
    foreach (scandir($directory) as $filename) {
        // Skip current and parent directories
        if ($filename == '.' || $filename == '..') {
            continue;
        }

        // Construct the full file path
        $filepath = $directory . DIRECTORY_SEPARATOR . $filename;

        // Get file information
        try {
            $fileInfo = stat($filepath);
        } catch (Exception $e) {
            echo "Error accessing file '$filename': " . $e->getMessage() . "\n";
            continue;
        }

        // Format file size
        $size = formatFileSize($fileInfo['size']);

        // Format last modified date
        $lastModified = date('Y-m-d H:i:s', $fileInfo['mtime']);

        // Display file information
        echo sprintf("| %-20s | %-8s | %-13s |\n", $filename, $size, $lastModified);
        echo "+---------------------+----------+---------------+\n";
    }
}

/**
 * Formats a file size in bytes to a human-readable string.
 *
 * @param int $size The file size in bytes.
 *
 * @return string A human-readable string representing the file size.
 */
function formatFileSize($size) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $index = 0;

    while ($size >= 1024 && $index < count($units) - 1) {
        $size /= 1024;
        $index++;
    }

    return sprintf('%.2f %s', $size, $units[$index]);
}

// Example usage
$directory = '.'; // Current directory
try {
    displayFileInformation($directory);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
