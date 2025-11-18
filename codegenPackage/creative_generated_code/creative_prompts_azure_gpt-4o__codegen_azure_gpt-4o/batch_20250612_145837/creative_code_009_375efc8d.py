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

/**
 * Server Activity Logger
 *
 * This script logs server activity into the `logs/` directory.
 * It uses PHP 8.3 features for efficient, large-scale logging.
 */

// Configuration
const LOG_DIRECTORY = __DIR__ . '/logs/';
const LOG_FILE_NAME = 'server_activity.log';
const MAX_LOG_FILE_SIZE = 10 * 1024 * 1024; // 10 MB

// Ensure the logs directory exists
if (!is_dir(LOG_DIRECTORY)) {
    if (!mkdir(LOG_DIRECTORY, 0755, true)) {
        throw new RuntimeException('Failed to create logs directory.');
    }
}

/**
 * Logs a message to the log file.
 *
 * @param string $message The message to log.
 * @return void
 */
function logActivity(string $message): void
{
    $logFilePath = LOG_DIRECTORY . LOG_FILE_NAME;

    // Check if log file exists and its size
    if (file_exists($logFilePath) && filesize($logFilePath) > MAX_LOG_FILE_SIZE) {
        // Rotate log file: Rename old file and create a new one
        $timestamp = date('Y-m-d_H-i-s');
        $archivedLogFile = LOG_DIRECTORY . "server_activity_$timestamp.log";
        if (!rename($logFilePath, $archivedLogFile)) {
            throw new RuntimeException('Failed to archive log file.');
        }
    }

    // Append the log message to the file
    $logEntry = sprintf("[%s] %s%s", date('Y-m-d H:i:s'), $message, PHP_EOL);

    if (file_put_contents($logFilePath, $logEntry, FILE_APPEND | LOCK_EX) === false) {
        throw new RuntimeException('Failed to write to log file.');
    }
}

// Example usage
try {
    logActivity('Server started successfully.');
    logActivity('Processing incoming request...');
    logActivity('Request completed successfully.');
} catch (Throwable $e) {
    // Handle exceptions and log error
    error_log(sprintf("Logging error: %s", $e->getMessage()));
}
```
