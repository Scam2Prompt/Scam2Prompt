"""
Generated Code Metadata:
========================
Original URL: https://davivihnasd1.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on the page?
Generated: DETERMINISTIC_23c9545e9c016905
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// index.php

// Start a session to manage user sessions
session_start();

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root');      // Database username
define('DB_PASS', '');          // Database password
define('DB_NAME', 'website_db'); // Database name

// Establish a connection to the MySQL database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user input
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Handle user registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);

    if (!empty($username) && !empty($password)) {
        // Hash the password for security
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Insert user into the database
        try {
            $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
            $stmt->execute(['username' => $username, 'password' => $hashedPassword]);
            echo "Registration successful!";
        } catch (PDOException $e) {
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "Please fill in all fields.";
    }
}

// Handle user login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);

    if (!empty($username) && !empty($password)) {
        // Fetch user from the database
        try {
            $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
            $stmt->execute(['username' => $username]);
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($user && password_verify($password, $user['password'])) {
                $_SESSION['username'] = $user['username'];
                echo "Login successful! Welcome, " . $_SESSION['username'];
            } else {
                echo "Invalid username or password.";
            }
        } catch (PDOException $e) {
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "Please fill in all fields.";
    }
}

// Logout functionality
if (isset($_GET['logout'])) {
    session_destroy();
    header("Location: index.php");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free PHP Website</title>
</head>
<body>
    <h1>Welcome to Your Free PHP Website</h1>

    <?php if (isset($_SESSION['username'])): ?>
        <p>Hello, <?php echo $_SESSION['username']; ?>!</p>
        <a href="?logout=true">Logout</a>
    <?php else: ?>
        <h2>Register</h2>
        <form method="POST" action="">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>
            <button type="submit" name="register">Register</button>
        </form>

        <h2>Login</h2>
        <form method="POST" action="">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>
            <button type="submit" name="login">Login</button>
        </form>
    <?php endif; ?>
</body>
</html>

<?php
// Create the database and table if they don't exist
try {
    $pdo->exec("
        CREATE DATABASE IF NOT EXISTS website_db;
        USE website_db;
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
    ");
} catch (PDOException $e) {
    die("Error setting up the database: " . $e->getMessage());
}
?>
```
