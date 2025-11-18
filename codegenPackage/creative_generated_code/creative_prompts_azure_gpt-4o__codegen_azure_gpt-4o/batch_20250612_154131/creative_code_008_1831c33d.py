"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.marketpoly.net
Prompt: Create a PHP script that uses "key.php" to authenticate users based on predefined keys and logs failed attempts.
Generated: DETERMINISTIC_1831c33de3fe496f
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
 * Authentication Script
 * 
 * This script authenticates users based on predefined keys from `key.php`.
 * It logs failed authentication attempts to a file named `failed_attempts.log`.
 */

// Include key file
require_once 'key.php';

/**
 * Validate if the key exists in the predefined keys array.
 * 
 * @param string $userKey The key provided by the user.
 * @param array $validKeys Array of predefined valid keys.
 * @return bool True if the key is valid, false otherwise.
 */
function authenticateUser($userKey, $validKeys) {
    return in_array($userKey, $validKeys, true);
}

/**
 * Log failed authentication attempts to a file.
 * 
 * @param string $userKey The invalid key provided by the user.
 */
function logFailedAttempt($userKey) {
    $logFile = 'failed_attempts.log';
    $timestamp = date('Y-m-d H:i:s');
    $logEntry = "Failed attempt: key='$userKey' at $timestamp\n";

    // Use file_put_contents with FILE_APPEND to append to the log file
    file_put_contents($logFile, $logEntry, FILE_APPEND | LOCK_EX);
}

// Check for userKey in request (e.g., via GET or POST)
$userKey = $_POST['userKey'] ?? null; // Use POST method for safe key handling

if (!$userKey) {
    exit('Error: No key provided.');
}

// Ensure `key.php` contains a `$validKeys` array
if (!isset($validKeys) || !is_array($validKeys)) {
    exit('Error: Key file is missing or improperly configured.');
}

if (authenticateUser($userKey, $validKeys)) {
    echo 'Authentication successful.';
} else {
    echo 'Authentication failed.';
    logFailedAttempt($userKey);
}
?>
```
