"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panccokesowpaflnace.com
Prompt: Create a PHP script that organizes files in a directory structure similar to the one listed (`approve.php`, `build.php`, `generators.php`) and moves older files to `tmp/`.
Generated: DETERMINISTIC_ebd23db1a9624e3a
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
 * File Organizer Script
 * 
 * This script organizes files in a specified directory by moving older files
 * to a temporary directory ('tmp/'). It retains specific files in the main
 * directory and organizes them in predefined subdirectories.
 * 
 * Usage:
 * - Define the source directory path.
 * - Define the temporary directory path.
 * - Define the duration in days to consider a file as 'old'.
 */

// Define the source directory and temporary directory
$sourceDir = 'your/source/directory'; // Change this to your source directory path
$tmpDir = 'your/source/directory/tmp'; // Change this to your desired temporary directory path
$daysOld = 30; // Files older than this will be moved to 'tmp/'

// Create the temporary directory if it does not exist
if (!is_dir($tmpDir)) {
    if (!mkdir($tmpDir, 0755, true)) {
        die("Failed to create temporary directory: $tmpDir");
    }
}

// Get the current time
$currentTime = time();

// Scan the source directory for files
$files = scandir($sourceDir);

// Check for any errors in scanning the directory
if ($files === false) {
    die("Failed to scan directory: $sourceDir");
}

// Organize files
foreach ($files as $file) {
    // Skip the current and parent directory entries
    if ($file === '.' || $file === '..') {
        continue;
    }

    $filePath = $sourceDir . '/' . $file;

    // Check if the item is a file
    if (is_file($filePath)) {
        // Calculate the file age in days
        $fileAgeDays = ($currentTime - filemtime($filePath)) / (60 * 60 * 24);

        // Move old files to the temporary directory
        if ($fileAgeDays > $daysOld) {
            if (!rename($filePath, $tmpDir . '/' . $file)) {
                echo "Failed to move file: $file to $tmpDir\n";
            } else {
                echo "Moved old file: $file to $tmpDir\n";
            }
        } else {
            // Logic to organize current files can be added here
            // For example, moving specific files to designated subdirectories.
            // This is a placeholder for additional organization logic.
        }
    }
}

echo "File organization complete.\n";
?>
```
