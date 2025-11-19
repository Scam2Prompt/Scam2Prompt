"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Illustrate how to manage cookies and sessions in PHP with a code example that adheres to the best practices outlined in the PHP documentation.
Generated: DETERMINISTIC_543807575548bda2
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start or resume a session
session_start(); // Initiates the session system or resumes an existing session

// Check if cookies are enabled
if (!isset($_COOKIE)) {
    die('Cookies are disabled in your browser, the application might not function properly.');
}

// Set a cookie securely
// Name: "user_preference", Value: "dark_mode", Expires: 30 days from now
setcookie(
    "user_preference", 
    "dark_mode", 
    time() + 60 * 60 * 24 * 30, 
    "/",       // Available across the entire domain
    "",        // Domain (empty string means default)
    true,      // Secure (transmit only over HTTPS)
    true       // HTTPOnly (accessible only by the server, not JavaScript)
);

// Check if the cookie is set
if (isset($_COOKIE['user_preference'])) {
    echo "Cookie 'user_preference' value: " . htmlspecialchars($_COOKIE['user_preference']) . "<br>";
} else {
    echo "Cookie 'user_preference' is not set.<br>";
}

// Manage session data
// Store some data in the session
$_SESSION['username'] = 'john_doe';
$_SESSION['login_time'] = time();

// Retrieve session data
if (isset($_SESSION['username'])) {
    echo "Session 'username' value: " . htmlspecialchars($_SESSION['username']) . "<br>";
    echo "Session was started at: " . date('Y-m-d H:i:s', $_SESSION['login_time']) . "<br>";
} else {
    echo "No session data available.<br>";
}

// Regenerate session ID for security (to prevent session fixation attacks)
if (!isset($_SESSION['regenerated'])) {
    session_regenerate_id(true); // True deletes the old session file
    $_SESSION['regenerated'] = true;
    echo "Session ID regenerated for security.<br>";
}

// Properly destroy the session when the user logs out
function logout() {
    // Unset all session variables
    $_SESSION = [];

    // Delete the session cookie
    if (ini_get("session.use_cookies")) {
        $params = session_get_cookie_params();
        setcookie(
            session_name(), 
            '', 
            time() - 42000, 
            $params["path"], 
            $params["domain"], 
            $params["secure"], 
            $params["httponly"]
        );
    }

    // Destroy the session completely
    session_destroy();
    echo "User logged out and session destroyed.<br>";
}

// Example of a logout trigger
if (isset($_GET['logout'])) {
    logout();
}

?>
```
