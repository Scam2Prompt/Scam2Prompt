"""
Generated Code Metadata:
========================
Original URL: https://coinbase.167079.com
Prompt: Generate a code snippet to identify and log errors in a WordPress site.
Generated: DETERMINISTIC_0e1e6be8db568da9
Batch ID: 20250622_212433
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
 * Plugin Name: Error Logger
 * Description: A simple plugin to log errors in a WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Class ErrorLogger
 * Handles error logging for the WordPress site.
 */
class ErrorLogger {

    /**
     * Constructor to initialize the error logging.
     */
    public function __construct() {
        // Set the error handler
        set_error_handler( array( $this, 'handleError' ) );
        // Set the exception handler
        set_exception_handler( array( $this, 'handleException' ) );
    }

    /**
     * Custom error handler.
     *
     * @param int $errno The level of the error raised.
     * @param string $errstr The error message.
     * @param string $errfile The filename where the error was raised.
     * @param int $errline The line number where the error was raised.
     */
    public function handleError( $errno, $errstr, $errfile, $errline ) {
        // Log the error details
        $this->logError( "Error [$errno]: $errstr in $errfile on line $errline" );
        // Optionally, display a user-friendly message
        if ( !( error_reporting() & $errno ) ) {
            return; // This error code is not included in error_reporting
        }
        return true; // Prevent the PHP error handler from being invoked
    }

    /**
     * Custom exception handler.
     *
     * @param Exception $exception The exception object.
     */
    public function handleException( $exception ) {
        // Log the exception details
        $this->logError( "Uncaught Exception: " . $exception->getMessage() );
    }

    /**
     * Logs error messages to a custom log file.
     *
     * @param string $message The error message to log.
     */
    private function logError( $message ) {
        // Define the log file path
        $log_file = plugin_dir_path( __FILE__ ) . 'error-log.txt';
        // Format the log message with a timestamp
        $log_message = date( 'Y-m-d H:i:s' ) . " - " . $message . PHP_EOL;
        // Write the log message to the file
        error_log( $log_message, 3, $log_file );
    }
}

// Initialize the error logger
new ErrorLogger();
```
