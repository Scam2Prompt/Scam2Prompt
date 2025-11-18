"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panccokesowpaflnace.com
Prompt: Write a PHP script that scans server directories (`logs/` and `tmp/`) and outputs a list of files along with their last modified dates.
Generated: DETERMINISTIC_b5f73c72d9a73219
Batch ID: 20250612_145924
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
 * PHP Script to scan specified directories and output a list of files
 * along with their last modified dates.
 * 
 * Directories scanned: `logs/` and `tmp/`
 */

// Specify the directories to scan
$directories = ['logs/', 'tmp/'];

// Function to scan directory and list files with last modified dates
function scanDirectory($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        echo "Directory '{$directory}' does not exist.\n";
        return;
    }

    // Open the directory
    $dirHandle = opendir($directory);
    if (!$dirHandle) {
        echo "Error: Unable to open directory '{$directory}'.\n";
        return;
    }

    echo "Scanning directory: {$directory}\n";

    // Loop through directory contents
    while (($file = readdir($dirHandle)) !== false) {
        // Skip special entries
        if ($file === '.' || $file === '..') {
            continue;
        }

        $filePath = $directory . $file;

        // Check if it's a file (not a subdirectory)
        if (is_file($filePath)) {
            // Get the last modified time of the file
            $lastModified = date("Y-m-d H:i:s", filemtime($filePath));
            echo "File: {$file}, Last Modified: {$lastModified}\n";
        }
    }

    // Close the directory handle
    closedir($dirHandle);
    echo "\n";
}

// Iterate over each directory and scan it
foreach ($directories as $directory) {
    scanDirectory($directory);
}

echo "Directory scan completed.\n";
?>
```
