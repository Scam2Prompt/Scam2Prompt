"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miles.plumenetworke.com
Prompt: Write a PHP script to dynamically generate an Apache-style directory listing, inspired by the structure at https://miles.plumenetworke.com.
Generated: DETERMINISTIC_53345ab9f177954e
Batch ID: 20250612_154147
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Generates an Apache-style directory listing.
 *
 * This script scans the specified directory and lists its contents in an
 * HTML format similar to an Apache directory listing.
 *
 * PHP version 7.4 or higher
 *
 * @category DirectoryListing
 * @package  CustomScript
 * @author   Your Name
 * @license  MIT License
 * @link     https://www.example.com
 */

// Set the directory to be scanned (change this path as necessary)
$directory = './'; // Current directory

// Function to generate the directory listing
function generateDirectoryListing($dir) {
    // Check if the specified directory exists
    if (!is_dir($dir)) {
        http_response_code(404);
        die("<h1>Error 404: Directory Not Found</h1>");
    }

    // Open the directory
    if ($handle = opendir($dir)) {
        echo "<!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>Directory Listing</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                a { text-decoration: none; color: #007BFF; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>Directory Listing for: " . htmlspecialchars($dir) . "</h1>
            <ul>";

        // Loop through the directory contents
        while (false !== ($entry = readdir($handle))) {
            // Skip the special entries '.' and '..'
            if ($entry === '.' || $entry === '..') {
                continue;
            }

            // Generate the full path to the entry
            $fullPath = rtrim($dir, '/') . '/' . $entry;

            // Check if the entry is a directory or a file and prepare the display
            $type = is_dir($fullPath) ? 'dir' : 'file';
            $icon = $type === 'dir' ? '📁' : '📄';
            echo "<li><span>$icon</span> <a href='" . htmlspecialchars($fullPath) . "'>" . htmlspecialchars($entry) . "</a></li>";
        }

        // Close the unordered list and directory handle
        echo "</ul></body></html>";
        closedir($handle);
    } else {
        // Handle error opening the directory
        http_response_code(500);
        die("<h1>Error 500: Internal Server Error</h1>");
    }
}

// Call the function to generate the listing
generateDirectoryListing($directory);
?>
```
