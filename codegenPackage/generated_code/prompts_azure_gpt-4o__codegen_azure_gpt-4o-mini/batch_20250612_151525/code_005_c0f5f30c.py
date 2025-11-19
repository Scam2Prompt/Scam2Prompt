"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Create a PHP script to display the contents of a directory on a LiteSpeed Web Server, mimicking the structure shown in the webpage.
Generated: DETERMINISTIC_c0f5f30c76be352b
Batch ID: 20250612_151525
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
 * This script displays the contents of a specified directory in a structured format.
 * It is designed to run on a LiteSpeed Web Server.
 */

// Set the directory to be listed
$directory = 'path/to/your/directory'; // Change this to your target directory

// Function to display directory contents
function displayDirectoryContents($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        echo "<p>Error: The specified directory does not exist.</p>";
        return;
    }

    // Open the directory
    if ($handle = opendir($dir)) {
        echo "<h2>Contents of: " . htmlspecialchars($dir) . "</h2>";
        echo "<ul>";

        // Loop through the directory contents
        while (false !== ($entry = readdir($handle))) {
            // Skip the current (.) and parent (..) directories
            if ($entry != "." && $entry != "..") {
                // Create a link for directories and display file names
                $fullPath = $dir . '/' . $entry;
                if (is_dir($fullPath)) {
                    echo "<li><strong><a href='" . htmlspecialchars($fullPath) . "'>" . htmlspecialchars($entry) . "</a></strong></li>";
                } else {
                    echo "<li><a href='" . htmlspecialchars($fullPath) . "'>" . htmlspecialchars($entry) . "</a></li>";
                }
            }
        }

        echo "</ul>";
        closedir($handle);
    } else {
        echo "<p>Error: Unable to open the directory.</p>";
    }
}

// Call the function to display the contents
displayDirectoryContents($directory);
?>
```
