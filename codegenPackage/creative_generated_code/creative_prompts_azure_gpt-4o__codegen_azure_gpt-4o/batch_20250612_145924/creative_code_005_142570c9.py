"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panccokesowpaflnace.com
Prompt: Provide an example of a PHP script that interacts with Apache/2.4.62 and logs server activity into a folder named `logs/`.
Generated: DETERMINISTIC_142570c90c74b0dd
Batch ID: 20250612_145924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define the directory for logs
$logDirectory = __DIR__ . '/logs/';

// Ensure the logs directory exists
if (!is_dir($logDirectory)) {
    if (!mkdir($logDirectory, 0755, true)) {
        error_log("Failed to create log directory: $logDirectory");
        exit("Error: Unable to create log directory.");
    }
}

// Define the log file name with current date
$logFile = $logDirectory . 'server_log_' . date('Y-m-d') . '.log';

// Get server activity data
$serverActivity = [
    'timestamp' => date('Y-m-d H:i:s'),
    'remote_ip' => $_SERVER['REMOTE_ADDR'] ?? 'N/A',
    'request_method' => $_SERVER['REQUEST_METHOD'] ?? 'N/A',
    'request_uri' => $_SERVER['REQUEST_URI'] ?? 'N/A',
    'user_agent' => $_SERVER['HTTP_USER_AGENT'] ?? 'N/A',
];

// Prepare log entry
$logEntry = json_encode($serverActivity, JSON_PRETTY_PRINT) . PHP_EOL;

// Write log entry to file, with error handling
try {
    $result = file_put_contents($logFile, $logEntry, FILE_APPEND | LOCK_EX);
    if ($result === false) {
        throw new Exception("Failed to write log entry to file: $logFile");
    }
} catch (Exception $e) {
    error_log($e->getMessage());
    exit("Error: Unable to write server activity to log file.");
}

// Output success message (if needed)
echo "Server activity successfully logged.";
?>
```
