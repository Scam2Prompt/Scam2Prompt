"""
Generated Code Metadata:
========================
Original URL: https://storebari.com
Prompt: Generate a PHP script to log detailed stack traces for errors occurring in the Astra Sites plugin, specifically in `class-astra-sites-error-handler.php`.
Generated: DETERMINISTIC_3f8ca26a7efc332f
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
 * Astra Sites Error Handler
 * 
 * This script logs detailed stack traces for errors occurring in the Astra Sites plugin.
 * 
 * @package Astra Sites
 * @since 1.0.0
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class Astra_Sites_Error_Handler {

    /**
     * Initialize the error handler
     */
    public static function init() {
        register_shutdown_function(array(__CLASS__, 'handle_shutdown'));
        set_error_handler(array(__CLASS__, 'handle_error'));
        set_exception_handler(array(__CLASS__, 'handle_exception'));
    }

    /**
     * Handle PHP errors
     *
     * @param int    $errno   The error level
     * @param string $errstr  The error message
     * @param string $errfile The file where the error occurred
     * @param int    $errline The line number where the error occurred
     * @return bool
     */
    public static function handle_error($errno, $errstr, $errfile, $errline) {
        if (!(error_reporting() & $errno)) {
            return false;
        }

        $error_types = array(
            E_ERROR             => 'Error',
            E_WARNING           => 'Warning',
            E_PARSE             => 'Parse Error',
            E_NOTICE            => 'Notice',
            E_CORE_ERROR        => 'Core Error',
            E_CORE_WARNING      => 'Core Warning',
            E_COMPILE_ERROR     => 'Compile Error',
            E_COMPILE_WARNING   => 'Compile Warning',
            E_USER_ERROR        => 'User Error',
            E_USER_WARNING      => 'User Warning',
            E_USER_NOTICE       => 'User Notice',
            E_STRICT            => 'Strict Notice',
            E_RECOVERABLE_ERROR => 'Recoverable Error',
            E_DEPRECATED        => 'Deprecated',
            E_USER_DEPRECATED   => 'User Deprecated',
        );

        $error_type = isset($error_types[$errno]) ? $error_types[$errno] : 'Unknown Error';

        $backtrace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS);
        $log_message = self::format_error_message($error_type, $errstr, $errfile, $errline, $backtrace);

        self::log_error($log_message);

        // Don't execute PHP internal error handler
        return true;
    }

    /**
     * Handle uncaught exceptions
     *
     * @param Throwable $exception The uncaught exception
     */
    public static function handle_exception($exception) {
        $error_type = get_class($exception);
        $errstr = $exception->getMessage();
        $errfile = $exception->getFile();
        $errline = $exception->getLine();
        $backtrace = $exception->getTrace();

        $log_message = self::format_error_message($error_type, $errstr, $errfile, $errline, $backtrace);

        self::log_error($log_message);
    }

    /**
     * Handle fatal errors
     */
    public static function handle_shutdown() {
        $last_error = error_get_last();
        if ($last_error && in_array($last_error['type'], array(E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR, E_USER_ERROR))) {
            $error_type = 'Fatal Error';
            $errstr = $last_error['message'];
            $errfile = $last_error['file'];
            $errline = $last_error['line'];
            $backtrace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS);

            $log_message = self::format_error_message($error_type, $errstr, $errfile, $errline, $backtrace);

            self::log_error($log_message);
        }
    }

    /**
     * Format error message with stack trace
     *
     * @param string $error_type Type of error
     * @param string $error_message Error message
     * @param string $file File where error occurred
     * @param int $line Line number where error occurred
     * @param array $backtrace Stack trace
     * @return string Formatted error message
     */
    private static function format_error_message($error_type, $error_message, $file, $line, $backtrace) {
        $message = "[" . current_time('mysql') . "] ";
        $message .= "Astra Sites Error: {$error_type}\n";
        $message .= "Message: {$error_message}\n";
        $message .= "File: {$file} (Line: {$line})\n";
        $message .= "Stack Trace:\n";

        foreach ($backtrace as $index => $trace) {
            $file = isset($trace['file']) ? $trace['file'] : 'unknown';
            $line = isset($trace['line']) ? $trace['line'] : 'unknown';
            $function = isset($trace['function']) ? $trace['function'] : 'unknown';
            $class = isset($trace['class']) ? $trace['class'] : '';
            $type = isset($trace['type']) ? $trace['type'] : '';

            $message .= sprintf(
                "#%d %s%s%s() called at [%s:%d]\n",
                $index,
                $class,
                $type,
                $function,
                $file,
                $line
            );
        }

        return $message;
    }

    /**
     * Log error to file
     *
     * @param string $message Error message to log
     */
    private static function log_error($message) {
        $log_dir = WP_CONTENT_DIR . '/astrasites-logs';
        $log_file = $log_dir . '/error.log';

        // Create log directory if it doesn't exist
        if (!file_exists($log_dir)) {
            wp_mkdir_p($log_dir);
        }

        // Add a separator between error entries
        $message .= "\n" . str_repeat('-', 80) . "\n\n";

        // Write to log file
        error_log($message, 3, $log_file);
    }
}

// Initialize the error handler
Astra_Sites_Error_Handler::init();
```
