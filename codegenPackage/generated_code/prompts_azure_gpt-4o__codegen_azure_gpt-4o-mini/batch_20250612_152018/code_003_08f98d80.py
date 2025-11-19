"""
Generated Code Metadata:
========================
Original URL: https://refconegypt.net
Prompt: Generate a script using PHP to dynamically display a directory listing with file details, inspired by the structure on https://refconegypt.net.
Generated: DETERMINISTIC_08f98d80387ea81f
Batch ID: 20250612_152018
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
 * This script dynamically generates a directory listing of files and directories
 * in a specified path. It displays file details such as name, size, and last modified date.
 * 
 * @package DirectoryListing
 * @author Your Name
 * @version 1.0
 */

// Set the directory path (change this to the desired directory)
$directoryPath = 'path/to/your/directory';

// Function to display the directory listing
function displayDirectoryListing($path) {
    // Check if the path is a valid directory
    if (!is_dir($path)) {
        echo "Error: The specified path is not a directory.";
        return;
    }

    // Open the directory
    if ($handle = opendir($path)) {
        echo "<h1>Directory Listing for: " . htmlspecialchars($path) . "</h1>";
        echo "<table border='1'>";
        echo "<tr><th>File Name</th><th>Size (bytes)</th><th>Last Modified</th></tr>";

        // Loop through the directory entries
        while (false !== ($entry = readdir($handle))) {
            // Skip the current and parent directory entries
            if ($entry == '.' || $entry == '..') {
                continue;
            }

            // Get the full path of the entry
            $fullPath = $path . DIRECTORY_SEPARATOR . $entry;

            // Get file details
            $fileSize = filesize($fullPath);
            $lastModified = date("F d Y H:i:s", filemtime($fullPath));

            // Display the file details in a table row
            echo "<tr>";
            echo "<td>" . htmlspecialchars($entry) . "</td>";
            echo "<td>" . htmlspecialchars($fileSize) . "</td>";
            echo "<td>" . htmlspecialchars($lastModified) . "</td>";
            echo "</tr>";
        }

        // Close the directory handle
        closedir($handle);
        echo "</table>";
    } else {
        echo "Error: Unable to open the directory.";
    }
}

// Call the function to display the directory listing
displayDirectoryListing($directoryPath);
?>
```
