"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon-farming.pro
Prompt: Write a PHP script that logs and timestamps access to a file like `key.php` on an Apache server.
Generated: DETERMINISTIC_73d7545a31955de6
Batch ID: 20250612_154151
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
 * Access Logger for key.php
 *
 * This script logs the access to the key.php file, including the timestamp,
 * client IP address, and user agent. The log is appended to a specified log file.
 */

// Define the log file path
define('LOG_FILE', 'access_log.txt');

/**
 * Function to log the access details
 *
 * @param string $logFile The path to the log file
 * @return void
 */
function logAccess($logFile) {
    // Get the current timestamp
    $timestamp = date('Y-m-d H:i:s');

    // Get the client IP address
    $ipAddress = $_SERVER['REMOTE_ADDR'];

    // Get the user agent
    $userAgent = $_SERVER['HTTP_USER_AGENT'];

    // Create the log entry
    $logEntry = sprintf("[%s] IP: %s | User-Agent: %s\n", $timestamp, $ipAddress, $userAgent);

    // Attempt to write to the log file
    try {
        // Check if the log file is writable
        if (is_writable($logFile)) {
            // Append the log entry to the log file
            file_put_contents($logFile, $logEntry, FILE_APPEND | LOCK_EX);
        } else {
            throw new Exception("Log file is not writable.");
        }
    } catch (Exception $e) {
        // Log error message to a system error log for debugging
        error_log($e->getMessage());
    }
}

// Log the access
logAccess(LOG_FILE);

// Rest of the key.php code can go here
// For example, displaying a simple message
echo "Access logged successfully.";
?>
```
