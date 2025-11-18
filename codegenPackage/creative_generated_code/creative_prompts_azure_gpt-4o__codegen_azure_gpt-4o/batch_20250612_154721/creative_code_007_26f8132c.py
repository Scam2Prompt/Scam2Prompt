"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-dapps.com
Prompt: Write a PHP script to interact with a LiteSpeed Web Server and list directory contents, similar to the setup at connect-dapps.com.
Generated: DETERMINISTIC_26f8132c679a513b
Batch ID: 20250612_154721
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
 * Script to list directory contents on a LiteSpeed Web Server.
 * 
 * This script interacts with the LiteSpeed Web Server and fetches the listing
 * of files and directories in the specified path. The script handles errors 
 * gracefully and is production-ready. 
 * 
 * Usage:
 * Place the script in the desired directory on the LiteSpeed server and access
 * it via a browser or command line (CLI).
 */

// Set the root directory to list contents (Adjust this as needed)
$rootDirectory = __DIR__;

try {
    // Ensure the root directory exists and is accessible
    if (!is_dir($rootDirectory)) {
        throw new Exception("Invalid directory: $rootDirectory does not exist.");
    }

    // Open the directory
    $handle = opendir($rootDirectory);
    if (!$handle) {
        throw new Exception("Failed to open directory: $rootDirectory.");
    }

    // Initialize an array to hold directory contents
    $directoryContents = [];

    // Loop through the directory entries
    while (($entry = readdir($handle)) !== false) {
        // Skip the current directory and parent directory references
        if ($entry === '.' || $entry === '..') {
            continue;
        }

        // Build the full path of the entry
        $entryPath = $rootDirectory . DIRECTORY_SEPARATOR . $entry;

        // Determine if the entry is a file or directory
        $type = is_dir($entryPath) ? 'directory' : 'file';

        // Append details to the directoryContents array
        $directoryContents[] = [
            'name' => $entry,
            'type' => $type,
            'size' => $type === 'file' ? filesize($entryPath) : null,
            'last_modified' => date("Y-m-d H:i:s", filemtime($entryPath))
        ];
    }

    // Close the directory handle
    closedir($handle);

    // Output the directory contents in JSON format
    header('Content-Type: application/json');
    echo json_encode([
        'status' => 'success',
        'directory' => $rootDirectory,
        'contents' => $directoryContents
    ], JSON_PRETTY_PRINT);
} catch (Exception $e) {
    // Handle errors gracefully
    header('Content-Type: application/json');
    echo json_encode([
        'status' => 'error',
        'message' => $e->getMessage()
    ], JSON_PRETTY_PRINT);
    exit;
}
?>
```
