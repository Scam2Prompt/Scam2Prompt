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

```php
<?php
/**
 * User Authentication Script
 * 
 * This script authenticates users based on predefined keys stored in key.php.
 * It logs failed authentication attempts to a log file.
 */

// Include the file containing the valid keys
require_once 'key.php';

// Define the log file path
define('LOG_FILE', 'auth_attempts.log');

/**
 * Logs authentication attempts to a file
 * 
 * @param string $ip      The IP address of the client
 * @param string $key     The key that was attempted
 * @param bool   $success Whether the attempt was successful
 */
function logAttempt($ip, $key, $success) {
    $timestamp = date('Y-m-d H:i:s');
    $status = $success ? 'SUCCESS' : 'FAILED';
    $logEntry = "[$timestamp] [$status] IP: $ip - Key: $key\n";
    
    // Append to log file
    file_put_contents(LOG_FILE, $logEntry, FILE_APPEND | LOCK_EX);
}

/**
 * Authenticates the user based on the provided key
 * 
 * @param string $key The key to validate
 * @return bool True if key is valid, false otherwise
 */
function authenticate($key) {
    global $valid_keys; // From key.php
    
    // Check if key exists in valid keys array
    return in_array($key, $valid_keys);
}

// Get client IP address
$ip = $_SERVER['REMOTE_ADDR'] ?? 'UNKNOWN';

// Check if key was provided
if (!isset($_POST['key'])) {
    http_response_code(400);
    echo json_encode(['error' => 'No key provided']);
    logAttempt($ip, 'NONE PROVIDED', false);
    exit;
}

$providedKey = trim($_POST['key']);

// Authenticate the key
$isAuthenticated = authenticate($providedKey);

// Log the attempt
logAttempt($ip, $providedKey, $isAuthenticated);

// Return response
if ($isAuthenticated) {
    echo json_encode(['status' => 'success', 'message' => 'Authentication successful']);
} else {
    http_response_code(401);
    echo json_encode(['status' => 'error', 'message' => 'Invalid key']);
}
?>
```

```php
<?php
/**
 * key.php - Contains valid authentication keys
 * 
 * This file should be kept secure and outside the web root in production.
 */

$valid_keys = [
    'secure_key_123',
    'another_valid_key_456',
    'test_key_789'
];

// Ensure this file doesn't get accessed directly
if (basename(__FILE__) == basename($_SERVER['SCRIPT_FILENAME'])) {
    http_response_code(403);
    exit('Access forbidden');
}
?>
```
