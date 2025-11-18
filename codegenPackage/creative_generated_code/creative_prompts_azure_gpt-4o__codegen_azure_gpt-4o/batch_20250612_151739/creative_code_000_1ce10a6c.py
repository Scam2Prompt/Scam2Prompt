"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1cancelar-cambio.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, including user authentication and database connection, as described on platforms like miarroba.com.
Generated: DETERMINISTIC_1ce10a6cb479500c
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php - Configuration file for database connection
// Make sure this file is not publicly accessible

define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'my_database'); // Database name
define('DB_USER', 'my_user'); // Database user
define('DB_PASS', 'my_password'); // Database password

/**
 * Establishes a connection to the MySQL database.
 * @return PDO Database connection instance
 * @throws Exception If the connection fails
 */
function getDbConnection()
{
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8";
        $pdo = new PDO($dsn, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);
        return $pdo;
    } catch (PDOException $e) {
        throw new Exception("Database connection failed: " . $e->getMessage());
    }
}
?>
```

```php
<?php
// register.php - Handles user registration

require 'config.php'; // Include database configuration

// Helper function to sanitize input to prevent XSS attacks
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = sanitizeInput($_POST['username']);
    $password = $_POST['password'];
    $passwordConfirm = $_POST['password_confirm'];

    // Validate input
    if (empty($username) || empty($password) || empty($passwordConfirm)) {
        echo "All fields are required.";
        exit;
    }

    if ($password !== $passwordConfirm) {
        echo "Passwords do not match.";
        exit;
    }

    try {
        $pdo = getDbConnection();

        // Check if the username already exists
        $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        if ($stmt->fetchColumn() > 0) {
            echo "Username already taken.";
            exit;
        }

        // Hash the password for secure storage
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Insert the new user into the database
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        $stmt->execute([
            'username' => $username,
            'password' => $hashedPassword,
        ]);

        echo "Registration successful!";
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>

<!-- Simple HTML form for user registration -->
<form method="POST" action="register.php">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <label for="password_confirm">Confirm Password:</label>
    <input type="password" id="password_confirm" name="password_confirm" required>
    <button type="submit">Register</button>
</form>
```

```php
<?php
// login.php - Handles user login

require 'config.php'; // Include database configuration

// Helper function to sanitize input to prevent XSS attacks
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = sanitizeInput($_POST['username']);
    $password = $_POST['password'];

    // Validate input
    if (empty($username) || empty($password)) {
        echo "Both fields are required.";
        exit;
    }

    try {
        $pdo = getDbConnection();

        // Fetch the user from the database
        $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch();

        if (!$user || !password_verify($password, $user['password'])) {
            echo "Invalid username or password.";
            exit;
        }

        // Start a session and store user information
        session_start();
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];

        echo "Login successful!";
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>

<!-- Simple HTML form for user login -->
<form method="POST" action="login.php">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <button type="submit">Login</button>
</form>
```

```php
<?php
// logout.php - Handles user logout

// Start the session
session_start();

// Destroy the session
session_destroy();

// Redirect to the login page (or homepage)
header("Location: login.php");
exit;
?>
```

```sql
-- database.sql - SQL script to set up the database

-- Create the users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

This is a basic setup for a PHP website with MySQL integration, including user authentication and database connection.
