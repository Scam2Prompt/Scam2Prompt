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
 * PHP script to log the last modified timestamps of files in a specified directory.
 * 
 * This script scans a directory for files and logs their last modified timestamps
 * into a text file. It is designed to handle errors gracefully and provides clear
 * feedback about the process.
 */

// Define the directory to scan and the log file path
define('DIRECTORY_TO_SCAN', '/path/to/your/directory'); // Change this to the directory you want to scan
define('LOG_FILE_PATH', '/path/to/your/logfile.txt');  // Change this to where you want to save the log file

/**
 * Function to log the last modified timestamp of files in the specified directory.
 *
 * @param string $directory The directory to scan for files.
 * @param string $logFile The path to the log file where timestamps will be saved.
 * @return void
 */
function logFileTimestamps($directory, $logFile) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        die("Error: The specified directory does not exist: $directory\n");
    }

    // Open the log file for writing
    $logHandle = fopen($logFile, 'w');
    if ($logHandle === false) {
        die("Error: Unable to open log file for writing: $logFile\n");
    }

    // Scan the directory for files
    $files = scandir($directory);
    if ($files === false) {
        fclose($logHandle);
        die("Error: Unable to scan directory: $directory\n");
    }

    // Loop through the files and log their last modified timestamps
    foreach ($files as $file) {
        // Skip the current and parent directory entries
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Get the full path of the file
        $filePath = $directory . DIRECTORY_SEPARATOR . $file;

        // Check if the current entry is a file
        if (is_file($filePath)) {
            // Get the last modified timestamp
            $lastModified = filemtime($filePath);
            if ($lastModified === false) {
                echo "Warning: Unable to get last modified time for file: $filePath\n";
                continue;
            }

            // Format and write the timestamp to the log file
            $logEntry = sprintf("%s - %s\n", date('Y-m-d H:i:s', $lastModified), $file);
            fwrite($logHandle, $logEntry);
        }
    }

    // Close the log file
    fclose($logHandle);

    echo "Log written to $logFile successfully.\n";
}

// Execute the logging function
logFileTimestamps(DIRECTORY_TO_SCAN, LOG_FILE_PATH);
?>
```

Make sure to adjust `DIRECTORY_TO_SCAN` and `LOG_FILE_PATH` to the appropriate paths before running the script.
