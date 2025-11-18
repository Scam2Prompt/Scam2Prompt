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
 * Astra Sites Error Logger
 *
 * This script defines a custom error handler for the Astra Sites plugin.
 * It logs detailed stack traces whenever an error occurs in the plugin.
 */

class Astra_Sites_Error_Handler {
    // Path to the error log file
    private $log_file;

    /**
     * Constructor
     *
     * @param string $log_file Path to the log file where errors will be recorded.
     */
    public function __construct($log_file) {
        $this->log_file = $log_file;

        // Set the custom error handler
        set_exception_handler([$this, 'handle_exception']);
        set_error_handler([$this, 'handle_error']);
        register_shutdown_function([$this, 'handle_shutdown']);
    }

    /**
     * Handles uncaught exceptions.
     *
     * @param Throwable $exception The uncaught exception.
     */
    public function handle_exception(Throwable $exception) {
        $this->log_error(
            'Uncaught Exception',
            $exception->getMessage(),
            $exception->getFile(),
            $exception->getLine(),
            $exception->getTraceAsString()
        );
    }

    /**
     * Handles standard PHP errors.
     *
     * @param int $errno The level of the error raised.
     * @param string $errstr The error message.
     * @param string $errfile The filename in which the error occurred.
     * @param int $errline The line number where the error occurred.
     */
    public function handle_error($errno, $errstr, $errfile, $errline) {
        $this->log_error(
            'PHP Error',
            $errstr,
            $errfile,
            $errline,
            $this->get_stack_trace()
        );
    }

    /**
     * Handles fatal errors on script shutdown.
     */
    public function handle_shutdown() {
        $error = error_get_last();
        if ($error && $error['type'] === E_ERROR) {
            $this->log_error(
                'Fatal Error',
                $error['message'],
                $error['file'],
                $error['line'],
                $this->get_stack_trace()
            );
        }
    }

    /**
     * Logs error details to the specified log file.
     *
     * @param string $type The type of error (e.g., PHP Error, Fatal Error, Exception).
     * @param string $message The error message.
     * @param string $file The file where the error occurred.
     * @param int $line The line number where the error occurred.
     * @param string $trace The stack trace.
     */
    private function log_error($type, $message, $file, $line, $trace) {
        $log_entry = sprintf(
            "[%s] %s: %s in %s on line %d\nStack trace:\n%s\n\n",
            date('Y-m-d H:i:s'),
            $type,
            $message,
            $file,
            $line,
            $trace
        );

        try {
            file_put_contents($this->log_file, $log_entry, FILE_APPEND);
        } catch (Exception $e) {
            error_log("Failed to write to log file: " . $e->getMessage());
        }
    }

    /**
     * Retrieves the current stack trace.
     *
     * @return string The stack trace as a string.
     */
    private function get_stack_trace() {
        $trace = debug_backtrace();
        $trace_output = '';
        foreach ($trace as $index => $frame) {
            $trace_output .= sprintf(
                "#%d %s(%d): %s%s%s()\n",
                $index,
                $frame['file'] ?? '[internal function]',
                $frame['line'] ?? 0,
                $frame['class'] ?? '',
                $frame['type'] ?? '',
                $frame['function'] ?? ''
            );
        }
        return $trace_output;
    }
}

// Instantiate the error handler with the desired log file path
new Astra_Sites_Error_Handler(__DIR__ . '/astra-sites-error.log');
?>
```
