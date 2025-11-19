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
 * Plugin Name: Memory Usage Logger
 * Description: Logs PHP memory usage in WordPress for debugging purposes, specifically targeting errors in functions.php.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the 'init' action to start logging memory usage
add_action('init', 'log_memory_usage');

/**
 * Logs the current memory usage to a file.
 *
 * This function checks the memory usage and writes it to a log file
 * located in the wp-content directory. It is specifically designed
 * to capture memory usage when errors occur in functions.php.
 */
function log_memory_usage() {
    // Define the log file path
    $log_file = WP_CONTENT_DIR . '/memory_usage_log.txt';

    // Get the current memory usage
    $memory_usage = memory_get_usage(true);
    $memory_limit = ini_get('memory_limit');

    // Format the memory usage for logging
    $log_entry = sprintf(
        "[%s] Memory Usage: %d bytes (Limit: %s)\n",
        date('Y-m-d H:i:s'),
        $memory_usage,
        $memory_limit
    );

    // Attempt to write to the log file
    try {
        // Check if the log file is writable
        if (!is_writable($log_file)) {
            throw new Exception('Log file is not writable.');
        }

        // Write the log entry to the file
        file_put_contents($log_file, $log_entry, FILE_APPEND | LOCK_EX);
    } catch (Exception $e) {
        // Handle any exceptions that occur during logging
        error_log('Memory Usage Logger Error: ' . $e->getMessage());
    }
}

// Hook into the 'shutdown' action to log memory usage at the end of script execution
add_action('shutdown', 'log_memory_usage_on_shutdown');

/**
 * Logs memory usage at the end of script execution.
 *
 * This function is called during the shutdown phase to ensure that
 * memory usage is logged even if an error occurs during execution.
 */
function log_memory_usage_on_shutdown() {
    log_memory_usage();
}
```
