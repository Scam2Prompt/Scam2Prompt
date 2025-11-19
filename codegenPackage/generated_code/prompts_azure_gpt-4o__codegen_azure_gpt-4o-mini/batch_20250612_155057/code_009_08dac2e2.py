"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Create a PHP script that logs errors and debug information, similar to the format of `error_log` and `submit_debug.txt`.
Generated: DETERMINISTIC_08dac2e2d43f8a11
Batch ID: 20250612_155057
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
 * Error and Debug Logger
 * 
 * This script provides functionality to log errors and debug information
 * to a specified log file. It can be used to track issues and monitor
 * application behavior in a production environment.
 */

// Define the log file path
define('LOG_FILE', __DIR__ . '/submit_debug.txt');

/**
 * Logs a message to the specified log file.
 *
 * @param string $message The message to log.
 * @param string $level The level of the log (INFO, ERROR, DEBUG).
 * @return void
 */
function logMessage($message, $level = 'INFO') {
    // Ensure the log level is valid
    $validLevels = ['INFO', 'ERROR', 'DEBUG'];
    if (!in_array($level, $validLevels)) {
        throw new InvalidArgumentException('Invalid log level: ' . $level);
    }

    // Create a timestamp for the log entry
    $timestamp = date('Y-m-d H:i:s');

    // Format the log entry
    $logEntry = sprintf("[%s] [%s] %s\n", $timestamp, $level, $message);

    // Attempt to write the log entry to the log file
    try {
        if (file_put_contents(LOG_FILE, $logEntry, FILE_APPEND | LOCK_EX) === false) {
            throw new RuntimeException('Failed to write to log file: ' . LOG_FILE);
        }
    } catch (Exception $e) {
        // Handle any exceptions that occur during logging
        error_log('Logging error: ' . $e->getMessage());
    }
}

// Example usage
try {
    // Log an informational message
    logMessage('Application started.');

    // Simulate an error
    if (!file_exists('somefile.txt')) {
        logMessage('File not found: somefile.txt', 'ERROR');
    }

    // Log a debug message
    logMessage('Debugging application state.', 'DEBUG');

} catch (Exception $e) {
    // Log any unexpected exceptions
    logMessage('Unexpected error: ' . $e->getMessage(), 'ERROR');
}
?>
```
