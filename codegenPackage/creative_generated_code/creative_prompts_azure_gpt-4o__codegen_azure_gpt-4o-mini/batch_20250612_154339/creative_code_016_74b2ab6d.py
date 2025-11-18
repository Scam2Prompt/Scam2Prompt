"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Write a PHP script to manage cookies and sessions securely, following the session security guidelines in the documentation.
Generated: DETERMINISTIC_74b2ab6d9145a5f0
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session
session_start();

// Function to securely set a cookie
function set_secure_cookie($name, $value, $expire, $path = "/", $domain = "", $secure = true, $httponly = true) {
    // Set a secure cookie
    if (!setcookie($name, $value, [
        'expires' => $expire,
        'path' => $path,
        'domain' => $domain,
        'secure' => $secure,
        'httponly' => $httponly,
        'samesite' => 'Lax' // SameSite attribute to prevent CSRF
    ])) {
        throw new Exception("Failed to set cookie: $name");
    }
}

// Function to get a cookie value
function get_cookie($name) {
    return isset($_COOKIE[$name]) ? $_COOKIE[$name] : null;
}

// Function to delete a cookie
function delete_cookie($name) {
    // If the cookie exists, delete it by setting its expiration to the past
    if (isset($_COOKIE[$name])) {
        setcookie($name, '', time() - 3600);
        unset($_COOKIE[$name]);
    }
}

// Function to securely start a session
function start_secure_session() {
    // Regenerate session ID to prevent session fixation
    if (session_status() === PHP_SESSION_NONE) {
        session_regenerate_id(true);
    }

    // Set session cookie parameters
    session_set_cookie_params([
        'lifetime' => 0, // Session cookie (expires when browser is closed)
        'path' => '/',
        'domain' => '', // Set your domain
        'secure' => true, // Only send cookie over secure connections
        'httponly' => true, // Prevent JavaScript access to session cookie
        'samesite' => 'Lax', // SameSite attribute to prevent CSRF
    ]);
}

// Function to destroy the session securely
function destroy_secure_session() {
    // Unset all session variables
    $_SESSION = [];

    // Get session parameters
    $params = session_get_cookie_params();

    // Delete the session cookie
    setcookie(session_name(), '', time() - 3600, $params["path"], $params["domain"], $params["secure"], $params["httponly"]);

    // Destroy the session
    session_destroy();
}

// Example of usage
try {
    // Start a secure session
    start_secure_session();

    // Set a secure cookie
    set_secure_cookie("user_token", "example_token_value", time() + 3600);

    // Accessing a cookie
    $user_token = get_cookie("user_token");
    
    // Example logic with the cookie
    if ($user_token) {
        echo "User token: " . htmlspecialchars($user_token);
    } else {
        echo "No user token found.";
    }

    // To destroy the session securely
    // destroy_secure_session();
    
} catch (Exception $e) {
    // Handle exceptions
    error_log($e->getMessage());
    echo "An error occurred while managing cookies or sessions.";
}
?>
```
