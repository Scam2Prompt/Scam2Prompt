"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonaeac.com
Prompt: Develop a login authentication system in PHP that verifies username and password credentials, as outlined on the bonaeac.com website.
Generated: DETERMINISTIC_b7e14622b199ef6f
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Login Authentication System
 * Author: Your Name
 * Date: YYYY-MM-DD
 * 
 * This script provides a secure login authentication system in PHP.
 * It verifies username and password credentials stored in a database.
 */

// Start session to manage user authentication state
session_start();

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'yourpassword');
define('DB_NAME', 'yourdatabase');

/**
 * Connect to the database.
 *
 * @return mysqli|false Database connection object or false on failure.
 */
function connectToDatabase() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    return $conn;
}

/**
 * Validate user credentials.
 *
 * @param string $username The username.
 * @param string $password The password.
 * @return bool True if valid credentials, false otherwise.
 */
function authenticateUser($username, $password) {
    // Establish database connection
    $conn = connectToDatabase();
    if (!$conn) {
        return false;
    }

    // Prepare SQL statement to prevent SQL injection
    $stmt = $conn->prepare("SELECT password FROM users WHERE username = ?");
    if (!$stmt) {
        $conn->close();
        return false;
    }

    // Bind parameters and execute statement
    $stmt->bind_param("s", $username);
    $stmt->execute();

    // Fetch the hashed password from the database
    $stmt->bind_result($hashedPassword);
    $stmt->fetch();

    // Close database resources
    $stmt->close();
    $conn->close();

    // Verify the password using password_verify()
    return password_verify($password, $hashedPassword);
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the username and password from POST data
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Validate user input
    if (empty($username) || empty($password)) {
        $error = "Username and password cannot be empty.";
    } else {
        // Authenticate the user
        if (authenticateUser($username, $password)) {
            // Set session variables if authentication succeeds
            $_SESSION['authenticated'] = true;
            $_SESSION['username'] = $username;

            // Redirect to a secured page (e.g., dashboard)
            header("Location: dashboard.php");
            exit();
        } else {
            $error = "Invalid username or password.";
        }
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <?php if (isset($error)): ?>
        <p style="color: red;"><?php echo htmlspecialchars($error); ?></p>
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
