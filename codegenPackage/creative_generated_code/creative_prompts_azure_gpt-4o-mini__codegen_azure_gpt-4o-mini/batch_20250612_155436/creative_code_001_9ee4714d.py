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
 * List files in a specified directory.
 * This script will scan the directory and display a list of files.
 */

// Define the directory to be scanned
$directoryPath = 'path/to/your/directory'; // Change this to your target directory

// Ensure the directory path is valid
if (!is_dir($directoryPath)) {
    die("Error: The directory '$directoryPath' does not exist.");
}

// Attempt to open the directory
if ($handle = opendir($directoryPath)) {
    echo "<h2>Files in Directory: " . htmlspecialchars($directoryPath) . "</h2>";
    echo "<ul>";

    // Loop through the directory contents
    while (false !== ($entry = readdir($handle))) {
        // Skip the current and parent directory entries
        if ($entry !== '.' && $entry !== '..') {
            // Display the file name
            echo "<li>" . htmlspecialchars($entry) . "</li>";
        }
    }

    // Close the directory handle
    closedir($handle);
    echo "</ul>";
} else {
    die("Error: Could not open the directory '$directoryPath'.");
}
?>
```
