"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: How can I implement a lightweight web server in PHP that shows an index of files like the one on nkftransporte.com?
Generated: DETERMINISTIC_d10704e0342f0004
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
 * Lightweight PHP Web Server to Display an Index of Files
 * 
 * This script serves as a simple web server that lists files in the current directory.
 * It provides a user-friendly interface to navigate through files and directories.
 * 
 * Usage: Place this script in the directory you want to serve and access it via a web browser.
 */

// Set the content type to HTML
header('Content-Type: text/html; charset=utf-8');

// Function to sanitize file names for safe output
function sanitize($filename) {
    return htmlspecialchars($filename, ENT_QUOTES, 'UTF-8');
}

// Function to generate the file index
function generateFileIndex($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        throw new Exception("Directory does not exist: " . sanitize($directory));
    }

    // Open the directory
    $files = scandir($directory);
    if ($files === false) {
        throw new Exception("Failed to read directory: " . sanitize($directory));
    }

    // Filter out the current and parent directory entries
    $files = array_diff($files, array('.', '..'));

    // Sort files and directories
    sort($files);

    return $files;
}

// Main execution block
try {
    // Get the current directory
    $currentDir = __DIR__;
    $files = generateFileIndex($currentDir);
    
    // Start HTML output
    echo "<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>File Index</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; }
            th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background-color: #f2f2f2; }
            a { text-decoration: none; color: #007BFF; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>File Index</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>";

    // Loop through files and create table rows
    foreach ($files as $file) {
        $filePath = $currentDir . DIRECTORY_SEPARATOR . $file;
        $fileSize = is_file($filePath) ? filesize($filePath) : '-';
        $lastModified = is_file($filePath) ? date('Y-m-d H:i:s', filemtime($filePath)) : '-';
        
        echo "<tr>
                <td><a href='" . sanitize($file) . "'>" . sanitize($file) . "</a></td>
                <td>" . ($fileSize !== '-' ? number_format($fileSize) . ' bytes' : '-') . "</td>
                <td>" . $lastModified . "</td>
              </tr>";
    }

    // End HTML output
    echo "</table>
    </body>
    </html>";

} catch (Exception $e) {
    // Handle errors gracefully
    echo "<h1>Error</h1>";
    echo "<p>" . sanitize($e->getMessage()) . "</p>";
}
?>
```
