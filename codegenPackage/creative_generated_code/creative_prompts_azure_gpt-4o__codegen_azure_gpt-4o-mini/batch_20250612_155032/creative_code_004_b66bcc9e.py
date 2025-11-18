"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinnbase.ltd
Prompt: Write PHP code to log errors from a WordPress plugin into a custom error log file for debugging purposes.
Generated: DETERMINISTIC_b66bcc9ed3e0e5df
Batch ID: 20250612_155032
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
 * Description: A simple WordPress plugin to log errors to a custom error log file.
 * Version: 1.0
 * Author: Your Name
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Custom error logging function.
 *
 * @param string $error_message The error message to log.
 */
function custom_error_log( $error_message ) {
    // Define the custom log file path
    $log_file = plugin_dir_path( __FILE__ ) . 'custom-error-log.txt';

    // Create the log message with a timestamp
    $timestamp = date( 'Y-m-d H:i:s' );
    $log_message = "[$timestamp] ERROR: $error_message" . PHP_EOL;

    // Try to write the log message to the file
    try {
        if ( ! file_exists( $log_file ) ) {
            // Create the log file if it doesn't exist
            touch( $log_file );
        }

        // Append the log message to the file
        file_put_contents( $log_file, $log_message, FILE_APPEND | LOCK_EX );
    } catch ( Exception $e ) {
        // Handle any exceptions that occur during logging
        error_log( "Failed to write to custom error log: " . $e->getMessage() );
    }
}

/**
 * Hook to handle errors in WordPress.
 */
add_action( 'wp_ajax_my_custom_action', 'handle_custom_action' );

/**
 * Handles a custom AJAX action.
 */
function handle_custom_action() {
    // Simulate an error for demonstration purposes
    $error_occurred = true; // Change this to false to simulate no error

    if ( $error_occurred ) {
        custom_error_log( 'An error occurred during the AJAX action.' );
        wp_send_json_error( 'An error occurred. Please check the error log.' );
    } else {
        wp_send_json_success( 'Action completed successfully.' );
    }
}

// Register the custom error handler
set_error_handler( function ( $errno, $errstr, $errfile, $errline ) {
    // Prepare the error message
    $error_message = "Error [$errno]: $errstr in $errfile on line $errline";
    custom_error_log( $error_message );

    // Optionally display an error message to the user
    if ( error_reporting() !== 0 ) { // Prevents throwing errors in @ operator
        echo "An error occurred. Please check the error log.";
    }
});

// Shutdown function to catch fatal errors
register_shutdown_function( function () {
    $error = error_get_last();
    if ( $error !== null ) {
        custom_error_log( 'Fatal error: ' . $error['message'] . ' in ' . $error['file'] . ' on line ' . $error['line'] );
    }
} );

?>
```
