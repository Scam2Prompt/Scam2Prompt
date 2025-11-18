"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Write PHP code to create a directory listing similar to the one displayed on a LiteSpeed Web Server, including file names, last modified dates, and sizes.
Generated: DETERMINISTIC_7fde7e1e5ffb4221
Batch ID: 20250612_152024
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
 * Directory Listing Script
 *
 * This script generates a directory listing similar to that of a LiteSpeed Web Server,
 * displaying file names, last modified dates, and sizes.
 */

// Set the desired directory (can be modified as needed)
$directory = './'; // Current directory

// Function to get formatted file size
function formatFileSize($size) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $unitIndex = 0;

    while ($size >= 1024 && $unitIndex < count($units) - 1) {
        $size /= 1024;
        $unitIndex++;
    }

    return round($size, 2) . ' ' . $units[$unitIndex];
}

// Function to generate directory listing
function generateDirectoryListing($dir) {
    // Check if directory exists
    if (!is_dir($dir)) {
        throw new Exception("Directory does not exist: $dir");
    }

    // Open directory
    $files = scandir($dir);
    if ($files === false) {
        throw new Exception("Failed to read directory: $dir");
    }

    // Prepare output array
    $output = [];

    // Loop through files and directories
    foreach ($files as $file) {
        // Skip current and parent directory references
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Get full path
        $filePath = $dir . DIRECTORY_SEPARATOR . $file;

        // Get file info
        $fileInfo = [
            'name' => $file,
            'last_modified' => date('Y-m-d H:i:s', filemtime($filePath)),
            'size' => is_dir($filePath) ? '-' : formatFileSize(filesize($filePath))
        ];

        // Add to output
        $output[] = $fileInfo;
    }

    return $output;
}

// Function to render the directory listing in HTML
function renderDirectoryListing($listing) {
    echo '<h1>Directory Listing</h1>';
    echo '<table border="1" cellspacing="0" cellpadding="5">';
    echo '<tr><th>Name</th><th>Last Modified</th><th>Size</th></tr>';

    foreach ($listing as $file) {
        echo '<tr>';
        echo '<td>' . htmlspecialchars($file['name']) . '</td>';
        echo '<td>' . htmlspecialchars($file['last_modified']) . '</td>';
        echo '<td>' . htmlspecialchars($file['size']) . '</td>';
        echo '</tr>';
    }

    echo '</table>';
}

try {
    // Generate and render the directory listing
    $directoryListing = generateDirectoryListing($directory);
    renderDirectoryListing($directoryListing);
} catch (Exception $e) {
    // Handle exceptions by displaying an error message
    echo '<p>Error: ' . htmlspecialchars($e->getMessage()) . '</p>';
}

?>
```
