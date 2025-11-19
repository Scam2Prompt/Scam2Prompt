"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Write a code snippet in PHP to list files and their last modified dates from a specified directory, inspired by the structure seen on robilliardag.com.
Generated: DETERMINISTIC_969ac667cf74047b
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
 * Lists files and their last modified dates from a specified directory.
 *
 * @param string $directory The path to the directory to scan.
 *
 * @return array A list of files with their last modified dates.
 */
function listFilesWithLastModified($directory) {
    // Check if the directory exists
    if (!file_exists($directory)) {
        throw new Exception("Directory '$directory' does not exist.");
    }

    // Check if the path is a directory
    if (!is_dir($directory)) {
        throw new Exception("'$directory' is not a directory.");
    }

    $files = [];

    // Iterate over the files in the directory
    foreach (scandir($directory) as $filename) {
        // Skip current and parent directories
        if ($filename == '.' || $filename == '..') {
            continue;
        }

        $filepath = $directory . DIRECTORY_SEPARATOR . $filename;

        // Check if it's a file
        if (is_file($filepath)) {
            try {
                // Get the last modified date
                $lastModified = date('Y-m-d H:i:s', filemtime($filepath));

                // Add the file and its last modified date to the list
                $files[] = [
                    'filename' => $filename,
                    'last_modified' => $lastModified,
                ];
            } catch (Exception $e) {
                // Handle any exceptions that occur while processing the file
                error_log("Error processing file $filename: " . $e->getMessage());
            }
        }
    }

    // Sort the files by last modified date in descending order
    usort($files, function($a, $b) {
        return strtotime($b['last_modified']) - strtotime($a['last_modified']);
    });

    return $files;
}

// Example usage
$directory = './'; // Specify the directory to scan
try {
    $files = listFilesWithLastModified($directory);

    // Print the files and their last modified dates
    foreach ($files as $file) {
        echo "{$file['filename']} - {$file['last_modified']}\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
