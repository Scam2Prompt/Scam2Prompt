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
 * Directory Listing Script
 * 
 * This script generates a directory listing similar to that of a LiteSpeed Web Server.
 * It displays file names, last modified dates, and sizes in a user-friendly format.
 * 
 * @package DirectoryListing
 * @author Your Name
 * @version 1.0
 */

// Set the directory to be listed
$directory = '.';

// Check if the directory exists
if (!is_dir($directory)) {
    die("Error: The specified directory does not exist.");
}

// Open the directory
if ($handle = opendir($directory)) {
    // Initialize an array to hold file information
    $files = [];

    // Loop through the directory entries
    while (false !== ($entry = readdir($handle))) {
        // Skip the current and parent directory entries
        if ($entry != "." && $entry != "..") {
            // Get file path
            $filePath = $directory . DIRECTORY_SEPARATOR . $entry;

            // Get file information
            $fileInfo = [
                'name' => $entry,
                'size' => filesize($filePath),
                'modified' => date("F d Y H:i:s", filemtime($filePath)),
                'isDir' => is_dir($filePath)
            ];

            // Add file information to the array
            $files[] = $fileInfo;
        }
    }

    // Close the directory handle
    closedir($handle);

    // Sort files by name
    usort($files, function($a, $b) {
        return strcmp($a['name'], $b['name']);
    });

    // Output the directory listing
    echo "<h1>Directory Listing for: $directory</h1>";
    echo "<table border='1'>";
    echo "<tr><th>Name</th><th>Size (bytes)</th><th>Last Modified</th></tr>";

    foreach ($files as $file) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($file['name']) . "</td>";
        echo "<td>" . ($file['isDir'] ? '-' : $file['size']) . "</td>";
        echo "<td>" . htmlspecialchars($file['modified']) . "</td>";
        echo "</tr>";
    }

    echo "</table>";
} else {
    // Handle error if the directory cannot be opened
    die("Error: Unable to open the directory.");
}
?>
```
