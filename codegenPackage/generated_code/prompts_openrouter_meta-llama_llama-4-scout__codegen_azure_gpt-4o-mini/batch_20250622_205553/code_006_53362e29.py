"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: "Write a PHP function that uses ThinkPHP's logging features to record errors and exceptions, and provide an example of how to configure the logging settings."
Generated: DETERMINISTIC_53362e297286b17a
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Import the necessary ThinkPHP classes
use think\Log;
use think\Exception;

// Function to log errors and exceptions
function logError($message, $context = [])
{
    try {
        // Check if the message is not empty
        if (empty($message)) {
            throw new Exception("Log message cannot be empty.");
        }

        // Log the error message with context
        Log::error($message, $context);
    } catch (Exception $e) {
        // Handle any exceptions that occur during logging
        Log::error("Logging error: " . $e->getMessage());
    }
}

// Example of configuring logging settings in ThinkPHP
function configureLogging()
{
    // Set the logging configuration
    config('log', [
        'type' => 'File', // Log type (File, Socket, etc.)
        'path' => '../runtime/log/', // Log file path
        'level' => ['error', 'warning', 'info'], // Log levels to record
        'single' => false, // Whether to use a single log file
        'max_files' => 30, // Maximum number of log files to keep
    ]);
}

// Example usage of the logError function
try {
    // Simulate an error
    throw new Exception("An example error occurred.");
} catch (Exception $e) {
    // Log the exception message
    logError($e->getMessage(), ['code' => $e->getCode()]);
}

// Call the configureLogging function to set up logging
configureLogging();
?>
```
