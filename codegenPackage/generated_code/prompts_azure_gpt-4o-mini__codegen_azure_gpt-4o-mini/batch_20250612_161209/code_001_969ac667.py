"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Write a code snippet in PHP to list files and their last modified dates from a specified directory, inspired by the structure seen on robilliardag.com.
Generated: DETERMINISTIC_969ac667cf74047b
Batch ID: 20250612_161209
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
 * List files and their last modified dates from a specified directory.
 *
 * @param string $directory The path to the directory to scan.
 * @return array An associative array of filenames and their last modified dates.
 * @throws InvalidArgumentException If the provided directory is not valid.
 */
function listFilesWithModificationDates($directory) {
    // Validate the directory path
    if (!is_dir($directory)) {
        throw new InvalidArgumentException("The provided path is not a valid directory: $directory");
    }

    // Initialize an array to hold the file information
    $filesInfo = [];

    // Open the directory
    if ($handle = opendir($directory)) {
        // Loop through the directory entries
        while (false !== ($entry = readdir($handle))) {
            // Skip the current and parent directory entries
            if ($entry !== '.' && $entry !== '..') {
                // Get the full path of the file
                $filePath = $directory . DIRECTORY_SEPARATOR . $entry;

                // Check if it's a file
                if (is_file($filePath)) {
                    // Get the last modified time
                    $lastModified = date("Y-m-d H:i:s", filemtime($filePath));
                    // Store the filename and last modified date
                    $filesInfo[$entry] = $lastModified;
                }
            }
        }
        // Close the directory handle
        closedir($handle);
    } else {
        throw new RuntimeException("Failed to open directory: $directory");
    }

    return $filesInfo;
}

// Example usage
try {
    $directoryPath = '/path/to/your/directory'; // Specify your directory path here
    $files = listFilesWithModificationDates($directoryPath);
    
    // Output the results
    foreach ($files as $file => $modifiedDate) {
        echo "File: $file - Last Modified: $modifiedDate\n";
    }
} catch (Exception $e) {
    // Handle any exceptions that may occur
    echo "Error: " . $e->getMessage();
}
?>
```
