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
session_start(); // Start the session to manage user sessions

// Function to set a cookie
function setUserCookie($username, $expireHours = 24) {
    $cookieName = 'user_auth';
    $cookieValue = $username;
    $expireTime = time() + ($expireHours * 3600); // Set expiration time for the cookie
    setcookie($cookieName, $cookieValue, $expireTime, "/"); // Set the cookie for the entire domain
}

// Function to validate user credentials (dummy implementation for example)
function validateUser($username, $password) {
    // In a real application, replace this with secure database validation
    $validUser = "admin";
    $validPass = "password123";

    return ($username === $validUser && $password === $validPass);
}

// Function to log in the user
function loginUser($username, $password) {
    if (validateUser($username, $password)) {
        $_SESSION['username'] = $username; // Store username in session
        setUserCookie($username); // Set a cookie for the user
        return true; // Login successful
    }
    return false; // Login failed
}

// Function to log out the user
function logoutUser() {
    // Unset all session variables
    $_SESSION = [];
    // Invalidate the session cookie
    if (ini_get("session.use_cookies")) {
        $params = session_get_cookie_params();
        setcookie(session_name(), '', time() - 42000,
            $params["path"], $params["domain"], $params["secure"], $params["httponly"]
        );
    }
    // Destroy the session
    session_destroy();
}

// Check if the user is already logged in
function isLoggedIn() {
    return isset($_SESSION['username']);
}

// Example usage of login and logout
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['login'])) {
        // Retrieve username and password from POST request
        $username = $_POST['username'] ?? '';
        $password = $_POST['password'] ?? '';
        
        // Attempt to log in the user
        if (loginUser($username, $password)) {
            echo "Login successful! Welcome, " . htmlspecialchars($username) . "!";
        } else {
            echo "Login failed! Invalid username or password.";
        }
    }

    if (isset($_POST['logout'])) {
        logoutUser();
        echo "You have been logged out.";
    }
}
?>

<!-- HTML form for user login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Authentication</title>
</head>
<body>
    <?php if (!isLoggedIn()): ?>
        <form method="POST" action="">
            <h2>Login</h2>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>
            <input type="submit" name="login" value="Login">
        </form>
    <?php else: ?>
        <h2>Welcome, <?php echo htmlspecialchars($_SESSION['username']); ?>!</h2>
        <form method="POST" action="">
            <input type="submit" name="logout" value="Logout">
        </form>
    <?php endif; ?>
</body>
</html>
```
