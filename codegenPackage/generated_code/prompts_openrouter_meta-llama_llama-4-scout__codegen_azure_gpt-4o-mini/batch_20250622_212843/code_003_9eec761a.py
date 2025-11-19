"""
Generated Code Metadata:
========================
Original URL: https://app.marketpoly.net
Prompt: Create a simple PHP script that checks the last modified date of a file, similar to what is shown in the directory listing.
Generated: DETERMINISTIC_9eec761aa1ee4bc5
Batch ID: 20250622_212843
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
 * A simple PHP script to check the last modified date of a specified file.
 * 
 * This script takes a file path as input and returns the last modified date
 * in a human-readable format. It also handles errors gracefully.
 */

// Function to get the last modified date of a file
function getLastModifiedDate($filePath) {
    // Check if the file exists
    if (!file_exists($filePath)) {
        throw new Exception("File not found: " . $filePath);
    }

    // Get the last modified time of the file
    $lastModifiedTime = filemtime($filePath);

    // Check if the filemtime function was successful
    if ($lastModifiedTime === false) {
        throw new Exception("Could not retrieve last modified time for: " . $filePath);
    }

    // Return the last modified date in a human-readable format
    return date("F d Y H:i:s", $lastModifiedTime);
}

// Main script execution
try {
    // Specify the file path (change this to the file you want to check)
    $filePath = 'path/to/your/file.txt';

    // Get the last modified date
    $lastModifiedDate = getLastModifiedDate($filePath);

    // Output the result
    echo "Last modified date of '{$filePath}': " . $lastModifiedDate . PHP_EOL;

} catch (Exception $e) {
    // Handle any exceptions and display an error message
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
