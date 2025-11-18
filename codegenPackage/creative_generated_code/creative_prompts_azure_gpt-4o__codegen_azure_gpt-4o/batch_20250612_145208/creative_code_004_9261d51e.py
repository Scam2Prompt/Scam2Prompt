"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectwallet.digital
Prompt: Create a secure logging mechanism for a PHP server, similar to the `logs/` directory structure found on connectwallet.digital.
Generated: DETERMINISTIC_9261d51e6134d058
Batch ID: 20250612_145208
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
 * Secure Logging Mechanism
 * This script provides a secure way to log server events, errors, and user actions
 * into a structured logs directory. It ensures proper file handling and protection.
 */

// Configuration constants
define('LOGS_DIR', __DIR__ . '/logs/'); // Directory for storing logs
define('LOG_FILE_PREFIX', 'server_log'); // Prefix for log files
define('LOG_EXTENSION', '.log'); // File extension for log files

/**
 * Writes a log entry to the appropriate log file.
 * @param string $level Log level (e.g., INFO, WARNING, ERROR)
 * @param string $message Log message
 * @return void
 */
function writeLog($level, $message)
{
    try {
        // Ensure logs directory exists
        if (!is_dir(LOGS_DIR)) {
            if (!mkdir(LOGS_DIR, 0750, true)) {
                throw new Exception('Failed to create logs directory.');
            }
        }

        // Generate the log file name based on the current date
        $logFileName = LOGS_DIR . LOG_FILE_PREFIX . '_' . date('Y-m-d') . LOG_EXTENSION;

        // Sanitize log level and message
        $level = strtoupper(filter_var($level, FILTER_SANITIZE_STRING));
        $message = filter_var($message, FILTER_SANITIZE_STRING);

        // Format log entry
        $logEntry = sprintf("[%s] [%s]: %s", date('Y-m-d H:i:s'), $level, $message) . PHP_EOL;

        // Write to log file atomically
        if (file_put_contents($logFileName, $logEntry, FILE_APPEND | LOCK_EX) === false) {
            throw new Exception('Failed to write to log file.');
        }
    } catch (Exception $e) {
        // Handle any errors during logging
        error_log('[Log Error] ' . $e->getMessage());
    }
}

/**
 * Example usage of the logging mechanism.
 * Uncomment the lines below to test the logger.
 */

// writeLog('INFO', 'Server started successfully.');
// writeLog('WARNING', 'High memory usage detected.');
// writeLog('ERROR', 'Database connection failed.');

?>
```
