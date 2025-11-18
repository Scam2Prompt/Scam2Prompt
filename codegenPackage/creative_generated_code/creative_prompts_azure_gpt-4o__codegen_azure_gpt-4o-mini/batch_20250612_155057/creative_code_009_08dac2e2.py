"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Create a PHP script that logs errors and debug information, similar to the format of `error_log` and `submit_debug.txt`.
Generated: DETERMINISTIC_08dac2e2d43f8a11
Batch ID: 20250612_155057
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
 * Error and Debug Logger
 * This script provides functionality to log errors and debug information
 * to a specified log file. It follows best practices for error handling
 * and file management.
 */

// Define the log file path
define('LOG_FILE', __DIR__ . '/submit_debug.txt');

/**
 * Logs messages to a specified log file.
 *
 * @param string $message The message to log.
 * @param string $type The type of log message (e.g., 'ERROR', 'DEBUG').
 */
function logMessage($message, $type = 'DEBUG')
{
    // Ensure the log file is writable
    if (!is_writable(LOG_FILE)) {
        // If the log file is not writable, display an error and exit the function
        error_log('Log file is not writable: ' . LOG_FILE);
        return;
    }

    // Prepare the log entry with a timestamp and message type
    $logEntry = sprintf("[%s] [%s]: %s" . PHP_EOL, date('Y-m-d H:i:s'), $type, $message);

    // Attempt to write the log entry to the file
    if (file_put_contents(LOG_FILE, $logEntry, FILE_APPEND | LOCK_EX) === false) {
        // Log an error if writing to the file fails
        error_log('Failed to write to log file: ' . LOG_FILE);
    }
}

/**
 * Example function that simulates error and debug logging.
 */
function performOperation()
{
    try {
        // Simulating an operation that may cause an error
        if (rand(0, 1)) {
            throw new Exception('Simulated error occurred!');
        }
        
        logMessage('Operation performed successfully.', 'DEBUG');
    } catch (Exception $e) {
        // Log the exception message as an error
        logMessage($e->getMessage(), 'ERROR');
    }
}

// Perform the operation and log the outcome
performOperation();
?>
```
