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
 * Access Logger for key.php
 * This script logs access to key.php, including timestamp and IP address.
 *
 * Usage: Include this script at the beginning of key.php
 * Ensure that the web server has write permissions to the log directory.
 */

// Define the log file path
define('LOG_FILE', '/var/log/key_access.log');

// Function to log access details
function logAccess() {
    // Get the client's IP address
    $ipAddress = $_SERVER['REMOTE_ADDR'];
    
    // Get the current timestamp in a readable format
    $timestamp = date('Y-m-d H:i:s');
    
    // Prepare the log entry
    $logEntry = sprintf("[%s] Access from IP: %s\n", $timestamp, $ipAddress);
    
    // Attempt to write the log entry to the log file
    try {
        // Ensure the log file is writable
        if (!is_writable(dirname(LOG_FILE))) {
            throw new Exception('Log directory is not writable.');
        }
        
        // Append the log entry to the log file
        file_put_contents(LOG_FILE, $logEntry, FILE_APPEND | LOCK_EX);
    } catch (Exception $e) {
        // Handle errors (could be logged to a different file or displayed)
        error_log("Logging error: " . $e->getMessage());
    }
}

// Call the logAccess function to log the request
logAccess();

// Rest of the key.php script goes here
// ...
?>
```
