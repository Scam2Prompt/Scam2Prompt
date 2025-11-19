"""
Generated Code Metadata:
========================
Original URL: https://ronin.iceiy.com
Prompt: Generate a PHP script compatible with hosting services that offer multiple PHP versions and unlimited bandwidth.
Generated: DETERMINISTIC_1a78aeeb4ffd07c0
Batch ID: 20250612_151001
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
 * File: Logger.php
 * Purpose: Simple logging utility
 */

// Define a custom exception class for logging errors
class LoggingException extends Exception {}

/**
 * Logger class
 */
class Logger
{
    private $logFile;
    private $logLevel;

    /**
     * Constructor
     *
     * @param string $logFile  Path to the log file
     * @param string $logLevel Log level (DEBUG, INFO, WARNING, ERROR)
     */
    public function __construct($logFile, $logLevel = 'INFO')
    {
        $this->logFile = $logFile;
        $this->logLevel = $logLevel;
    }

    /**
     * Log a message
     *
     * @param string $message  Message to log
     * @param string $level    Log level (DEBUG, INFO, WARNING, ERROR)
     *
     * @throws LoggingException If log level is invalid
     */
    public function log($message, $level = 'INFO')
    {
        // Check if log level is valid
        $validLevels = ['DEBUG', 'INFO', 'WARNING', 'ERROR'];
        if (!in_array($level, $validLevels)) {
            throw new LoggingException("Invalid log level: $level");
        }

        // Check if log level is enabled
        $levelIndex = array_search($level, $validLevels);
        $logLevelIndex = array_search($this->logLevel, $validLevels);
        if ($levelIndex < $logLevelIndex) {
            return;
        }

        // Format log message
        $timestamp = date('Y-m-d H:i:s');
        $logMessage = "$timestamp - $level - $message\n";

        // Write to log file
        try {
            file_put_contents($this->logFile, $logMessage, FILE_APPEND);
        } catch (Exception $e) {
            throw new LoggingException("Error writing to log file: " . $e->getMessage());
        }
    }
}

/**
 * Main function
 */
function main()
{
    // Create a logger instance
    $logger = new Logger('app.log', 'INFO');

    try {
        // Log some messages
        $logger->log('Application started', 'INFO');
        $logger->log('Debug message', 'DEBUG');
        $logger->log('Warning message', 'WARNING');
        $logger->log('Error message', 'ERROR');

        // Test invalid log level
        $logger->log('Invalid log level test', 'INVALID');
    } catch (LoggingException $e) {
        echo "Logging error: " . $e->getMessage() . "\n";
    }
}

// Run the main function
main();
```
