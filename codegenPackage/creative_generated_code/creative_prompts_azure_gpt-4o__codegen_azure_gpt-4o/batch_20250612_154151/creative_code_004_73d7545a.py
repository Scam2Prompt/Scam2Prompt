"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon-farming.pro
Prompt: Write a PHP script that logs and timestamps access to a file like `key.php` on an Apache server.
Generated: DETERMINISTIC_73d7545a31955de6
Batch ID: 20250612_154151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: access_logger.php

// Configuration
$logFile = __DIR__ . '/access_log.txt'; // Path to the log file
$targetFile = 'key.php'; // Name of the file being accessed

// Function to log access
function logAccess($logFile, $fileAccessed) {
    try {
        // Get the current timestamp
        $timestamp = date('Y-m-d H:i:s');

        // Get the client IP address
        $clientIP = $_SERVER['REMOTE_ADDR'] ?? 'UNKNOWN';

        // Format the log entry
        $logEntry = "[{$timestamp}] - File Accessed: {$fileAccessed} - IP: {$clientIP}\n";

        // Write the log entry to the log file
        file_put_contents($logFile, $logEntry, FILE_APPEND | LOCK_EX);
    } catch (Exception $e) {
        // Log the error message if logging fails
        error_log("Error logging access: " . $e->getMessage());
    }
}

// Check if the target file is being accessed
if (basename($_SERVER['SCRIPT_FILENAME']) === $targetFile) {
    // Log the access
    logAccess($logFile, $targetFile);
}
?>
```
