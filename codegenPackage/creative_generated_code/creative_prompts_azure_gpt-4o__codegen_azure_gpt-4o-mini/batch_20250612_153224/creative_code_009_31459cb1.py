"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storebari.com
Prompt: Provide a solution to handle fatal errors in the Astra Sites plugin by implementing a custom error handler in `class-astra-sites-error-handler.php`.
Generated: DETERMINISTIC_31459cb146c793ea
Batch ID: 20250612_153224
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
 * Class Astra_Sites_Error_Handler
 *
 * Custom error handler for the Astra Sites plugin.
 * This class handles fatal errors gracefully and logs them for further investigation.
 */

class Astra_Sites_Error_Handler {

    /**
     * Constructor to set the custom error handler.
     */
    public function __construct() {
        // Set the custom error handler
        set_error_handler([$this, 'handleError']);
        register_shutdown_function([$this, 'handleShutdown']);
    }

    /**
     * Custom error handler function.
     *
     * @param int    $errno   The error level.
     * @param string $errstr  The error message.
     * @param string $errfile The filename where the error was raised.
     * @param int    $errline The line number where the error was raised.
     *
     * @return bool
     */
    public function handleError($errno, $errstr, $errfile, $errline) {
        // Log the error to a file for further analysis
        error_log("Error [$errno]: $errstr in $errfile on line $errline", 3, __DIR__ . '/error.log');

        // Display a user-friendly message (not to expose sensitive details)
        if ($errno !== E_NOTICE && $errno !== E_WARNING) {
            echo "An unexpected error occurred. Please try again later.";
            exit();
        }

        // Allow the default error handler to continue for non-fatal errors
        return false;
    }

    /**
     * Shutdown function to handle fatal errors.
     */
    public function handleShutdown() {
        $error = error_get_last();
        if ($error !== null) {
            // Log the fatal error
            error_log("Fatal Error: {$error['message']} in {$error['file']} on line {$error['line']}", 3, __DIR__ . '/error.log');

            // Display a user-friendly message
            echo "A fatal error occurred. Please try again later.";
            exit();
        }
    }
}

// Instantiate the error handler
new Astra_Sites_Error_Handler();
```
