"""
Generated Code Metadata:
========================
Original URL: https://storebari.com
Prompt: How can I debug and fix the error in `class-astra-sites-error-handler.php` on line 50 for the Astra Sites WordPress plugin? Provide code examples or steps specific to this plugin.
Generated: DETERMINISTIC_61265cec50275898
Batch ID: 20250612_153224
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
 * Astra Sites Error Handler Class
 *
 * This class handles errors for the Astra Sites plugin.
 *
 * @package Astra_Sites
 */

class Astra_Sites_Error_Handler {

    /**
     * Constructor to initialize the error handler.
     */
    public function __construct() {
        // Set the error handler
        set_error_handler([$this, 'handleError']);
    }

    /**
     * Custom error handler function.
     *
     * @param int    $errno   The level of the error raised.
     * @param string $errstr  The error message.
     * @param string $errfile The filename where the error was raised.
     * @param int    $errline The line number where the error was raised.
     *
     * @return void
     */
    public function handleError($errno, $errstr, $errfile, $errline) {
        // Check if error reporting is enabled
        if (!(error_reporting() & $errno)) {
            return; // This error code is not included in error_reporting
        }

        // Log the error details
        error_log("Error [$errno]: $errstr in $errfile on line $errline");

        // Display a user-friendly message
        if (defined('WP_DEBUG') && WP_DEBUG) {
            echo "<b>Error:</b> [$errno] $errstr in $errfile on line $errline<br>";
        } else {
            echo "<b>An error occurred. Please try again later.</b>";
        }

        // Prevent the PHP internal error handler from being invoked
        return true;
    }

    /**
     * Function to trigger an error for testing purposes.
     *
     * @return void
     */
    public function triggerError() {
        // Example of triggering an error
        trigger_error("This is a test error!", E_USER_NOTICE);
    }
}

// Initialize the error handler
$error_handler = new Astra_Sites_Error_Handler();

// Example usage: Uncomment to trigger an error for testing
// $error_handler->triggerError();
```
