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
 * Displays the contents of a directory on a LiteSpeed Web Server.
 *
 * @author [Your Name]
 */

// Configuration
$directoryPath = './'; // Current directory
$maxDepth = 5; // Maximum recursion depth

/**
 * Displays directory contents.
 *
 * @param string $path Directory path.
 * @param int $depth Current recursion depth.
 */
function displayDirectoryContents($path, $depth = 0) {
    // Check if directory exists
    if (!file_exists($path)) {
        throw new Exception("Directory '$path' does not exist.");
    }

    // Check if path is a directory
    if (!is_dir($path)) {
        throw new Exception("'$path' is not a directory.");
    }

    // Check maximum recursion depth
    if ($depth >= $GLOBALS['maxDepth']) {
        echo "Maximum recursion depth reached.\n";
        return;
    }

    try {
        // Open directory
        $dirHandle = opendir($path);
        if (!$dirHandle) {
            throw new Exception("Failed to open directory '$path'.");
        }

        // Read directory contents
        while (($entry = readdir($dirHandle)) !== false) {
            // Skip current and parent directories
            if ($entry == '.' || $entry == '..') {
                continue;
            }

            $entryPath = $path . $entry;

            // Display directory or file information
            if (is_dir($entryPath)) {
                echo "Directory: $entry\n";
                displayDirectoryContents($entryPath, $depth + 1);
            } else {
                echo "File: $entry\n";
            }
        }

        // Close directory
        closedir($dirHandle);
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
    }
}

// Display directory contents
try {
    displayDirectoryContents($directoryPath);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
