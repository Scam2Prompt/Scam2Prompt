"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Generate PHP code to manage sessions securely, as explained in the security section of phpm.ru.
Generated: DETERMINISTIC_df5cac05f533a2e1
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a secure PHP session
function startSecureSession() {
    // Set custom session parameters for enhanced security
    $sessionName = 'secure_session'; // Custom session name
    $secure = true; // Use only HTTPS
    $httponly = true; // Prevent JavaScript access to session cookies

    // Set session cookie parameters
    session_set_cookie_params([
        'lifetime' => 0, // Session cookie expires when the browser is closed
        'path' => '/',
        'domain' => '', // Defaults to current domain
        'secure' => $secure, // Enforce HTTPS
        'httponly' => $httponly, // Disable JavaScript access
        'samesite' => 'Strict' // Prevent CSRF by restricting cookie usage to same-site requests
    ]);

    // Set the session name
    session_name($sessionName);

    // Start the session
    session_start();

    // Regenerate session ID periodically to prevent session fixation attacks
    if (!isset($_SESSION['initialized'])) {
        session_regenerate_id(true);
        $_SESSION['initialized'] = true;
    }
}

// Function to safely store data in the session
function setSessionData($key, $value) {
    if (is_string($key)) {
        $_SESSION[$key] = $value;
    } else {
        throw new InvalidArgumentException('Session key must be a string.');
    }
}

// Function to retrieve data from the session
function getSessionData($key) {
    if (isset($_SESSION[$key])) {
        return $_SESSION[$key];
    }
    return null; // Return null if the key does not exist
}

// Function to delete data from the session
function deleteSessionData($key) {
    if (isset($_SESSION[$key])) {
        unset($_SESSION[$key]);
    }
}

// Ensure session is started securely
try {
    startSecureSession();
} catch (Exception $e) {
    error_log('Session initialization failed: ' . $e->getMessage());
    exit('An error occurred while starting the session.');
}

// Example usage
setSessionData('user_id', 12345); // Store data in session
$userId = getSessionData('user_id'); // Retrieve data from session
deleteSessionData('user_id'); // Delete data from session

// End the session securely
function destroySession() {
    // Clear all session variables
    $_SESSION = [];

    // Delete the session cookie
    if (ini_get('session.use_cookies')) {
        $params = session_get_cookie_params();
        setcookie(session_name(), '', time() - 3600, $params['path'], $params['domain'], $params['secure'], $params['httponly']);
    }

    // Destroy the session
    session_destroy();
}

// Example: Destroy session during logout
destroySession();
?>
```
