"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://it10.alhuda.com.pk
Prompt: Write a script to log PHP memory usage in WordPress for debugging purposes, specifically targeting errors in `functions.php`.
Generated: DETERMINISTIC_c43a325a2079d258
Batch ID: 20250612_152109
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
 * Plugin Name: Memory Usage Logger for functions.php
 * Description: Logs PHP memory usage in WordPress specifically targeting errors in functions.php.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the 'init' action to start the memory logging process
add_action('init', 'log_memory_usage');

function log_memory_usage() {
    // Ensure we are in the admin area or during debug mode
    if (is_admin() || defined('WP_DEBUG') && WP_DEBUG) {
        // Register an error handler to catch errors in functions.php
        set_error_handler('memory_usage_error_handler');
    }
}

/**
 * Custom error handler to log memory usage when an error occurs.
 *
 * @param int    $errno   The level of the error raised.
 * @param string $errstr  The error message.
 * @param string $errfile The filename that the error was raised in.
 * @param int    $errline The line number the error was raised at.
 */
function memory_usage_error_handler($errno, $errstr, $errfile, $errline) {
    // Check if the error occurred in functions.php
    if (strpos($errfile, 'functions.php') !== false) {
        // Get current memory usage
        $memoryUsage = memory_get_usage(true);
        // Format the memory usage for logging
        $formattedMemoryUsage = format_memory($memoryUsage);

        // Prepare the log message
        $logMessage = sprintf(
            "[%s] ERROR: %s in %s on line %d - Memory Usage: %s\n",
            date('Y-m-d H:i:s'),
            $errstr,
            $errfile,
            $errline,
            $formattedMemoryUsage
        );

        // Log the message to debug.log
        error_log($logMessage);
    }
}

/**
 * Format the memory usage into a human-readable string.
 *
 * @param int $memoryInBytes Memory usage in bytes.
 * @return string Formatted memory usage.
 */
function format_memory($memoryInBytes) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $factor = floor((strlen($memoryInBytes) - 1) / 3);
    return number_format($memoryInBytes / pow(1024, $factor), 2) . ' ' . $units[$factor];
}

// Ensure to restore the previous error handler on shutdown
register_shutdown_function(function() {
    restore_error_handler();
});
```
