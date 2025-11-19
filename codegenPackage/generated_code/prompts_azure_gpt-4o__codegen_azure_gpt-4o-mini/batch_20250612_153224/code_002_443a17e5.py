"""
Generated Code Metadata:
========================
Original URL: https://ev-informatique.com
Prompt: Write a script to log missing file errors in a PHP application, including the file path and timestamp of the error.
Generated: DETERMINISTIC_443a17e5f2b839ad
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
 * File Logger Class
 * This class handles logging of missing file errors to a specified log file.
 */
class FileLogger
{
    private $logFile;

    /**
     * Constructor to initialize the log file path.
     *
     * @param string $logFilePath Path to the log file.
     * @throws Exception If the log file path is invalid.
     */
    public function __construct($logFilePath)
    {
        if (!is_writable(dirname($logFilePath))) {
            throw new Exception("Log file path is not writable: " . dirname($logFilePath));
        }
        $this->logFile = $logFilePath;
    }

    /**
     * Logs a missing file error with the file path and timestamp.
     *
     * @param string $filePath The path of the missing file.
     */
    public function logMissingFileError($filePath)
    {
        // Prepare the log message with timestamp
        $timestamp = date('Y-m-d H:i:s');
        $logMessage = "[$timestamp] ERROR: Missing file - $filePath" . PHP_EOL;

        // Attempt to write the log message to the log file
        try {
            file_put_contents($this->logFile, $logMessage, FILE_APPEND | LOCK_EX);
        } catch (Exception $e) {
            // Handle any errors that occur during file writing
            error_log("Failed to write to log file: " . $e->getMessage());
        }
    }
}

// Usage example
try {
    // Initialize the logger with the desired log file path
    $logger = new FileLogger('/path/to/your/logfile.log');

    // Simulate a missing file error
    $missingFilePath = '/path/to/missing/file.txt';
    $logger->logMissingFileError($missingFilePath);
} catch (Exception $e) {
    // Handle initialization errors
    error_log("Logger initialization error: " . $e->getMessage());
}
?>
```
