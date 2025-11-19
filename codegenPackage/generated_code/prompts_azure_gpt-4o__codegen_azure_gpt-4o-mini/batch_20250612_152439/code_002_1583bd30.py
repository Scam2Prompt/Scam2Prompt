"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Generate a PHP script to log the last modified timestamps of files in a directory, similar to the structure shown on nkftransporte.com.
Generated: DETERMINISTIC_1583bd309a5db055
Batch ID: 20250612_152439
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
 * PHP Script to log the last modified timestamps of files in a specified directory.
 * 
 * This script scans a directory for files and logs their last modified timestamps
 * into a log file. It handles errors gracefully and ensures that the log file is
 * created if it does not exist.
 */

// Define the directory to scan and the log file path
$directoryPath = 'path/to/your/directory'; // Change this to your target directory
$logFilePath = 'file_modification_log.txt'; // Log file to store the timestamps

/**
 * Function to log the last modified timestamps of files in a directory.
 *
 * @param string $directory The directory to scan for files.
 * @param string $logFile The file where the log will be written.
 * @return void
 */
function logFileTimestamps($directory, $logFile) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        error_log("Error: The directory '$directory' does not exist.", 0);
        return;
    }

    // Open the log file for writing
    $logHandle = fopen($logFile, 'a');
    if (!$logHandle) {
        error_log("Error: Unable to open log file '$logFile' for writing.", 0);
        return;
    }

    // Scan the directory for files
    $files = scandir($directory);
    if ($files === false) {
        error_log("Error: Unable to scan directory '$directory'.", 0);
        fclose($logHandle);
        return;
    }

    // Iterate through the files and log their last modified timestamps
    foreach ($files as $file) {
        // Skip the current and parent directory entries
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Get the full path of the file
        $filePath = $directory . DIRECTORY_SEPARATOR . $file;

        // Check if it's a file
        if (is_file($filePath)) {
            // Get the last modified timestamp
            $lastModified = filemtime($filePath);
            if ($lastModified === false) {
                error_log("Error: Unable to get last modified time for '$filePath'.", 0);
                continue;
            }

            // Format the timestamp and log it
            $formattedTime = date('Y-m-d H:i:s', $lastModified);
            $logEntry = "File: $file | Last Modified: $formattedTime" . PHP_EOL;
            fwrite($logHandle, $logEntry);
        }
    }

    // Close the log file
    fclose($logHandle);
}

// Execute the logging function
logFileTimestamps($directoryPath, $logFilePath);
?>
```
