"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Create a PHP script that logs errors and debug information, similar to the format of `error_log` and `submit_debug.txt`.
Generated: DETERMINISTIC_08dac2e2d43f8a11
Batch ID: 20250612_155057
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
 * Error Logger Class
 *
 * This class provides a simple way to log errors and debug information to a file.
 */
class ErrorLogger
{
    /**
     * Log file path
     *
     * @var string
     */
    private $logFile;

    /**
     * Debug file path
     *
     * @var string
     */
    private $debugFile;

    /**
     * Constructor
     *
     * @param string $logFile  Path to the log file
     * @param string $debugFile Path to the debug file
     */
    public function __construct($logFile = 'error_log.txt', $debugFile = 'submit_debug.txt')
    {
        $this->logFile  = $logFile;
        $this->debugFile = $debugFile;
    }

    /**
     * Log an error
     *
     * @param string $message Error message
     * @param int    $level   Error level (E_NOTICE, E_WARNING, E_ERROR)
     */
    public function logError($message, $level = E_ERROR)
    {
        $this->log($this->logFile, $message, $level);
    }

    /**
     * Log debug information
     *
     * @param string $message Debug message
     */
    public function logDebug($message)
    {
        $this->log($this->debugFile, $message);
    }

    /**
     * Log a message to a file
     *
     * @param string $file    Log file path
     * @param string $message Message to log
     * @param int    $level   Error level (optional)
     */
    private function log($file, $message, $level = null)
    {
        try {
            // Get current timestamp
            $timestamp = date('Y-m-d H:i:s');

            // Format log message
            if ($level !== null) {
                $logMessage = "$timestamp - Level: $level - $message\n";
            } else {
                $logMessage = "$timestamp - $message\n";
            }

            // Write to log file
            file_put_contents($file, $logMessage, FILE_APPEND);
        } catch (Exception $e) {
            // Handle exception
            echo "Error logging message: " . $e->getMessage() . "\n";
        }
    }
}

// Example usage
$logger = new ErrorLogger();

// Log an error
$logger->logError('This is an error message', E_ERROR);

// Log debug information
$logger->logDebug('This is a debug message');

// Test error handling
try {
    throw new Exception('Test exception');
} catch (Exception $e) {
    $logger->logError($e->getMessage(), E_ERROR);
}
```
