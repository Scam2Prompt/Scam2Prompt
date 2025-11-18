"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: Write a PHP script to log and display detailed error messages for server issues, such as those described on FASTPANEL's troubleshooting page.
Generated: DETERMINISTIC_06fc4ccdc2b22825
Batch ID: 20250612_152240
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
 * This script logs and displays detailed error messages for server issues.
 * It is designed to follow best practices for error handling and logging in PHP.
 * Ensure that appropriate permissions are set for the log file.
 */

// Configuration settings
define('ERROR_LOG_FILE', __DIR__ . '/server_error_log.txt');
define('DISPLAY_ERRORS', true); // Set to false in production for security reasons
define('LOG_ERRORS', true); // Enable or disable error logging

/**
 * Initialize error handling settings.
 */
function initializeErrorHandling() {
    // Set error reporting to capture all types of errors
    error_reporting(E_ALL);

    // Set custom error handler
    set_error_handler('customErrorHandler');

    // Set custom exception handler
    set_exception_handler('customExceptionHandler');

    // Register shutdown function to catch fatal errors
    register_shutdown_function('shutdownHandler');
}

/**
 * Custom error handler for non-fatal errors.
 * @param int $errno The error number
 * @param string $errstr The error message
 * @param string $errfile The file in which the error occurred
 * @param int $errline The line number where the error occurred
 */
function customErrorHandler($errno, $errstr, $errfile, $errline) {
    $errorMessage = "[ERROR] [Type: $errno] $errstr in $errfile on line $errline";

    // Log the error to a file
    if (LOG_ERRORS) {
        logError($errorMessage);
    }

    // Display the error if DISPLAY_ERRORS is true
    if (DISPLAY_ERRORS) {
        echo "<pre>$errorMessage</pre>";
    }
}

/**
 * Custom exception handler for uncaught exceptions.
 * @param Throwable $exception The uncaught exception
 */
function customExceptionHandler($exception) {
    $errorMessage = "[EXCEPTION] " . $exception->getMessage() . " in " .
        $exception->getFile() . " on line " . $exception->getLine();

    // Log the exception to a file
    if (LOG_ERRORS) {
        logError($errorMessage);
    }

    // Display the exception if DISPLAY_ERRORS is true
    if (DISPLAY_ERRORS) {
        echo "<pre>$errorMessage</pre>";
    }
}

/**
 * Shutdown function to catch fatal errors.
 */
function shutdownHandler() {
    $lastError = error_get_last();
    if ($lastError && ($lastError['type'] === E_ERROR || $lastError['type'] === E_PARSE || $lastError['type'] === E_COMPILE_ERROR || $lastError['type'] === E_CORE_ERROR)) {
        $errorMessage = "[FATAL] " . $lastError['message'] . " in " .
            $lastError['file'] . " on line " . $lastError['line'];

        // Log the fatal error to a file
        if (LOG_ERRORS) {
            logError($errorMessage);
        }

        // Display the fatal error if DISPLAY_ERRORS is true
        if (DISPLAY_ERRORS) {
            echo "<pre>$errorMessage</pre>";
        }
    }
}

/**
 * Logs error messages to a file.
 * @param string $message The error message to log
 */
function logError($message) {
    $timestamp = date('Y-m-d H:i:s');
    $logMessage = "[$timestamp] $message" . PHP_EOL;

    // Append log message to the error log file
    file_put_contents(ERROR_LOG_FILE, $logMessage, FILE_APPEND | LOCK_EX);
}

/**
 * Example function to trigger errors and exceptions for testing.
 */
function testErrorHandling() {
    // Trigger a warning
    trigger_error("This is a test warning", E_USER_WARNING);

    // Trigger an exception
    throw new Exception("This is a test exception");

    // Trigger a fatal error
    nonexistentFunction(); // This function does not exist
}

// Initialize error handling
initializeErrorHandling();

// Uncomment the line below to test error handling (for debugging purposes)
// testErrorHandling();
?>
```
