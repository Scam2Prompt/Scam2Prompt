"""
Generated Code Metadata:
========================
Original URL: https://okxaltdrive.com
Prompt: Write a PHP script to log and display detailed error messages for server issues, such as those described on FASTPANEL's troubleshooting page.
Generated: DETERMINISTIC_06fc4ccdc2b22825
Batch ID: 20250612_152240
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
 * Error Logger and Display Script
 * 
 * This script logs detailed error messages to a file and displays them in a user-friendly format.
 * It handles various server issues and provides troubleshooting information.
 */

// Define constants
define('LOG_FILE', 'server_errors.log');
define('DISPLAY_ERRORS', true);
define('LOG_ERRORS', true);
define('ERROR_TYPES', E_ALL);

// Set error reporting level
error_reporting(ERROR_TYPES);

// Custom error handler function
function customErrorHandler($errno, $errstr, $errfile, $errline, $errcontext = null) {
    // Check if error should be logged or displayed
    $log_error = LOG_ERRORS && ($errno & ERROR_TYPES);
    $display_error = DISPLAY_ERRORS && ($errno & ERROR_TYPES);
    
    // Format error message
    $error_type = '';
    switch ($errno) {
        case E_ERROR:
            $error_type = 'Fatal Error';
            break;
        case E_WARNING:
            $error_type = 'Warning';
            break;
        case E_PARSE:
            $error_type = 'Parse Error';
            break;
        case E_NOTICE:
            $error_type = 'Notice';
            break;
        case E_CORE_ERROR:
            $error_type = 'Core Error';
            break;
        case E_CORE_WARNING:
            $error_type = 'Core Warning';
            break;
        case E_COMPILE_ERROR:
            $error_type = 'Compile Error';
            break;
        case E_COMPILE_WARNING:
            $error_type = 'Compile Warning';
            break;
        case E_USER_ERROR:
            $error_type = 'User Error';
            break;
        case E_USER_WARNING:
            $error_type = 'User Warning';
            break;
        case E_USER_NOTICE:
            $error_type = 'User Notice';
            break;
        case E_STRICT:
            $error_type = 'Strict Standards';
            break;
        case E_RECOVERABLE_ERROR:
            $error_type = 'Recoverable Error';
            break;
        case E_DEPRECATED:
            $error_type = 'Deprecated';
            break;
        case E_USER_DEPRECATED:
            $error_type = 'User Deprecated';
            break;
        default:
            $error_type = 'Unknown Error';
    }
    
    $error_message = sprintf(
        "[%s] %s: %s in %s on line %d",
        date('Y-m-d H:i:s'),
        $error_type,
        $errstr,
        $errfile,
        $errline
    );
    
    // Log error to file
    if ($log_error) {
        error_log($error_message . PHP_EOL, 3, LOG_FILE);
    }
    
    // Display error to user
    if ($display_error) {
        echo '<div class="error-message">';
        echo '<h3>Server Error Encountered</h3>';
        echo '<p><strong>Type:</strong> ' . htmlspecialchars($error_type) . '</p>';
        echo '<p><strong>Message:</strong> ' . htmlspecialchars($errstr) . '</p>';
        echo '<p><strong>File:</strong> ' . htmlspecialchars($errfile) . '</p>';
        echo '<p><strong>Line:</strong> ' . htmlspecialchars($errline) . '</p>';
        
        // Additional troubleshooting information
        echo '<div class="troubleshooting">';
        echo '<h4>Troubleshooting Suggestions:</h4>';
        echo '<ul>';
        echo '<li>Check file permissions</li>';
        echo '<li>Verify database connection settings</li>';
        echo '<li>Review recent code changes</li>';
        echo '<li>Check server resource usage</li>';
        echo '</ul>';
        echo '</div>';
        echo '</div>';
    }
    
    // Don't execute PHP internal error handler
    return true;
}

// Custom exception handler
function customExceptionHandler($exception) {
    customErrorHandler(
        E_ERROR,
        'Uncaught Exception: ' . $exception->getMessage(),
        $exception->getFile(),
        $exception->getLine()
    );
}

// Set error and exception handlers
set_error_handler('customErrorHandler');
set_exception_handler('customExceptionHandler');

// Register shutdown function for fatal errors
register_shutdown_function(function() {
    $error = error_get_last();
    if ($error && ($error['type'] & (E_ERROR | E_PARSE | E_CORE_ERROR | E_COMPILE_ERROR))) {
        customErrorHandler(
            $error['type'],
            $error['message'],
            $error['file'],
            $error['line']
        );
    }
});

// CSS for error display
echo '<style>
.error-message {
    border: 1px solid #ff0000;
    background-color: #ffeeee;
    padding: 15px;
    margin: 20px;
    font-family: Arial, sans-serif;
    color: #333;
}
.error-message h3 {
    color: #ff0000;
    margin-top: 0;
}
.troubleshooting {
    margin-top: 15px;
    padding: 10px;
    background-color: #fff;
    border: 1px solid #ddd;
}
.troubleshooting h4 {
    margin-top: 0;
}
</style>';
```
