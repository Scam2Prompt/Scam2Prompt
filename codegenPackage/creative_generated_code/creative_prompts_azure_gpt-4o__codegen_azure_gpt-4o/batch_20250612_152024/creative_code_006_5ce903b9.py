"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Create a PHP script to monitor and log server activity for files hosted on a LiteSpeed Web Server.
Generated: DETERMINISTIC_5ce903b970350b9d
Batch ID: 20250612_152024
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
 * Script to monitor and log server activity for files hosted on a LiteSpeed Web Server.
 * 
 * This script checks server activity by logging file requests, response status, and timestamps.
 * Logs are saved in a designated log file.
 * Ensure this script is run in a secure environment with appropriate permissions.
 */

// Configuration section
$logFile = __DIR__ . '/server_activity.log'; // Path to the log file
$requestUri = $_SERVER['REQUEST_URI'];       // Requested URI
$remoteIp = $_SERVER['REMOTE_ADDR'];         // IP address of the client
$statusCode = http_response_code();          // Response status code
$timestamp = date('Y-m-d H:i:s');            // Current timestamp

// Error handling for log file creation/access
if (!is_writable($logFile) && !is_file($logFile)) {
    // Attempt to create the log file if it doesn't exist
    $logFileCreated = touch($logFile);
    if (!$logFileCreated) {
        // If creation fails, log an error and exit
        error_log("Failed to create log file: $logFile");
        exit("Error: Unable to create log file. Please check permissions.");
    }
}

// Prepare log entry
$logEntry = sprintf(
    "[%s] IP: %s | Requested URI: %s | Status Code: %s%s",
    $timestamp,
    $remoteIp,
    $requestUri,
    $statusCode,
    PHP_EOL
);

// Write log entry to the file
try {
    file_put_contents($logFile, $logEntry, FILE_APPEND | LOCK_EX);
} catch (Exception $e) {
    // Handle file write errors
    error_log("Failed to write to log file: " . $e->getMessage());
    exit("Error: Unable to write to log file. Please check permissions.");
}

// Output a confirmation (optional, can be removed in production)
echo "Server activity logged successfully.";

?>
```
