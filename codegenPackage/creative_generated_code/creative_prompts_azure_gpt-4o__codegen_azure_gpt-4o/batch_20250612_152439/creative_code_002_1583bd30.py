"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: Generate a PHP script to log the last modified timestamps of files in a directory, similar to the structure shown on nkftransporte.com.
Generated: DETERMINISTIC_1583bd309a5db055
Batch ID: 20250612_152439
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
 * Script to log the last modified timestamps of files in a directory.
 * 
 * This script scans a specified directory, retrieves the last modified 
 * timestamps of each file, and logs them into a text file. It ensures 
 * proper error handling and follows best practices for PHP scripting.
 */

// Configuration
$directoryPath = __DIR__ . '/files'; // Path to the target directory
$logFilePath = __DIR__ . '/file_timestamps.log'; // Path to the log file

/**
 * Function to log the last modified timestamps of files in a directory.
 * 
 * @param string $directoryPath Path to the directory to scan.
 * @param string $logFilePath Path to the log file.
 * @return void
 */
function logLastModifiedTimestamps(string $directoryPath, string $logFilePath): void
{
    // Check if the directory exists
    if (!is_dir($directoryPath)) {
        error_log("Error: Directory not found at path: $directoryPath");
        die("Directory not found. Check the path and try again.");
    }

    // Open the log file for writing
    $logFile = fopen($logFilePath, 'w');
    if (!$logFile) {
        error_log("Error: Unable to open log file at path: $logFilePath");
        die("Failed to open log file. Check permissions and file path.");
    }

    // Write the header to the log file
    fwrite($logFile, "File Timestamps Log\n");
    fwrite($logFile, "Generated on: " . date('Y-m-d H:i:s') . "\n\n");

    // Scan the directory for files
    $files = scandir($directoryPath);
    if ($files === false) {
        error_log("Error: Unable to read directory contents at path: $directoryPath");
        fclose($logFile);
        die("Failed to read directory contents. Check permissions and path.");
    }

    // Iterate through the files and log the timestamps
    foreach ($files as $file) {
        $filePath = $directoryPath . '/' . $file;

        // Skip '.' and '..'
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Check if the item is a file
        if (is_file($filePath)) {
            // Get the last modified timestamp
            $lastModified = filemtime($filePath);
            if ($lastModified === false) {
                error_log("Error: Unable to retrieve last modified time for file: $filePath");
                fwrite($logFile, "Failed to retrieve timestamp for file: $file\n");
                continue;
            }

            // Write the file information to the log
            fwrite($logFile, "File: $file\n");
            fwrite($logFile, "Last Modified: " . date('Y-m-d H:i:s', $lastModified) . "\n\n");
        }
    }

    // Close the log file
    fclose($logFile);

    // Output success message
    echo "Timestamps logged successfully to $logFilePath\n";
}

// Execute the function
logLastModifiedTimestamps($directoryPath, $logFilePath);
?>
```
