"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.newtork.cc
Prompt: Generate PHP code to log and monitor access to a file named `key.php` on an Apache server.
Generated: DETERMINISTIC_834ae9c2c4ae6b54
Batch ID: 20250612_154115
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
 * File: monitor_access.php
 * Purpose: Logs and monitors access to a file named 'key.php'
 * Author: [Your Name]
 * Date: [Date]
 */

// Define the log file path
define('ACCESS_LOG_FILE', __DIR__ . '/access.log');

// Function to log access attempts
function logAccess($ipAddress, $timestamp, $userAgent, $requestedFile)
{
    // Construct log entry
    $logEntry = sprintf(
        "[%s] IP: %s | User-Agent: %s | File: %s\n",
        $timestamp,
        $ipAddress,
        $userAgent,
        $requestedFile
    );

    // Append the log entry to the file
    file_put_contents(ACCESS_LOG_FILE, $logEntry, FILE_APPEND);
}

// Function to handle errors gracefully
function handleErrors($errno, $errstr, $errfile, $errline)
{
    // Log the error to the PHP error log
    error_log("Error [$errno]: $errstr in $errfile on line $errline");
}

// Set custom error handler
set_error_handler('handleErrors');

// Check if the requested file is 'key.php'
if (basename($_SERVER['PHP_SELF']) === 'key.php') {
    // Get details about the request
    $ipAddress = $_SERVER['REMOTE_ADDR'] ?? 'UNKNOWN_IP';
    $timestamp = date('Y-m-d H:i:s');
    $userAgent = $_SERVER['HTTP_USER_AGENT'] ?? 'UNKNOWN_USER_AGENT';
    $requestedFile = $_SERVER['PHP_SELF'];

    // Log the access
    logAccess($ipAddress, $timestamp, $userAgent, $requestedFile);

    // Additional monitoring actions (if any) can be added here
}

// The rest of your 'key.php' file handling code goes below
?>
```
