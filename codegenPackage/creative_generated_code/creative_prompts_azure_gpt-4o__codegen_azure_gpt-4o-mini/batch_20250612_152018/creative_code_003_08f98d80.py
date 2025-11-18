"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: Generate a script using PHP to dynamically display a directory listing with file details, inspired by the structure on https://refconegypt.net.
Generated: DETERMINISTIC_08f98d80387ea81f
Batch ID: 20250612_152018
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
 * This script dynamically displays a directory listing with file details.
 * It shows the file name, size, and last modified date.
 */

// Define the directory to list files from
$directory = 'your/directory/path'; // Change this to your target directory

// Function to display directory contents
function displayDirectoryListing($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        die("Error: The directory '$dir' does not exist.");
    }

    // Open the directory
    if ($handle = opendir($dir)) {
        echo "<h1>Directory Listing for: $dir</h1>";
        echo "<table border='1'>
                <tr>
                    <th>Filename</th>
                    <th>Size (bytes)</th>
                    <th>Last Modified</th>
                </tr>";

        // Loop through directory contents
        while (false !== ($entry = readdir($handle))) {
            // Skip the special entries "." and ".."
            if ($entry != "." && $entry != "..") {
                // Get the full path of the entry
                $filePath = $dir . '/' . $entry;
                
                // Get file details
                $fileSize = filesize($filePath);
                $lastModified = date("F d Y H:i:s.", filemtime($filePath));
                
                // Display file details in a table row
                echo "<tr>
                        <td><a href='$filePath'>$entry</a></td>
                        <td>$fileSize</td>
                        <td>$lastModified</td>
                      </tr>";
            }
        }
        
        echo "</table>";
        // Close the directory handle
        closedir($handle);
    } else {
        die("Error: Could not open directory '$dir'.");
    }
}

// Call the function to display the directory listing
displayDirectoryListing($directory);
?>
```
