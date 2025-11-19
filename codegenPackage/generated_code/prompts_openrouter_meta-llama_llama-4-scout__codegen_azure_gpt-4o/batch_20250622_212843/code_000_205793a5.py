"""
Generated Code Metadata:
========================
Original URL: https://app.marketpoly.net
Prompt: Write a PHP script that interacts with an Apache server to list directory contents.
Generated: DETERMINISTIC_205793a51c1e3117
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
 * Script to list directory contents on an Apache server.
 * 
 * This script lists the contents of a specified directory on the server.
 * It includes error handling to ensure the directory exists and is readable.
 * 
 * Usage: Place this script in a directory accessible by the Apache server.
 * Ensure proper permissions are set for the directory you want to list.
 */

// Define the directory to list (change this to the desired directory)
$directory = __DIR__; // Current directory

try {
    // Check if the directory exists
    if (!is_dir($directory)) {
        throw new Exception("The specified path is not a valid directory: $directory");
    }

    // Open the directory
    $dirHandle = opendir($directory);
    if (!$dirHandle) {
        throw new Exception("Failed to open the directory: $directory");
    }

    // Initialize an array to store directory contents
    $contents = [];

    // Read the directory contents
    while (($entry = readdir($dirHandle)) !== false) {
        // Skip the current and parent directory entries
        if ($entry === '.' || $entry === '..') {
            continue;
        }
        $contents[] = $entry;
    }

    // Close the directory handle
    closedir($dirHandle);

    // Output the directory contents as a JSON response
    header('Content-Type: application/json');
    echo json_encode([
        'status' => 'success',
        'directory' => $directory,
        'contents' => $contents
    ], JSON_PRETTY_PRINT);

} catch (Exception $e) {
    // Handle errors and output a JSON error response
    header('Content-Type: application/json', true, 500);
    echo json_encode([
        'status' => 'error',
        'message' => $e->getMessage()
    ], JSON_PRETTY_PRINT);
}
?>
```
