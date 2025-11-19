"""
Generated Code Metadata:
========================
Original URL: https://hostmkt.com
Prompt: Create a PHP snippet that retrieves and displays the last modified date and size of files in a directory, similar to the index page at https://hostmkt.com.
Generated: DETERMINISTIC_ca1d5dd78d998edb
Batch ID: 20250612_163147
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
 * Retrieves and displays the last modified date and size of files in a directory.
 */

// Configuration
$directoryPath = '.'; // Current directory

// Check if the directory exists
if (!file_exists($directoryPath)) {
    throw new Exception("The directory '$directoryPath' does not exist.");
}

// Check if the directory is readable
if (!is_readable($directoryPath)) {
    throw new Exception("The directory '$directoryPath' is not readable.");
}

// Get a list of files in the directory
try {
    $files = scandir($directoryPath);
} catch (Exception $e) {
    throw new Exception("Failed to scan the directory '$directoryPath': " . $e->getMessage());
}

// Filter out directories and sort files by last modified date
$filteredFiles = [];
foreach ($files as $file) {
    $filePath = $directoryPath . DIRECTORY_SEPARATOR . $file;
    if (is_file($filePath)) {
        $filteredFiles[] = $filePath;
    }
}

usort($filteredFiles, function($a, $b) {
    return filemtime($b) - filemtime($a);
});

// Display file information
echo "<table>";
echo "<tr><th>File</th><th>Last Modified</th><th>Size</th></tr>";

foreach ($filteredFiles as $file) {
    try {
        $lastModified = date("Y-m-d H:i:s", filemtime($file));
        $fileSize = filesize($file);
        $fileName = basename($file);

        // Format file size
        if ($fileSize < 1024) {
            $fileSize = $fileSize . " B";
        } elseif ($fileSize < 1024 * 1024) {
            $fileSize = sprintf("%.2f KB", $fileSize / 1024);
        } else {
            $fileSize = sprintf("%.2f MB", $fileSize / (1024 * 1024));
        }

        echo "<tr>";
        echo "<td>$fileName</td>";
        echo "<td>$lastModified</td>";
        echo "<td>$fileSize</td>";
        echo "</tr>";
    } catch (Exception $e) {
        echo "<tr><td>$file</td><td colspan='2'>Error: " . $e->getMessage() . "</td></tr>";
    }
}

echo "</table>";

?>
```
