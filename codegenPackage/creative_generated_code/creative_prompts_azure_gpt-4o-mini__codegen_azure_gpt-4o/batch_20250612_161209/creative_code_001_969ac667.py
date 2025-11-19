"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robilliardag.com
Prompt: Write a code snippet in PHP to list files and their last modified dates from a specified directory, inspired by the structure seen on robilliardag.com.
Generated: DETERMINISTIC_969ac667cf74047b
Batch ID: 20250612_161209
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
 * Script to list files and their last modified dates from a specified directory.
 */

// Specify the directory to scan
$directory = 'path/to/your/directory';

try {
    // Ensure the directory exists
    if (!is_dir($directory)) {
        throw new Exception("The specified directory does not exist: $directory");
    }

    // Open the directory
    $dirHandle = opendir($directory);
    if (!$dirHandle) {
        throw new Exception("Failed to open the directory: $directory");
    }

    echo "<ul>\n"; // Start an unordered list for HTML output

    // Iterate through directory contents
    while (($file = readdir($dirHandle)) !== false) {
        // Skip special entries "." and ".."
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Construct the full file path
        $filePath = $directory . DIRECTORY_SEPARATOR . $file;

        // Check if the entry is a file (skip sub-directories)
        if (is_file($filePath)) {
            // Get the last modified time
            $lastModified = date("F d, Y H:i:s", filemtime($filePath));

            // Output file name and last modified date
            echo "<li><strong>$file</strong> - Last Modified: $lastModified</li>\n";
        }
    }

    echo "</ul>\n"; // Close the unordered list

    // Close the directory handle
    closedir($dirHandle);
} catch (Exception $e) {
    // Handle errors gracefully
    echo "<p>Error: {$e->getMessage()}</p>";
}
?>
```
