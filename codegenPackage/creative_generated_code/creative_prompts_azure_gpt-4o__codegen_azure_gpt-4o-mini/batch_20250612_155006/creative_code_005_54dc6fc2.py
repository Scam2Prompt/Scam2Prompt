"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.com-live.org
Prompt: Create PHP code to restrict access to the `key.php` file based on user authentication, tailored for an Apache/2.4.52 server environment.
Generated: DETERMINISTIC_54dc6fc245d44f7a
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// key.php

// Start the session to access session variables
session_start();

// Define a function to check user authentication
function isAuthenticated() {
    // Check if user is logged in by verifying session variable
    return isset($_SESSION['user_logged_in']) && $_SESSION['user_logged_in'] === true;
}

// Redirect function to send the user to the login page if not authenticated
function redirectToLogin() {
    header("Location: login.php"); // Change to your login page
    exit; // Ensure no further code is executed after redirection
}

// Check if the user is authenticated; if not, redirect to login
if (!isAuthenticated()) {
    redirectToLogin();
}

// If the user is authenticated, continue to serve the content of key.php
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Protected Key Page</title>
</head>
<body>
    <h1>Welcome to the Protected Key Page</h1>
    <p>Your sensitive data can be accessed here.</p>
    <!-- Add your key content here -->
</body>
</html>
```

```php
<?php
// login.php

// Start the session
session_start();

// Dummy authentication (replace this with your actual authentication logic)
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Example user credentials (replace with a database check in production)
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username === 'admin' && $password === 'password') {
        // Set session variable to indicate user is logged in
        $_SESSION['user_logged_in'] = true;
        // Redirect to the protected key page
        header("Location: key.php");
        exit;
    } else {
        // Handle invalid login attempt
        $error_message = "Invalid username or password.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
</head>
<body>
    <h1>Login</h1>
    <?php if (isset($error_message)): ?>
        <div style="color: red;"><?php echo htmlspecialchars($error_message); ?></div>
    <?php endif; ?>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Note:
- Remember to replace the dummy authentication logic with a secure method, such as checking against a database.
- Ensure that sessions are properly managed in your server configuration for security.
