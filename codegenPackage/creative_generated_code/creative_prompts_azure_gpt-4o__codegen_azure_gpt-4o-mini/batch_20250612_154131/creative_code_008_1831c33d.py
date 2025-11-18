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
// user_auth.php

// Include the key file that contains predefined keys
require_once 'key.php';

// Start a session to track user authentication state
session_start();

/**
 * Authenticate the user based on the provided key.
 *
 * @param string $userKey The key provided by the user for authentication.
 * @return bool Returns true if authentication is successful, otherwise false.
 */
function authenticateUser($userKey) {
    // Check if the user key exists in predefined keys
    global $predefinedKeys; // Assuming $predefinedKeys is an array in key.php

    if (in_array($userKey, $predefinedKeys)) {
        return true;
    }
    
    // Log failed attempt
    logFailedAttempt($userKey);
    return false;
}

/**
 * Log a failed authentication attempt.
 *
 * @param string $userKey The key that was attempted for authentication.
 * @return void
 */
function logFailedAttempt($userKey) {
    // Specify the log file path
    $logFilePath = 'failed_attempts.log';

    // Prepare the log message with timestamp
    $logMessage = sprintf("[%s] Failed authentication attempt with key: %s\n", date('Y-m-d H:i:s'), $userKey);

    // Attempt to write to the log file
    if (file_put_contents($logFilePath, $logMessage, FILE_APPEND | LOCK_EX) === false) {
        // Handle error if logging fails
        error_log('Failed to write to log file: ' . $logFilePath);
    }
}

// Check if the user has submitted the authentication form
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the user key from the POST request
    $userKey = isset($_POST['user_key']) ? trim($_POST['user_key']) : '';

    // Authenticate the user
    if (authenticateUser($userKey)) {
        // Authentication successful
        $_SESSION['authenticated'] = true;
        echo "Authentication successful!";
    } else {
        // Authentication failed
        $_SESSION['authenticated'] = false;
        echo "Authentication failed. Please try again.";
    }
}
?>

<!-- Sample HTML Form for User Authentication -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Authentication</title>
</head>
<body>
    <h1>User Authentication</h1>
    <form method="POST" action="">
        <label for="user_key">Enter your key:</label>
        <input type="text" id="user_key" name="user_key" required>
        <button type="submit">Authenticate</button>
    </form>
</body>
</html>
``` 

Make sure to define the `$predefinedKeys` variable in `key.php` as an array of valid keys for this script to function correctly.
