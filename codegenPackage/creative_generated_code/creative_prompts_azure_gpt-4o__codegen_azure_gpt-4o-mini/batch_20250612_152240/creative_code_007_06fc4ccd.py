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
 * Error Logging and Display Script
 * This script logs detailed error messages for server issues
 * and displays them when configured to do so.
 */

// Set the reporting level to display all errors, but you may want to change this in production
error_reporting(E_ALL);

// Path to the log file
define('LOG_FILE', __DIR__ . '/error_log.txt');

// Function to log error messages to a file
function logError($message) {
    // Create a timestamp for the log entry
    $timestamp = date('Y-m-d H:i:s');
    
    // Format the error message
    $logMessage = "[{$timestamp}] ERROR: {$message}\n";
    
    // Attempt to write the log message to the log file
    if (file_put_contents(LOG_FILE, $logMessage, FILE_APPEND | LOCK_EX) === false) {
        // Log file writing failed, handle the error
        error_log("Failed to write to log file: " . LOG_FILE);
    }
}

// Custom error handler function
function customErrorHandler($errno, $errstr, $errfile, $errline) {
    // Log the error
    logError("Error number: {$errno}, Error string: {$errstr}, File: {$errfile}, Line: {$errline}");

    // Display a user-friendly message if not in production mode
    if (defined('SHOW_ERRORS') && SHOW_ERRORS) {
        echo "<b>Error:</b> [$errno] $errstr in $errfile on line $errline<br>";
    }
}

// Set the custom error handler
set_error_handler("customErrorHandler");

// Example usage: Trigger an error for testing purposes
// Uncomment the line below to simulate an error
// trigger_error("This is a test error!", E_USER_ERROR);

// Sample function to demonstrate error logging
function divide($numerator, $denominator) {
    if ($denominator == 0) {
        // Log and handle division by zero error
        logError("Division by zero error: numerator = {$numerator}, denominator = {$denominator}");
        return false; // Return false to indicate an error
    }
    return $numerator / $denominator;
}

// Example test: Uncomment the following lines to test the divide function
// $result = divide(10, 0);
// if ($result === false) {
//     echo "An error occurred during division. Check the log for details.";
// }

?>
```
