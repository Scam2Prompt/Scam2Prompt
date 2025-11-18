"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmaarokatcap.com
Prompt: Create a PHP script that interacts with files in a directory listing, similar to the one shown on the webpage, to display file metadata (e.g., size, last modified date).
Generated: DETERMINISTIC_d5528e798fb7d68c
Batch ID: 20250612_145923
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
 * File Metadata Viewer
 * 
 * This script lists all files in a specified directory and displays their metadata,
 * including file size and last modified date.
 * 
 * Usage: Place this script in a PHP-enabled web server. Modify the $directory variable
 * to point to the desired directory for file listing.
 */

// Set the directory path (modify as needed)
$directory = './files'; // Relative or absolute path to the directory

// Ensure the directory exists
if (!is_dir($directory)) {
    die('Error: Specified directory does not exist.');
}

// Open the directory
$dirHandle = opendir($directory);
if (!$dirHandle) {
    die('Error: Unable to open the directory.');
}

echo "<h1>File Metadata Viewer</h1>";
echo "<table border='1' cellpadding='5' cellspacing='0'>";
echo "<tr><th>File Name</th><th>Size (Bytes)</th><th>Last Modified</th></tr>";

try {
    // Iterate through the files in the directory
    while (($file = readdir($dirHandle)) !== false) {
        // Skip special directories '.' and '..'
        if ($file === '.' || $file === '..') {
            continue;
        }

        $filePath = $directory . '/' . $file;

        // Ensure it's a file
        if (is_file($filePath)) {
            // Get file metadata
            $fileSize = filesize($filePath); // File size in bytes
            $lastModified = date('Y-m-d H:i:s', filemtime($filePath)); // Last modified date

            // Output file metadata in table format
            echo "<tr>";
            echo "<td>" . htmlspecialchars($file) . "</td>"; // Sanitize for HTML
            echo "<td>" . $fileSize . "</td>";
            echo "<td>" . $lastModified . "</td>";
            echo "</tr>";
        }
    }
} catch (Exception $e) {
    // Handle unexpected errors
    echo "<tr><td colspan='3' style='color: red;'>Error: " . htmlspecialchars($e->getMessage()) . "</td></tr>";
}

// Close the directory handle
closedir($dirHandle);

echo "</table>";
?>
```
