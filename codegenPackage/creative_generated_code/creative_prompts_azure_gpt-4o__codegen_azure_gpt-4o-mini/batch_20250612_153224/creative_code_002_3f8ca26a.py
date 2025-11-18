"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storebari.com
Prompt: Generate a PHP script to log detailed stack traces for errors occurring in the Astra Sites plugin, specifically in `class-astra-sites-error-handler.php`.
Generated: DETERMINISTIC_3f8ca26a7efc332f
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
 * This script logs detailed stack traces for errors occurring in the Astra Sites plugin.
 * It is designed to capture exceptions and errors, providing insights for debugging.
 */

class Astra_Sites_Error_Handler {
    // Path to the log file
    private $log_file;

    /**
     * Constructor to initialize the error handler.
     *
     * @param string $log_file Path to the log file where errors will be recorded.
     */
    public function __construct($log_file) {
        $this->log_file = $log_file;
        // Set the custom error handler
        set_error_handler([$this, 'handleError']);
        // Set the custom exception handler
        set_exception_handler([$this, 'handleException']);
    }

    /**
     * Custom error handler to log errors.
     *
     * @param int $errno Error level.
     * @param string $errstr Error message.
     * @param string $errfile Filename where the error occurred.
     * @param int $errline Line number where the error occurred.
     * @return void
     */
    public function handleError($errno, $errstr, $errfile, $errline) {
        // Format error message
        $error_message = sprintf(
            "[%s] ERROR: [%d] %s in %s on line %d\n",
            date('Y-m-d H:i:s'),
            $errno,
            $errstr,
            $errfile,
            $errline
        );
        $this->logError($error_message);
        return true; // Prevent the PHP error handler from being called
    }

    /**
     * Custom exception handler to log exceptions.
     *
     * @param Exception $exception The uncaught exception.
     * @return void
     */
    public function handleException($exception) {
        // Format exception message with stack trace
        $exception_message = sprintf(
            "[%s] UNCAUGHT EXCEPTION: %s in %s on line %d\nStack trace:\n%s\n",
            date('Y-m-d H:i:s'),
            $exception->getMessage(),
            $exception->getFile(),
            $exception->getLine(),
            $exception->getTraceAsString()
        );
        $this->logError($exception_message);
    }

    /**
     * Logs error messages to the specified log file.
     *
     * @param string $message The message to log.
     * @return void
     */
    private function logError($message) {
        // Ensure the log directory is writable
        if (!is_writable(dirname($this->log_file))) {
            error_log('Log directory is not writable: ' . dirname($this->log_file));
            return;
        }

        // Append the error message to the log file
        file_put_contents($this->log_file, $message, FILE_APPEND | LOCK_EX);
    }
}

// Usage: Create an instance of the error handler with the log file path
$new_error_handler = new Astra_Sites_Error_Handler(__DIR__ . '/astra_sites_error.log');
```
