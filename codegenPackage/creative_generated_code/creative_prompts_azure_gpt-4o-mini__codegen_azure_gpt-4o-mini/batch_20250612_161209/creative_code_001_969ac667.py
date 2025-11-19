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
 * List files and their last modified dates from a specified directory.
 *
 * This script scans a given directory and outputs the names of files
 * along with their last modified dates in a user-friendly format.
 *
 * @param string $directory The path to the directory to scan.
 * @return void Outputs the file names and last modified dates to the browser.
 */
function listFilesWithLastModified($directory) {
    // Ensure the specified directory exists
    if (!is_dir($directory)) {
        echo "Error: The specified directory does not exist.";
        return;
    }

    // Open the directory
    if ($handle = opendir($directory)) {
        echo "<h1>Files in Directory: " . htmlspecialchars($directory) . "</h1>";
        echo "<table border='1'>";
        echo "<tr><th>File Name</th><th>Last Modified</th></tr>";

        // Iterate through the directory entries
        while (false !== ($file = readdir($handle))) {
            // Skip the special . and .. entries
            if ($file !== '.' && $file !== '..') {
                $filePath = $directory . '/' . $file;

                // Check if it's a file (and not a directory)
                if (is_file($filePath)) {
                    // Get the last modified time
                    $lastModified = date("F d Y H:i:s.", filemtime($filePath));

                    // Display the file name and last modified date
                    echo "<tr><td>" . htmlspecialchars($file) . "</td><td>" . htmlspecialchars($lastModified) . "</td></tr>";
                }
            }
        }

        // Close the directory handle
        closedir($handle);
        echo "</table>";
    } else {
        echo "Error: Unable to open the directory.";
    }
}

// Specify the directory to list
$directoryPath = '/path/to/your/directory'; // Change this to your target directory

// Call the function to list files
listFilesWithLastModified($directoryPath);
?>
```
