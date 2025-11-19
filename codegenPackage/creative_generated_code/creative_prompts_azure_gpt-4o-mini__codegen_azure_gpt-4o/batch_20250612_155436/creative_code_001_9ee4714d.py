"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: Write a code snippet to list files in a directory using PHP, referencing the structure seen in the nkftransporte.com index page.
Generated: DETERMINISTIC_9ee4714d21d5ceb1
Batch ID: 20250612_155436
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
 * List all files in a given directory.
 * 
 * This script lists the files in a directory in a clean and structured way.
 * It includes error handling and adheres to best practices.
 */

// Define the target directory
$targetDirectory = './'; // Change this to the desired path

try {
    // Ensure the directory exists and is readable
    if (!is_dir($targetDirectory)) {
        throw new Exception("The specified directory does not exist: $targetDirectory");
    }

    if (!is_readable($targetDirectory)) {
        throw new Exception("The specified directory is not readable: $targetDirectory");
    }

    // Open the directory handle
    $directoryHandle = opendir($targetDirectory);
    if (!$directoryHandle) {
        throw new Exception("Failed to open the directory: $targetDirectory");
    }

    echo "<ul>\n"; // Start the list for displaying files

    // Iterate through the directory contents
    while (($file = readdir($directoryHandle)) !== false) {
        // Skip current and parent directory pointers
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Check if the item is a file (not a directory)
        if (is_file($targetDirectory . DIRECTORY_SEPARATOR . $file)) {
            echo "<li>" . htmlspecialchars($file) . "</li>\n"; // Output each file name
        }
    }

    echo "</ul>\n"; // End the list

    // Close the directory handle
    closedir($directoryHandle);
} catch (Exception $e) {
    // Handle and log errors
    error_log($e->getMessage());
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
