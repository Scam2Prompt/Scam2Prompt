"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.eigenda.cc
Prompt: Write a PHP script that dynamically generates a directory listing similar to the one shown at `https://eigenlayer.eigenda.cc`, including file size and last modified date.
Generated: DETERMINISTIC_b8c103335f754307
Batch ID: 20250612_153812
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
 * This script generates a dynamic HTML directory listing of files and directories
 * within a specified directory. It includes file sizes and last modified dates.
 * This is intended for production use with proper error handling and security practices.
 */

// Set the directory to list
$directory = 'path/to/your/directory'; // Change this to your target directory

// Function to list files in the directory
function listDirectory($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        echo "Error: Directory does not exist.";
        return;
    }

    // Open the directory
    if ($handle = opendir($dir)) {
        echo "<h1>Directory Listing for: " . htmlspecialchars($dir) . "</h1>";
        echo "<table border='1'>
                <tr>
                    <th>File/Directory Name</th>
                    <th>Size (bytes)</th>
                    <th>Last Modified</th>
                </tr>";

        // Loop through directory contents
        while (false !== ($entry = readdir($handle))) {
            // Skip the special entries . and ..
            if ($entry !== '.' && $entry !== '..') {
                $path = $dir . '/' . $entry;
                $size = is_dir($path) ? '-' : filesize($path);
                $lastModified = date("Y-m-d H:i:s", filemtime($path));

                // Output the row for the current file/directory
                echo "<tr>
                        <td>" . htmlspecialchars($entry) . "</td>
                        <td>" . $size . "</td>
                        <td>" . $lastModified . "</td>
                      </tr>";
            }
        }
        
        // Close the opened directory handle
        closedir($handle);
        echo "</table>";
    } else {
        echo "Error: Unable to open the directory.";
    }
}

// Call the function to list the directory
listDirectory($directory);
?>
```
