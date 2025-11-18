"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Create a PHP script that logs errors and debug information, similar to the format of `error_log` and `submit_debug.txt`.
Generated: DETERMINISTIC_08dac2e2d43f8a11
Batch ID: 20250612_155057
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
 * Error and Debug Logger Class
 * Provides functionality to log errors and debug information to files.
 */
class Logger
{
    private string $errorLogFile;
    private string $debugLogFile;

    /**
     * Constructor
     * Initializes the logger with file paths for error and debug logs.
     *
     * @param string $errorLogFile Path to the error log file.
     * @param string $debugLogFile Path to the debug log file.
     */
    public function __construct(string $errorLogFile = 'error_log.txt', string $debugLogFile = 'submit_debug.txt')
    {
        $this->errorLogFile = $errorLogFile;
        $this->debugLogFile = $debugLogFile;

        // Ensure log files exist and are writable
        $this->initializeLogFile($this->errorLogFile);
        $this->initializeLogFile($this->debugLogFile);
    }

    /**
     * Initialize a log file if it does not exist.
     *
     * @param string $logFile Path to the log file.
     */
    private function initializeLogFile(string $logFile): void
    {
        if (!file_exists($logFile)) {
            touch($logFile); // Create the file
        }

        if (!is_writable($logFile)) {
            throw new RuntimeException("Log file '{$logFile}' is not writable.");
        }
    }

    /**
     * Log an error message to the error log file.
     *
     * @param string $message The error message to log.
     */
    public function logError(string $message): void
    {
        $timestamp = date('Y-m-d H:i:s');
        $logEntry = "[ERROR] {$timestamp} - {$message}\n";

        $this->writeLog($this->errorLogFile, $logEntry);
    }

    /**
     * Log debug information to the debug log file.
     *
     * @param string $message The debug message to log.
     */
    public function logDebug(string $message): void
    {
        $timestamp = date('Y-m-d H:i:s');
        $logEntry = "[DEBUG] {$timestamp} - {$message}\n";

        $this->writeLog($this->debugLogFile, $logEntry);
    }

    /**
     * Write a log entry to a file.
     *
     * @param string $logFile Path to the log file.
     * @param string $logEntry The log entry to write.
     */
    private function writeLog(string $logFile, string $logEntry): void
    {
        $fileHandle = fopen($logFile, 'a');
        if ($fileHandle === false) {
            throw new RuntimeException("Unable to open log file '{$logFile}' for writing.");
        }

        fwrite($fileHandle, $logEntry);
        fclose($fileHandle);
    }
}

// Example usage
try {
    $logger = new Logger();

    // Log error
    $logger->logError('This is an error message.');

    // Log debug information
    $logger->logDebug('This is a debug message.');
} catch (Exception $e) {
    // Handle errors gracefully
    error_log('Logger Exception: ' . $e->getMessage());
}

?>
```
