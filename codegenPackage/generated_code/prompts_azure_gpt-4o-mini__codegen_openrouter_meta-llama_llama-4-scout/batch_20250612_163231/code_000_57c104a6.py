"""
Generated Code Metadata:
========================
Original URL: https://omni.newtork.cc
Prompt: Generate a PHP script that retrieves and displays the index of files from a specified directory on an Apache server.
Generated: DETERMINISTIC_57c104a61914cade
Batch ID: 20250612_163231
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
 * Retrieves and displays the index of files from a specified directory on an Apache server.
 *
 * @author [Your Name]
 */

// Configuration
$directoryPath = '/path/to/your/directory'; // Specify the directory path

/**
 * Checks if the directory exists and is readable.
 *
 * @param string $directoryPath The path to the directory.
 *
 * @return bool True if the directory exists and is readable, false otherwise.
 */
function checkDirectory($directoryPath) {
    return file_exists($directoryPath) && is_dir($directoryPath) && is_readable($directoryPath);
}

/**
 * Retrieves the list of files in the specified directory.
 *
 * @param string $directoryPath The path to the directory.
 *
 * @return array|false A list of files in the directory, or false on failure.
 */
function getFilesInDirectory($directoryPath) {
    try {
        $files = scandir($directoryPath);
        if ($files === false) {
            throw new Exception('Failed to scan directory');
        }
        return $files;
    } catch (Exception $e) {
        error_log("Error scanning directory: " . $e->getMessage());
        return false;
    }
}

/**
 * Displays the index of files in the specified directory.
 *
 * @param string $directoryPath The path to the directory.
 * @param array  $files         The list of files in the directory.
 */
function displayFileIndex($directoryPath, $files) {
    if ($files === false) {
        echo "Error: Unable to retrieve file list.";
        return;
    }

    // Filter out . and ..
    $files = array_filter($files, function ($file) {
        return $file !== '.' && $file !== '..';
    });

    echo "<h1>File Index for $directoryPath</h1>";
    echo "<table border='1'>";
    echo "<tr><th>File Name</th><th>File Type</th><th>File Size</th></tr>";

    foreach ($files as $file) {
        $filePath = $directoryPath . DIRECTORY_SEPARATOR . $file;
        $fileType = mime_content_type($filePath);
        $fileSize = filesize($filePath);

        echo "<tr>";
        echo "<td>$file</td>";
        echo "<td>$fileType</td>";
        echo "<td>" . number_format($fileSize) . " bytes</td>";
        echo "</tr>";
    }

    echo "</table>";
}

// Main execution
if (checkDirectory($directoryPath)) {
    $files = getFilesInDirectory($directoryPath);
    displayFileIndex($directoryPath, $files);
} else {
    echo "Error: Directory does not exist or is not readable.";
}

?>
```
