"""
Generated Code Metadata:
========================
Original URL: https://app.marketpoly.net
Prompt: Create a PHP script that uses "key.php" to authenticate users based on predefined keys and logs failed attempts.
Generated: DETERMINISTIC_1831c33de3fe496f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**auth.php**
```php
<?php

/**
 * Authentication script using predefined keys.
 */

// Configuration
$logFile = 'auth.log';
$maxAttempts = 5; // Maximum number of failed attempts before blocking

// Include key configuration
require_once 'key.php';

/**
 * Authenticate a user based on a provided key.
 *
 * @param string $key The authentication key.
 * @return bool True if authentication is successful, false otherwise.
 */
function authenticate($key) {
    global $keys;
    if (isset($keys[$key])) {
        return true;
    }
    return false;
}

/**
 * Log a failed authentication attempt.
 *
 * @param string $key The authentication key that failed.
 */
function logFailedAttempt($key) {
    global $logFile;
    $timestamp = date('Y-m-d H:i:s');
    $logEntry = "$timestamp - Failed authentication attempt for key: $key\n";
    file_put_contents($logFile, $logEntry, FILE_APPEND);
}

/**
 * Check if an IP is blocked due to excessive failed attempts.
 *
 * @param string $ip The IP address to check.
 * @return bool True if the IP is blocked, false otherwise.
 */
function isIpBlocked($ip) {
    global $logFile, $maxAttempts;
    $failedAttempts = 0;
    $logEntries = file($logFile, FILE_IGNORE_NEW_LINES);
    foreach ($logEntries as $entry) {
        if (strpos($entry, $ip) !== false) {
            $failedAttempts++;
            if ($failedAttempts >= $maxAttempts) {
                return true;
            }
        }
    }
    return false;
}

// Get the client's IP address
$clientIp = $_SERVER['REMOTE_ADDR'];

// Check if the client's IP is blocked
if (isIpBlocked($clientIp)) {
    http_response_code(403);
    echo "Forbidden: Your IP has been blocked due to excessive failed authentication attempts.";
    exit;
}

// Get the authentication key from the request
$key = $_SERVER['PHP_AUTH_USER'] ?? $_POST['key'] ?? null;

// Authenticate the user
if (authenticate($key)) {
    // Authentication successful
    http_response_code(200);
    echo "Authenticated successfully.";
} else {
    // Authentication failed
    logFailedAttempt($key);
    http_response_code(401);
    echo "Authentication failed.";
}

?>
```

**key.php**
```php
<?php

/**
 * Predefined authentication keys.
 */

// Example keys (replace with your own)
$keys = [
    'user1' => 'password1',
    'user2' => 'password2',
];

?>
```
