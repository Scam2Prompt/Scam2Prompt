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
 * Logs the last modified timestamps of files in a directory.
 *
 * @author [Your Name]
 */

// Configuration
$directoryPath = '/path/to/directory'; // Directory to scan for files
$logFilePath = '/path/to/logfile.log'; // Path to log file

// Check if directory and log file paths are set
if (empty($directoryPath) || empty($logFilePath)) {
    throw new Exception('Directory and log file paths must be set.');
}

// Check if directory exists
if (!file_exists($directoryPath)) {
    throw new Exception("Directory '$directoryPath' does not exist.");
}

// Check if log file is writable
if (file_exists($logFilePath) && !is_writable($logFilePath)) {
    throw new Exception("Log file '$logFilePath' is not writable.");
}

// Function to get last modified timestamp of files in a directory
function getLastModifiedTimestamps($directoryPath) {
    $lastModifiedTimestamps = [];

    try {
        // Open directory
        $dirHandle = opendir($directoryPath);
        if ($dirHandle === false) {
            throw new Exception("Failed to open directory '$directoryPath'.");
        }

        // Iterate through directory
        while (($filename = readdir($dirHandle)) !== false) {
            // Skip current and parent directories
            if ($filename == '.' || $filename == '..') {
                continue;
            }

            // Construct full file path
            $filePath = $directoryPath . DIRECTORY_SEPARATOR . $filename;

            // Check if file is a regular file (not a directory)
            if (is_file($filePath)) {
                // Get last modified timestamp
                $lastModifiedTimestamp = filemtime($filePath);

                // Add to array
                $lastModifiedTimestamps[$filename] = $lastModifiedTimestamp;
            }
        }

        // Close directory
        closedir($dirHandle);
    } catch (Exception $e) {
        echo "Error reading directory: " . $e->getMessage() . PHP_EOL;
    }

    return $lastModifiedTimestamps;
}

// Function to log last modified timestamps
function logLastModifiedTimestamps($lastModifiedTimestamps, $logFilePath) {
    try {
        // Open log file for writing
        $logFileHandle = fopen($logFilePath, 'a');
        if ($logFileHandle === false) {
            throw new Exception("Failed to open log file '$logFilePath' for writing.");
        }

        // Log last modified timestamps
        foreach ($lastModifiedTimestamps as $filename => $lastModifiedTimestamp) {
            $logMessage = date('Y-m-d H:i:s', $lastModifiedTimestamp) . " - $filename" . PHP_EOL;
            fwrite($logFileHandle, $logMessage);
        }

        // Close log file
        fclose($logFileHandle);
    } catch (Exception $e) {
        echo "Error writing to log file: " . $e->getMessage() . PHP_EOL;
    }
}

// Main
try {
    // Get last modified timestamps
    $lastModifiedTimestamps = getLastModifiedTimestamps($directoryPath);

    // Log last modified timestamps
    logLastModifiedTimestamps($lastModifiedTimestamps, $logFilePath);

    echo "Last modified timestamps logged successfully." . PHP_EOL;
} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage() . PHP_EOL;
}
```
