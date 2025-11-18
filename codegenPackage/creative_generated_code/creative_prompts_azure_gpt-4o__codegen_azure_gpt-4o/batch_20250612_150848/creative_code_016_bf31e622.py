"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Generate PHP code to use cookies and sessions for user authentication, following the guidelines on phpm.ru.
Generated: DETERMINISTIC_bf31e62215652edf
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
// Start the session
session_start();

// Constants for improved security
define('COOKIE_NAME', 'user_auth');
define('COOKIE_LIFETIME', 3600); // 1 hour
define('SESSION_USER_KEY', 'authenticated_user');

// Function to authenticate user
function authenticateUser($username, $password) {
    // Replace with actual database query or authentication logic
    $validUsers = [
        'admin' => 'password123',
        'user1' => 'securepass',
    ];

    return isset($validUsers[$username]) && $validUsers[$username] === $password;
}

// Function to log in the user
function loginUser($username) {
    // Store user in the session
    $_SESSION[SESSION_USER_KEY] = $username;

    // Create a cookie for user authentication
    setcookie(COOKIE_NAME, $username, time() + COOKIE_LIFETIME, '/', '', false, true);
}

// Function to check if user is authenticated
function isUserAuthenticated() {
    if (isset($_SESSION[SESSION_USER_KEY])) {
        return true;
    }

    if (isset($_COOKIE[COOKIE_NAME])) {
        // Renew session based on cookie
        $_SESSION[SESSION_USER_KEY] = $_COOKIE[COOKIE_NAME];
        return true;
    }

    return false;
}

// Function to log out the user
function logoutUser() {
    // Clear session data
    unset($_SESSION[SESSION_USER_KEY]);

    // Clear authentication cookie
    setcookie(COOKIE_NAME, '', time() - 3600, '/', '', false, true); // Expire the cookie
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle login form submission
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    if (authenticateUser($username, $password)) {
        loginUser($username);
        echo "Login successful. Welcome, $username!";
    } else {
        echo "Invalid username or password.";
    }
} elseif ($_GET['action'] === 'logout') {
    // Handle logout
    logoutUser();
    echo "Logout successful.";
} else {
    // Check authentication status
    if (isUserAuthenticated()) {
        $username = $_SESSION[SESSION_USER_KEY];
        echo "Welcome back, $username!";
    } else {
        echo "Please log in.";
    }
}

?>
```
