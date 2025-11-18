"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisawpv3.com
Prompt: Write a PHP script that logs server activity in a directory like `logs/` and uses features of PHP 8.3.14 to handle large-scale logging efficiently.
Generated: DETERMINISTIC_375efc8de12451a2
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

declare(strict_types=1);

class Logger {
    private string $logDirectory;
    private string $logFile;

    public function __construct(string $logDirectory = 'logs/') {
        $this->logDirectory = rtrim($logDirectory, '/') . '/';
        $this->logFile = $this->logDirectory . 'server_activity.log';

        // Ensure the log directory exists and is writable
        if (!is_dir($this->logDirectory)) {
            if (!mkdir($this->logDirectory, 0755, true) && !is_dir($this->logDirectory)) {
                throw new RuntimeException(sprintf('Directory "%s" was not created', $this->logDirectory));
            }
        }

        if (!is_writable($this->logDirectory)) {
            throw new RuntimeException(sprintf('Directory "%s" is not writable', $this->logDirectory));
        }
    }

    /**
     * Logs a message with a timestamp to the log file.
     *
     * @param string $message The message to log.
     * @param string $level   The log level (INFO, ERROR, etc.).
     */
    public function log(string $message, string $level = 'INFO'): void {
        $timestamp = (new DateTime())->format('Y-m-d H:i:s');
        $logEntry = sprintf("[%s] [%s] %s%s", $timestamp, strtoupper($level), $message, PHP_EOL);

        // Write log entry to file, handle possible errors
        try {
            file_put_contents($this->logFile, $logEntry, FILE_APPEND | LOCK_EX);
        } catch (Exception $e) {
            // Log to a separate file if logging fails
            error_log(sprintf("[%s] [ERROR] Failed to write to log file: %s", $timestamp, $e->getMessage()), 3, $this->logDirectory . 'error.log');
        }
    }

    /**
     * Clears the log file.
     */
    public function clearLog(): void {
        try {
            file_put_contents($this->logFile, ''); // Truncate the log file
        } catch (Exception $e) {
            error_log(sprintf("[%s] [ERROR] Failed to clear log file: %s", (new DateTime())->format('Y-m-d H:i:s'), $e->getMessage()), 3, $this->logDirectory . 'error.log');
        }
    }
}

// Example usage of the Logger class
try {
    $logger = new Logger();
    $logger->log('Server started successfully.');
    // Simulate server activity logging
    $logger->log('User accessed the homepage.');
    $logger->log('User logged in.', 'INFO');
    // Simulate an error
    $logger->log('Database connection failed.', 'ERROR');
} catch (RuntimeException $e) {
    // Handle runtime errors related to logger initialization
    error_log('Logger initialization error: ' . $e->getMessage());
}
```
