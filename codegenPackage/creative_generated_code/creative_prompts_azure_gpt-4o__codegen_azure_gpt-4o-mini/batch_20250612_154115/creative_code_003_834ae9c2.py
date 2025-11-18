"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.newtork.cc
Prompt: Generate PHP code to log and monitor access to a file named `key.php` on an Apache server.
Generated: DETERMINISTIC_834ae9c2c4ae6b54
Batch ID: 20250612_154115
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
 *
 * This script logs access attempts to the key.php file and monitors
 * the IP address, timestamp, and user agent of each request.
 */

// Define the log file path
define('LOG_FILE', __DIR__ . '/access_log.txt');

/**
 * Log access attempt to the log file.
 *
 * @param string $message The message to log.
 * @return void
 */
function logAccess($message) {
    // Check if the log file is writable
    if (!is_writable(LOG_FILE)) {
        error_log('Log file is not writable: ' . LOG_FILE);
        return;
    }

    // Prepare the log message
    $timestamp = date('Y-m-d H:i:s');
    $logMessage = "[$timestamp] $message" . PHP_EOL;

    // Write to the log file
    file_put_contents(LOG_FILE, $logMessage, FILE_APPEND | LOCK_EX);
}

// Get client details
$clientIP = $_SERVER['REMOTE_ADDR'];
$userAgent = $_SERVER['HTTP_USER_AGENT'];

// Log the access attempt
logAccess("Accessed by IP: $clientIP | User Agent: $userAgent");

// Check access permission (dummy check, replace with actual logic if needed)
if (!hasAccess()) {
    http_response_code(403); // Forbidden
    echo "Access denied.";
    logAccess("Access denied for IP: $clientIP");
    exit;
}

// Dummy function for access validation
function hasAccess() {
    // Implement actual access control logic if necessary
    return true; // Allow access for demonstration purposes
}

// Proceed with the main logic of key.php
echo "Access granted to key.php.";
```

This code will log access attempts to `key.php` along with the client's IP address and user agent, while handling errors appropriately.
