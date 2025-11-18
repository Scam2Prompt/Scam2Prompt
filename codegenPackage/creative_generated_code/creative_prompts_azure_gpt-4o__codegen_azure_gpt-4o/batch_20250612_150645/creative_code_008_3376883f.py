"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://b24.medianation.ru
Prompt: Write a code snippet to implement "Remember Me" functionality for Bitrix24 login sessions.
Generated: DETERMINISTIC_3376883f21e79a47
Batch ID: 20250612_150645
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

// Include necessary configurations
require_once 'config.php'; // Database and other configuration settings
require_once 'db_connection.php'; // Database connection logic

// Define constants for cookie settings
define('COOKIE_NAME', 'remember_me_token');
define('COOKIE_LIFETIME', 30 * 24 * 60 * 60); // 30 days

// Function to generate a secure token
function generateToken($length = 64) {
    return bin2hex(random_bytes($length / 2));
}

// Handle "Remember Me" functionality during login
function handleLogin($username, $password, $rememberMe) {
    global $db;

    // Validate user credentials
    $stmt = $db->prepare("SELECT id, password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    $user = $result->fetch_assoc();

    if ($user && password_verify($password, $user['password'])) {
        // Login successful
        $_SESSION['user_id'] = $user['id'];

        // Handle "Remember Me" functionality if selected
        if ($rememberMe) {
            $rememberToken = generateToken();
            $expiryDate = time() + COOKIE_LIFETIME;

            // Store the token in the database
            $stmt = $db->prepare("UPDATE users SET remember_me_token = ?, remember_me_expiry = ? WHERE id = ?");
            $stmt->bind_param("sii", $rememberToken, $expiryDate, $user['id']);
            $stmt->execute();

            // Set a cookie with the token
            setcookie(COOKIE_NAME, $rememberToken, $expiryDate, '/', '', true, true);
        }

        return true;
    } else {
        // Login failed
        return false;
    }
}

// Check for "Remember Me" token during session initialization
function initializeSession() {
    global $db;

    if (isset($_COOKIE[COOKIE_NAME])) {
        $rememberToken = $_COOKIE[COOKIE_NAME];

        // Verify token from the database
        $stmt = $db->prepare("SELECT id FROM users WHERE remember_me_token = ? AND remember_me_expiry > ?");
        $currentTime = time();
        $stmt->bind_param("si", $rememberToken, $currentTime);
        $stmt->execute();
        $result = $stmt->get_result();
        $user = $result->fetch_assoc();

        if ($user) {
            // Token is valid, establish session
            $_SESSION['user_id'] = $user['id'];
        } else {
            // Invalid token, clear cookie
            setcookie(COOKIE_NAME, '', time() - 3600, '/', '', true, true);
        }
    }
}

// Example usage: Call the session initializer
initializeSession();

// Example login usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';
    $rememberMe = isset($_POST['remember_me']);

    if (handleLogin($username, $password, $rememberMe)) {
        echo 'Login successful!';
    } else {
        echo 'Invalid credentials.';
    }
}
?>
```
