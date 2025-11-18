"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmaarokatcap.com
Prompt: Write a PHP script to log server activity into a directory structure similar to `logs/` and `tmp/`, ensuring secure file handling.
Generated: DETERMINISTIC_1cd0da8a238cd1b5
Batch ID: 20250612_145923
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
 * PHP Script to log server activity securely into a directory structure.
 * Directory structure: `logs/` and `tmp/`
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

/**
 * Logs server activity securely to a file.
 *
 * @param string $message The log message to write.
 * @param string $type The type of log (e.g., 'error', 'info', 'debug').
 * @return void
 */
function logServerActivity($message, $type = 'info') {
    // Define the directory paths
    $logDir = __DIR__ . '/logs/';
    $tmpDir = __DIR__ . '/tmp/';
    
    // Ensure directories exist and are writable
    if (!is_dir($logDir)) {
        mkdir($logDir, 0755, true);
    }
    if (!is_dir($tmpDir)) {
        mkdir($tmpDir, 0755, true);
    }

    // Sanitize log type for safe file naming
    $safeType = preg_replace('/[^a-zA-Z0-9_\-]/', '', $type);

    // Construct the log file path
    $logFilePath = $logDir . $safeType . '_log.txt';

    // Prepare the log message
    $timestamp = date('Y-m-d H:i:s');
    $logMessage = "[{$timestamp}] {$message}\n";

    // Secure file handling and error checking
    try {
        $logFileHandle = fopen($logFilePath, 'a'); // Open file in append mode
        if ($logFileHandle === false) {
            throw new Exception("Failed to open log file: {$logFilePath}");
        }

        if (fwrite($logFileHandle, $logMessage) === false) {
            throw new Exception("Failed to write to log file: {$logFilePath}");
        }

        fclose($logFileHandle);
    } catch (Exception $e) {
        // Log errors to a temporary file
        $errorLogFilePath = $tmpDir . 'error_log.txt';
        file_put_contents(
            $errorLogFilePath,
            "[{$timestamp}] " . $e->getMessage() . "\n",
            FILE_APPEND
        );
    }
}

// Example usage
logServerActivity('Server started successfully.', 'info');
logServerActivity('An error occurred while connecting to the database.', 'error');
logServerActivity('Debugging request headers.', 'debug');
?>
```
