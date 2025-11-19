"""
Generated Code Metadata:
========================
Original URL: https://it10.alhuda.com.pk
Prompt: Write a script to log PHP memory usage in WordPress for debugging purposes, specifically targeting errors in `functions.php`.
Generated: DETERMINISTIC_c43a325a2079d258
Batch ID: 20250612_152109
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
 * Log PHP memory usage in WordPress for debugging purposes.
 *
 * This script targets errors in functions.php and logs memory usage.
 *
 * @package WordPress
 */

// Define the log file path
$log_file_path = wp_log_dir() . 'memory-usage.log';

/**
 * Log memory usage to a file.
 *
 * @param string $message The message to log.
 */
function log_memory_usage($message) {
    global $log_file_path;
    
    // Check if the log file is writable
    if (!is_writable($log_file_path)) {
        error_log("Error: Log file $log_file_path is not writable.");
        return;
    }
    
    // Get current memory usage
    $memory_usage = memory_get_usage(true);
    $peak_memory_usage = memory_get_peak_usage(true);
    
    // Format the log message
    $log_message = sprintf(
        "%s - Memory usage: %d KB, Peak memory usage: %d KB\n",
        date('Y-m-d H:i:s'),
        $memory_usage / 1024,
        $peak_memory_usage / 1024
    );
    
    // Append the log message to the file
    file_put_contents($log_file_path, $log_message . $message . "\n", FILE_APPEND);
}

/**
 * Hook into WordPress to log memory usage on errors in functions.php.
 */
function log_memory_usage_on_error($error) {
    // Check if the error occurred in functions.php
    if (strpos($error['file'], 'functions.php') !== false) {
        $message = sprintf(
            "Error in %s on line %d: %s\n",
            $error['file'],
            $error['line'],
            $error['message']
        );
        log_memory_usage($message);
    }
}

// Hook into WordPress error handling
set_error_handler('log_memory_usage_on_error');

// Example usage:
// trigger_error('Test error in functions.php', E_USER_ERROR);
```
