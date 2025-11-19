"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Write a code snippet to list files in a directory using PHP, referencing the structure seen in the nkftransporte.com index page.
Generated: DETERMINISTIC_9ee4714d21d5ceb1
Batch ID: 20250612_155436
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
 * List files in a specified directory.
 * 
 * This script retrieves and displays a list of files in a given directory.
 * It handles errors gracefully and ensures that only files are listed.
 * 
 * @param string $directory The path to the directory to list files from.
 * @return void
 */
function listFilesInDirectory($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        echo "Error: The specified path is not a directory.";
        return;
    }

    // Attempt to open the directory
    if ($handle = opendir($directory)) {
        echo "<h2>Files in directory: $directory</h2>";
        echo "<ul>";

        // Loop through the directory entries
        while (false !== ($entry = readdir($handle))) {
            // Skip the current and parent directory entries
            if ($entry != "." && $entry != "..") {
                // Check if the entry is a file
                if (is_file($directory . '/' . $entry)) {
                    echo "<li>" . htmlspecialchars($entry) . "</li>";
                }
            }
        }

        echo "</ul>";
        // Close the directory handle
        closedir($handle);
    } else {
        echo "Error: Unable to open the directory.";
    }
}

// Specify the directory to list files from
$directoryPath = '/path/to/your/directory'; // Change this to your target directory

// Call the function to list files
listFilesInDirectory($directoryPath);
?>
```
