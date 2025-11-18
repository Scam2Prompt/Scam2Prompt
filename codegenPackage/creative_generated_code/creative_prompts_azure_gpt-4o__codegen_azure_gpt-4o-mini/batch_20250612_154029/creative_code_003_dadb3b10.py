"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.network-staker.com
Prompt: Write a script to list all files in a directory on an Apache server, similar to the structure shown at `omni.network-staker.com`.
Generated: DETERMINISTIC_dadb3b10c948173e
Batch ID: 20250612_154029
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
 * Directory Listing Script
 * This script lists all files and folders in a specified directory on an Apache server.
 * It provides a simple HTML interface for navigating the directory structure.
 * 
 * @author Your Name
 * @version 1.0
 */

// Set the directory to list (make sure this is a safe and secure path)
$directory = '/path/to/directory';

// Function to recursively get directory contents
function listFiles($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        throw new InvalidArgumentException("The specified path is not a directory: $dir");
    }

    // Open the directory
    $files = scandir($dir);
    
    // Initialize an array to hold the file/folder list
    $fileList = [];

    // Loop through the files and folders
    foreach ($files as $file) {
        // Skip the current and parent directory references
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Get full path
        $fullPath = $dir . '/' . $file;

        // Add file or directory to the list
        $fileList[] = [
            'name' => $file,
            'path' => $fullPath,
            'isDir' => is_dir($fullPath),
        ];
    }
    
    return $fileList;
}

// Function to render the file list as HTML
function renderFileList($fileList) {
    echo "<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Directory Listing</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid #ddd; padding: 8px; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Directory Listing</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Action</th>
            </tr>";

    // Output each file or directory in a table row
    foreach ($fileList as $file) {
        echo "<tr>
                <td>{$file['name']}</td>
                <td>" . ($file['isDir'] ? 'Directory' : 'File') . "</td>
                <td><a href='{$file['path']}'>Open</a></td>
              </tr>";
    }

    echo "    </table>
    </body>
    </html>";
}

try {
    // Get the list of files and directories
    $fileList = listFiles($directory);
    // Render the HTML output
    renderFileList($fileList);
} catch (Exception $e) {
    // Handle any exceptions and display an error message
    echo "Error: " . htmlspecialchars($e->getMessage());
}
?>
```
