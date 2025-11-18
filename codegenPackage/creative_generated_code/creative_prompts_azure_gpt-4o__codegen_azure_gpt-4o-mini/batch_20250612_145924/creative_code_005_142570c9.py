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
/**
 * Simple PHP script to log server activity to a specified log folder.
 * This script records the request method, requested URL, and timestamp.
 */

// Define the log file path
define('LOG_DIR', __DIR__ . '/logs/');
define('LOG_FILE', LOG_DIR . 'server_activity.log');

/**
 * Function to log server activity
 *
 * @param string $message The message to log
 * @return void
 */
function logServerActivity($message) {
    // Ensure the logs directory exists
    if (!is_dir(LOG_DIR)) {
        mkdir(LOG_DIR, 0755, true);
    }

    // Prepare the log entry with a timestamp
    $timestamp = date('Y-m-d H:i:s');
    $logEntry = "[{$timestamp}] {$message}" . PHP_EOL;

    // Attempt to write the log entry to the log file
    try {
        file_put_contents(LOG_FILE, $logEntry, FILE_APPEND | LOCK_EX);
    } catch (Exception $e) {
        // Handle any errors during file write
        error_log("Error writing to log file: " . $e->getMessage());
    }
}

// Log the server request method and requested URI
$requestMethod = $_SERVER['REQUEST_METHOD'];
$requestUri = $_SERVER['REQUEST_URI'];
logServerActivity("Request Method: {$requestMethod}, Requested URI: {$requestUri}");

// Optionally, output a simple response
header('Content-Type: text/plain');
echo "Server activity logged successfully.";
?>
```
