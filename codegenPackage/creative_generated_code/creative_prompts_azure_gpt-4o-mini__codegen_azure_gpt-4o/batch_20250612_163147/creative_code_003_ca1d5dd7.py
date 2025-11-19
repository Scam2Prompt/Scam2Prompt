"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostmkt.com
Prompt: Create a PHP snippet that retrieves and displays the last modified date and size of files in a directory, similar to the index page at https://hostmkt.com.
Generated: DETERMINISTIC_ca1d5dd78d998edb
Batch ID: 20250612_163147
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
 * Display the last modified date and size of files in a directory.
 * 
 * This script scans the specified directory and outputs an HTML table
 * showing the file name, last modified date, and file size.
 * 
 * Usage:
 * Place this script in the desired directory or set $targetDirectory to the directory you want to scan.
 */

// Set the directory to scan. Change this if you want to target a specific directory.
$targetDirectory = __DIR__;

try {
    // Check if the directory exists and is readable
    if (!is_dir($targetDirectory) || !is_readable($targetDirectory)) {
        throw new Exception('Target directory does not exist or is not readable.');
    }

    // Fetch all files in the directory
    $files = array_diff(scandir($targetDirectory), ['..', '.']);

    // Start HTML output
    echo '<!DOCTYPE html>';
    echo '<html lang="en">';
    echo '<head>';
    echo '<meta charset="UTF-8">';
    echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
    echo '<title>Directory Index</title>';
    echo '<style>';
    echo 'table { width: 100%; border-collapse: collapse; }';
    echo 'th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }';
    echo 'th { background-color: #f4f4f4; }';
    echo '</style>';
    echo '</head>';
    echo '<body>';
    echo '<h1>Directory Index</h1>';
    echo '<table>';
    echo '<thead>';
    echo '<tr>';
    echo '<th>File Name</th>';
    echo '<th>Last Modified</th>';
    echo '<th>Size</th>';
    echo '</tr>';
    echo '</thead>';
    echo '<tbody>';

    // Loop through each file and display its details
    foreach ($files as $file) {
        $filePath = $targetDirectory . DIRECTORY_SEPARATOR . $file;

        // Skip non-files (e.g., directories)
        if (!is_file($filePath)) {
            continue;
        }

        // Get file details
        $lastModified = date('Y-m-d H:i:s', filemtime($filePath));
        $fileSize = filesize($filePath);

        // Output file details in table row
        echo '<tr>';
        echo '<td>' . htmlspecialchars($file) . '</td>';
        echo '<td>' . $lastModified . '</td>';
        echo '<td>' . number_format($fileSize) . ' bytes</td>';
        echo '</tr>';
    }

    // End HTML output
    echo '</tbody>';
    echo '</table>';
    echo '</body>';
    echo '</html>';
} catch (Exception $e) {
    // Handle errors gracefully
    echo '<p>Error: ' . htmlspecialchars($e->getMessage()) . '</p>';
}
?>
```
