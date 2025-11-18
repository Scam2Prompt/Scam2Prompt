"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perurest.com
Prompt: Write a PHP script to dynamically display directory contents served by LiteSpeed Web Server in a user-friendly format.
Generated: DETERMINISTIC_f455f30dc6e35bca
Batch ID: 20250612_154216
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
 * This script dynamically generates a user-friendly directory listing 
 * for files and folders in the current working directory.
 * 
 * Requirements: Running on a LiteSpeed Web Server with PHP enabled.
 * 
 * Author: [Your Name]
 * Date: [Current Date]
 */

// Set the content type to HTML
header('Content-Type: text/html; charset=utf-8');

// Define the directory to list
$directory = '.'; // Current directory

// Function to safely escape output
function safeOutput($string) {
    return htmlspecialchars($string, ENT_QUOTES, 'UTF-8');
}

// Function to list the contents of the directory
function listDirectory($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        throw new Exception("The specified directory does not exist: " . safeOutput($dir));
    }

    // Open the directory
    if ($handle = opendir($dir)) {
        echo "<h1>Directory Listing for: " . safeOutput($dir) . "</h1>";
        echo "<ul>";

        // Loop through the directory contents
        while (false !== ($entry = readdir($handle))) {
            // Skip the special entries "." and ".."
            if ($entry != "." && $entry != "..") {
                // Determine if the entry is a directory or a file
                $fullPath = $dir . DIRECTORY_SEPARATOR . $entry;
                if (is_dir($fullPath)) {
                    echo "<li><strong>Directory:</strong> <a href=\"" . safeOutput($fullPath) . "\">" . safeOutput($entry) . "</a></li>";
                } else {
                    echo "<li><strong>File:</strong> " . safeOutput($entry) . "</li>";
                }
            }
        }

        echo "</ul>";
        closedir($handle); // Close the directory handle
    } else {
        throw new Exception("Unable to open the directory: " . safeOutput($dir));
    }
}

// Error handling
try {
    listDirectory($directory);
} catch (Exception $e) {
    echo "<p style='color:red;'>Error: " . safeOutput($e->getMessage()) . "</p>";
}

?>
```
