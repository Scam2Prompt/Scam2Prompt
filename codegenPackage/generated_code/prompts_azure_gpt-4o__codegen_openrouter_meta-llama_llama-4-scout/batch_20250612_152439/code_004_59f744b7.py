"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Write a PHP script that scans a directory and outputs file metadata (e.g., name, size, last modified date) in a format similar to the listing on nkftransporte.com.
Generated: DETERMINISTIC_59f744b7c1606ccb
Batch ID: 20250612_152439
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
 * Scans a directory and outputs file metadata.
 *
 * @author [Your Name]
 */

// Configuration
$directoryPath = './'; // directory to scan
$maxFileSizeMB = 1024; // max file size to display (in MB)

// Check if directory exists
if (!file_exists($directoryPath)) {
    throw new Exception("Directory '$directoryPath' does not exist.");
}

// Check if directory is readable
if (!is_readable($directoryPath)) {
    throw new Exception("Directory '$directoryPath' is not readable.");
}

// Initialize output
$files = [];

// Scan directory
try {
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directoryPath));
    foreach ($iterator as $file) {
        if ($file->isFile()) {
            $fileSize = $file->getSize() / (1024 * 1024); // convert to MB
            if ($fileSize <= $maxFileSizeMB) {
                $files[] = [
                    'name' => $file->getFilename(),
                    'size' => number_format($fileSize, 2) . ' MB',
                    'lastModified' => date('Y-m-d H:i:s', $file->getMTime()),
                    'path' => $file->getPathname(),
                ];
            }
        }
    }
} catch (Exception $e) {
    echo "Error scanning directory: " . $e->getMessage() . PHP_EOL;
    exit(1);
}

// Output file metadata
if (!empty($files)) {
    echo "+---------------------+----------+---------------+----------------------------------------+" . PHP_EOL;
    echo "| File Name           | Size     | Last Modified | Path                                   |" . PHP_EOL;
    echo "+---------------------+----------+---------------+----------------------------------------+" . PHP_EOL;
    foreach ($files as $file) {
        printf("| %-20s | %-8s | %-13s | %-40s |" . PHP_EOL,
               $file['name'],
               $file['size'],
               $file['lastModified'],
               $file['path']);
    }
    echo "+---------------------+----------+---------------+----------------------------------------+" . PHP_EOL;
} else {
    echo "No files found in directory '$directoryPath'." . PHP_EOL;
}
```
