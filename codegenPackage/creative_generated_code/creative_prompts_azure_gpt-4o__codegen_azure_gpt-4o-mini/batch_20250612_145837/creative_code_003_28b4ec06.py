"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisawpv3.com
Prompt: Recommend a PHP library compatible with PHP 8.3.14 for managing server logs in a structure similar to the `logs/` directory on Apache 2.4.62.
Generated: DETERMINISTIC_28b4ec066cfee169
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

/**
 * LogManager class for handling server logs.
 * 
 * This class provides methods to write, read, and manage logs
 * in a structured format similar to the Apache logs directory.
 *
 * PHP Version 8.3.14
 */
class LogManager
{
    private string $logDirectory;

    /**
     * Constructor to set the log directory.
     * 
     * @param string $logDirectory Directory to store log files.
     * @throws InvalidArgumentException if the log directory is not writable.
     */
    public function __construct(string $logDirectory)
    {
        if (!is_dir($logDirectory) || !is_writable($logDirectory)) {
            throw new InvalidArgumentException("Log directory is not writable: $logDirectory");
        }
        $this->logDirectory = rtrim($logDirectory, '/') . '/';
    }

    /**
     * Write a log message to a specific log file.
     * 
     * @param string $message The log message to write.
     * @param string $logFile The name of the log file.
     * @throws RuntimeException if unable to write to the log file.
     */
    public function writeLog(string $message, string $logFile): void
    {
        $logFilePath = $this->logDirectory . $logFile;
        $formattedMessage = sprintf("%s - %s\n", date('Y-m-d H:i:s'), $message);

        if (file_put_contents($logFilePath, $formattedMessage, FILE_APPEND) === false) {
            throw new RuntimeException("Unable to write to log file: $logFilePath");
        }
    }

    /**
     * Read the contents of a log file.
     * 
     * @param string $logFile The name of the log file to read.
     * @return string Contents of the log file.
     * @throws RuntimeException if the log file cannot be read.
     */
    public function readLog(string $logFile): string
    {
        $logFilePath = $this->logDirectory . $logFile;

        if (!is_readable($logFilePath)) {
            throw new RuntimeException("Log file is not readable: $logFilePath");
        }

        return file_get_contents($logFilePath);
    }

    /**
     * List all log files in the log directory.
     * 
     * @return array Array of log file names.
     */
    public function listLogFiles(): array
    {
        return array_filter(scandir($this->logDirectory), function($file) {
            return is_file($this->logDirectory . $file) && pathinfo($file, PATHINFO_EXTENSION) === 'log';
        });
    }
}

// Example usage:
try {
    $logManager = new LogManager('/path/to/logs'); // Set the path to your logs directory
    $logManager->writeLog('This is a test log message.', 'access.log');
    $logs = $logManager->readLog('access.log');
    echo $logs;

    $logFiles = $logManager->listLogFiles();
    print_r($logFiles);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
