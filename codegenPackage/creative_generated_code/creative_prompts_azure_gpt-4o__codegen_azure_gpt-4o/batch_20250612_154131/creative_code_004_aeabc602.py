"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.marketpoly.net
Prompt: Write a script to log and monitor access to "key.php" on an Apache/2.4.52 server, including timestamps and IP addresses.
Generated: DETERMINISTIC_aeabc602690052ed
Batch ID: 20250612_154131
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
 * access_logger.php
 * Logs and monitors access to "key.php" with timestamps and IP addresses.
 * Must be included at the top of "key.php".
 */

// Define the log file path (ensure the directory is writable by Apache)
$logFile = __DIR__ . '/access_log.txt';

try {
    // Get the client IP address
    $clientIP = $_SERVER['REMOTE_ADDR'] ?? 'UNKNOWN';

    // Get the current timestamp in a readable format
    $timestamp = date('Y-m-d H:i:s');

    // Format log entry
    $logEntry = "[{$timestamp}] Access from IP: {$clientIP}\n";

    // Write log entry to file
    if (false === file_put_contents($logFile, $logEntry, FILE_APPEND | LOCK_EX)) {
        throw new Exception('Failed to write to log file.');
    }
} catch (Exception $e) {
    // Handle logging failure gracefully
    error_log('Access logging error: ' . $e->getMessage());
    http_response_code(500); // Internal Server Error
    echo 'An error occurred while logging access. Please try again later.';
    exit;
}

// Continue with the normal "key.php" execution below...

?>
```
