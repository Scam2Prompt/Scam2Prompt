"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.699539.com
Prompt: How do I implement error logging in WordPress to diagnose critical errors similar to those on the Coinbase page?
Generated: DETERMINISTIC_8695b9e89c89a135
Batch ID: 20250612_155829
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
 * Plugin Name: Custom Error Logger
 * Description: Logs critical errors in WordPress to a custom log file for debugging purposes.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Log errors to a custom log file.
 *
 * @param string $error_message The error message to log.
 */
function custom_log_error($error_message) {
    // Define the log file path in the wp-content directory.
    $log_file = WP_CONTENT_DIR . '/custom-error-log.log';

    // Create or append the error message to the log file.
    $timestamp = date('Y-m-d H:i:s');
    $formatted_message = "[{$timestamp}] ERROR: {$error_message}" . PHP_EOL;

    // Use error suppression to handle potential file write errors gracefully.
    @file_put_contents($log_file, $formatted_message, FILE_APPEND | LOCK_EX);
}

/**
 * Handle PHP errors and log them.
 *
 * @param int $error_level Error level (severity).
 * @param string $error_message Error message.
 * @param string $error_file File in which the error occurred.
 * @param int $error_line Line number where the error occurred.
 */
function custom_php_error_handler($error_level, $error_message, $error_file, $error_line) {
    // Only log critical errors (E_ERROR, E_USER_ERROR, etc.).
    if (in_array($error_level, [E_ERROR, E_USER_ERROR, E_CORE_ERROR, E_COMPILE_ERROR, E_RECOVERABLE_ERROR])) {
        $log_message = "An error occurred in {$error_file} on line {$error_line}: {$error_message}";
        custom_log_error($log_message);
    }
}
set_error_handler('custom_php_error_handler');

/**
 * Handle WordPress shutdown and check for fatal errors.
 */
function custom_shutdown_handler() {
    $error = error_get_last();

    // Log fatal errors (e.g., syntax errors or memory issues).
    if ($error && in_array($error['type'], [E_ERROR, E_CORE_ERROR, E_COMPILE_ERROR, E_PARSE])) {
        $log_message = "Fatal error: {$error['message']} in {$error['file']} on line {$error['line']}";
        custom_log_error($log_message);
    }
}
add_action('shutdown', 'custom_shutdown_handler');

/**
 * Handle uncaught exceptions and log them.
 *
 * @param Throwable $exception The uncaught exception.
 */
function custom_exception_handler($exception) {
    $log_message = "Uncaught exception: " . $exception->getMessage() .
        " in " . $exception->getFile() .
        " on line " . $exception->getLine();
    custom_log_error($log_message);
}
set_exception_handler('custom_exception_handler');

// Ensure proper permissions for the log file on plugin activation.
register_activation_hook(__FILE__, function () {
    $log_file = WP_CONTENT_DIR . '/custom-error-log.log';

    // Create the log file if it does not exist.
    if (!file_exists($log_file)) {
        @file_put_contents($log_file, '');
    }

    // Set proper file permissions.
    @chmod($log_file, 0664);
});

// Clean up the log file on plugin deactivation.
register_deactivation_hook(__FILE__, function () {
    $log_file = WP_CONTENT_DIR . '/custom-error-log.log';

    // Optionally delete the log file on deactivation.
    if (file_exists($log_file)) {
        @unlink($log_file);
    }
});
```
