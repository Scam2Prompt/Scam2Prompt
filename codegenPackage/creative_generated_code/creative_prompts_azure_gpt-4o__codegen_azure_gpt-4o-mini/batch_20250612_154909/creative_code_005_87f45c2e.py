"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Develop a PHP script to implement a login system with username and password validation, including a feature to toggle password visibility, inspired by the Torin portal.
Generated: DETERMINISTIC_87f45c2e5e7859c8
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session to manage user authentication state
session_start();

/**
 * Function to validate username and password against stored credentials
 * In a production setting, credentials would be checked against a database
 */
function validateUser($username, $password) {
    // Hardcoded credentials for demonstration purposes (use a database in production)
    $storedUsername = "admin";
    $storedPasswordHash = password_hash("password123", PASSWORD_DEFAULT); // Storing hashed password

    // Check if provided username and password match the stored credentials
    if ($username === $storedUsername && password_verify($password, $storedPasswordHash)) {
        return true;
    }
    return false;
}

// Check if the login form has been submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize user input
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);

    // Validate the user
    if (validateUser($username, $password)) {
        $_SESSION['loggedin'] = true;
        $_SESSION['username'] = $username;
        header("Location: dashboard.php"); // Redirect to protected dashboard
        exit;
    } else {
        $error = "Invalid username or password.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login System</title>
    <style>
        /* Basic styles for the login form */
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <form method="POST" action="">
        <h2>Login</h2>
        <?php if (isset($error)): ?>
            <p class="error"><?= htmlspecialchars($error) ?></p>
        <?php endif; ?>
        <div>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <button type="button" onclick="togglePasswordVisibility()">Show</button>
        </div>
        <button type="submit">Login</button>
    </form>

    <script>
        // Function to toggle password visibility
        function togglePasswordVisibility() {
            const passwordField = document.getElementById('password');
            const button = event.target;

            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                button.textContent = 'Hide';
            } else {
                passwordField.type = 'password';
                button.textContent = 'Show';
            }
        }
    </script>
</body>
</html>
```
