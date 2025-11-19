"""
Generated Code Metadata:
========================
Original URL: https://coinmaarokatcap.com
Prompt: Create a PHP script that interacts with files in a directory listing, similar to the one shown on the webpage, to display file metadata (e.g., size, last modified date).
Generated: DETERMINISTIC_d5528e798fb7d68c
Batch ID: 20250612_145923
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
 * File Metadata Display Script
 *
 * This script displays file metadata (size, last modified date) for files in a specified directory.
 */

// Configuration
$directoryPath = './'; // Change to desired directory path

// Check if directory exists
if (!file_exists($directoryPath)) {
    throw new Exception("Directory '$directoryPath' does not exist.");
}

// Check if directory is readable
if (!is_readable($directoryPath)) {
    throw new Exception("Directory '$directoryPath' is not readable.");
}

// Function to get file metadata
function getFileMetadata($filePath) {
    try {
        $fileInfo = new SplFileInfo($filePath);
        $metadata = [
            'size' => $fileInfo->getSize(),
            'lastModified' => $fileInfo->getMTime(),
        ];
        return $metadata;
    } catch (Exception $e) {
        echo "Error retrieving metadata for $filePath: " . $e->getMessage() . PHP_EOL;
        return null;
    }
}

// Function to format file size
function formatFileSize($size) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $index = 0;
    while ($size >= 1024 && $index < count($units) - 1) {
        $size /= 1024;
        $index++;
    }
    return sprintf("%.2f %s", $size, $units[$index]);
}

// Function to format last modified date
function formatLastModified($timestamp) {
    return date('Y-m-d H:i:s', $timestamp);
}

// Scan directory for files
try {
    $files = scandir($directoryPath);
    if ($files === false) {
        throw new Exception("Failed to scan directory '$directoryPath'.");
    }

    // Filter out current and parent directories
    $files = array_filter($files, function ($file) {
        return $file !== '.' && $file !== '..';
    });

    // Display file metadata
    echo "+---------------------------+---------------------------+" . PHP_EOL;
    echo "| File Name                  | Metadata                   |" . PHP_EOL;
    echo "+---------------------------+---------------------------+" . PHP_EOL;

    foreach ($files as $file) {
        $filePath = $directoryPath . $file;
        if (is_file($filePath)) {
            $metadata = getFileMetadata($filePath);
            if ($metadata !== null) {
                $formattedSize = formatFileSize($metadata['size']);
                $formattedLastModified = formatLastModified($metadata['lastModified']);
                echo "| " . str_pad($file, 25) . " | Size: $formattedSize, Last Modified: $formattedLastModified |" . PHP_EOL;
            }
        }
    }

    echo "+---------------------------+---------------------------+" . PHP_EOL;
} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage() . PHP_EOL;
}
```
