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
 * This script scans a given directory and outputs the file names along with
 * their last modified timestamps in a human-readable format.
 * 
 * Usage: Update the $directory variable with the path to the desired directory.
 */

// Specify the directory to scan
$directory = __DIR__; // Change this to your desired directory path

// Check if the directory exists and is readable
if (!is_dir($directory)) {
    die("Error: The specified directory does not exist.\n");
}

if (!is_readable($directory)) {
    die("Error: The specified directory is not readable.\n");
}

// Open the directory
$handle = opendir($directory);

if ($handle === false) {
    die("Error: Failed to open the directory.\n");
}

// Array to store file details
$fileDetails = [];

try {
    // Loop through the directory contents
    while (($file = readdir($handle)) !== false) {
        $filePath = $directory . DIRECTORY_SEPARATOR . $file;

        // Skip special entries "." and ".."
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Check if the entry is a file
        if (is_file($filePath)) {
            // Get the last modified time of the file
            $lastModified = filemtime($filePath);

            if ($lastModified === false) {
                throw new Exception("Error: Unable to retrieve last modified time for file: $file");
            }

            // Add file details to the array
            $fileDetails[] = [
                'name' => $file,
                'last_modified' => date('Y-m-d H:i:s', $lastModified),
            ];
        }
    }
} catch (Exception $e) {
    // Handle any exceptions
    die($e->getMessage() . "\n");
} finally {
    // Close the directory handle
    closedir($handle);
}

// Output the file details
echo "Files in directory: $directory\n";
echo str_repeat('=', 40) . "\n";

foreach ($fileDetails as $file) {
    echo "File: " . $file['name'] . "\n";
    echo "Last Modified: " . $file['last_modified'] . "\n";
    echo str_repeat('-', 40) . "\n";
}
?>
```
