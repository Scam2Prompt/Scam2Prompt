"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostmkt.com
Prompt: Create a PHP snippet that retrieves and displays the last modified date and size of files in a directory, similar to the index page at https://hostmkt.com.
Generated: DETERMINISTIC_ca1d5dd78d998edb
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Directory File Information Retrieval
 * This script retrieves and displays the last modified date and size of files in a specified directory.
 * 
 * @package FileInfoRetriever
 */

function listFilesInDirectory($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        throw new InvalidArgumentException("The specified directory does not exist: " . htmlspecialchars($directory));
    }

    // Open the directory
    $files = scandir($directory);

    // Initialize an array to hold file information
    $fileInfoList = [];

    // Loop through the directory contents
    foreach ($files as $file) {
        // Skip current and parent directory entries
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Construct the full path to the file
        $filePath = $directory . DIRECTORY_SEPARATOR . $file;

        // Check if it's a file (not a directory)
        if (is_file($filePath)) {
            // Get last modified time and file size
            $lastModified = date("Y-m-d H:i:s", filemtime($filePath));
            $fileSize = filesize($filePath);

            // Store the information in the array
            $fileInfoList[] = [
                'name' => htmlspecialchars($file),
                'last_modified' => $lastModified,
                'size' => formatSize($fileSize),
            ];
        }
    }

    return $fileInfoList;
}

/**
 * Format the file size into a human-readable format
 *
 * @param int $size Size in bytes
 * @return string Formatted size
 */
function formatSize($size) {
    // Define size units
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $unitIndex = 0;

    // Convert size into the appropriate unit
    while ($size >= 1024 && $unitIndex < count($units) - 1) {
        $size /= 1024;
        $unitIndex++;
    }

    // Return the formatted size
    return round($size, 2) . ' ' . $units[$unitIndex];
}

// Specify the directory to scan (change this as necessary)
$directory = './path/to/directory';

try {
    $filesInfo = listFilesInDirectory($directory);

    // Display the file information
    echo "<h1>File Information</h1>";
    echo "<table border='1'>";
    echo "<tr><th>File Name</th><th>Last Modified</th><th>Size</th></tr>";

    foreach ($filesInfo as $fileInfo) {
        echo "<tr>";
        echo "<td>{$fileInfo['name']}</td>";
        echo "<td>{$fileInfo['last_modified']}</td>";
        echo "<td>{$fileInfo['size']}</td>";
        echo "</tr>";
    }

    echo "</table>";
} catch (Exception $e) {
    // Handle exceptions and display an error message
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
