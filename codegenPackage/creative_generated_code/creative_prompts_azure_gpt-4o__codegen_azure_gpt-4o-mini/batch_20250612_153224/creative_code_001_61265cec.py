"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storebari.com
Prompt: How can I debug and fix the error in `class-astra-sites-error-handler.php` on line 50 for the Astra Sites WordPress plugin? Provide code examples or steps specific to this plugin.
Generated: DETERMINISTIC_61265cec50275898
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
 * Astra Sites Error Handler
 *
 * This class handles errors for the Astra Sites WordPress plugin.
 */
class Astra_Sites_Error_Handler {

    /**
     * Constructor to initialize error handling.
     */
    public function __construct() {
        // Register error handling methods.
        set_error_handler([$this, 'handleErrors']);
        set_exception_handler([$this, 'handleExceptions']);
    }

    /**
     * Custom error handler.
     *
     * @param int $errno The error level.
     * @param string $errstr The error message.
     * @param string $errfile The filename where the error occurred.
     * @param int $errline The line number where the error occurred.
     */
    public function handleErrors($errno, $errstr, $errfile, $errline) {
        // Log the error details for debugging
        error_log("Error [$errno]: $errstr in $errfile on line $errline");

        // Display a user-friendly error message if not in development mode
        if (defined('WP_DEBUG') && WP_DEBUG) {
            echo "An error occurred: $errstr";
        } else {
            echo "Something went wrong. Please try again later.";
        }

        // Stop script execution if it's a critical error
        if ($errno === E_ERROR || $errno === E_CORE_ERROR || $errno === E_COMPILE_ERROR) {
            exit(1);
        }
    }

    /**
     * Custom exception handler.
     *
     * @param Exception $exception The exception object.
     */
    public function handleExceptions($exception) {
        // Log exception details for debugging
        error_log("Uncaught exception: " . $exception->getMessage());

        // Display a user-friendly error message
        echo "An unexpected error occurred. Please contact support.";

        // Stop script execution
        exit(1);
    }

    /**
     * Example function to demonstrate error handling.
     *
     * @param string $data Example data that could trigger an error.
     */
    public function processData($data) {
        try {
            if (empty($data)) {
                throw new InvalidArgumentException('Input data cannot be empty.');
            }

            // Process data here
            // ...

        } catch (InvalidArgumentException $e) {
            // Handle specific exception
            $this->handleExceptions($e);
        } catch (Exception $e) {
            // Handle any other exceptions
            $this->handleExceptions($e);
        }
    }
}

// Initialize the error handler
new Astra_Sites_Error_Handler();
```
