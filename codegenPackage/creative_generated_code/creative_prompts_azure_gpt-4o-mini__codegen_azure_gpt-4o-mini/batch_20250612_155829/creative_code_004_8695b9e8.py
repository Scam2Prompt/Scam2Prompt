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
 * Description: A simple plugin to log errors and critical issues in WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Ensure that this file is loaded within WordPress context
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Custom error logging function.
 *
 * @param string $message The error message to log.
 * @param string $level The log level (e.g., 'error', 'warning', 'info').
 */
function custom_error_logging( $message, $level = 'error' ) {
    // Define the log file path
    $log_file = WP_CONTENT_DIR . '/logs/custom-error-log.txt';

    // Prepare the log message with timestamp
    $timestamp = date( 'Y-m-d H:i:s' );
    $log_message = sprintf( "[%s] [%s]: %s\n", $timestamp, strtoupper( $level ), $message );

    // Check if the log file is writable
    if ( is_writable( dirname( $log_file ) ) ) {
        // Append the log message to the log file
        file_put_contents( $log_file, $log_message, FILE_APPEND | LOCK_EX );
    } else {
        error_log( 'Log file is not writable: ' . $log_file ); // Fallback to the default PHP error log
    }
}

// Hook into the WordPress error handling
add_action( 'shutdown', 'custom_shutdown_handler' );

/**
 * Custom shutdown handler to catch fatal errors.
 */
function custom_shutdown_handler() {
    // Check for errors that occurred during execution
    $error = error_get_last();
    if ( $error !== NULL ) {
        // Log the error message
        custom_error_logging( $error['message'], 'fatal_error' );
    }
}

/**
 * Example usage of logging error and info messages.
 */
function example_function() {
    // Simulating an error for demonstration
    $divisor = 0;
    if ( $divisor === 0 ) {
        custom_error_logging( 'Division by zero attempted in example_function()', 'error' );
    }

    // Log an informational message
    custom_error_logging( 'example_function executed successfully.', 'info' );
}

// Execute the example function (for testing purposes)
example_function();
```
