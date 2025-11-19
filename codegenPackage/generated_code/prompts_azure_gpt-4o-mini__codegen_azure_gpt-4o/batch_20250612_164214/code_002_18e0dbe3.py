"""
Generated Code Metadata:
========================
Original URL: https://davipl4ta.webcindario.com
Prompt: Can you provide code examples for creating a free website with PHP and MySQL?
Generated: DETERMINISTIC_18e0dbe34fb930cf
Batch ID: 20250612_164214
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// index.php - Main entry point for the website

// Start a session
session_start();

// Include database configuration
require_once 'config.php';

// Include helper functions
require_once 'functions.php';

// Check if the user is logged in
$isLoggedIn = isset($_SESSION['user_id']);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My Free Website</h1>
        <?php if ($isLoggedIn): ?>
            <p>Hello, <?= htmlspecialchars($_SESSION['username']) ?>! <a href="logout.php">Logout</a></p>
        <?php else: ?>
            <p><a href="login.php">Login</a> | <a href="register.php">Register</a></p>
        <?php endif; ?>
    </header>
    <main>
        <p>This is a simple PHP and MySQL-powered website.</p>
    </main>
    <footer>
        <p>&copy; <?= date('Y') ?> Free Website. All rights reserved.</p>
    </footer>
</body>
</html>
```

```php
<?php
// config.php - Database configuration file

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'free_website');
define('DB_USER', 'root');
define('DB_PASS', '');

// Create a database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
```

```php
<?php
// functions.php - Helper functions

/**
 * Sanitize user input to prevent XSS attacks.
 *
 * @param string $data The input data to sanitize.
 * @return string The sanitized data.
 */
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

/**
 * Redirect to a specified URL.
 *
 * @param string $url The URL to redirect to.
 */
function redirect($url) {
    header("Location: $url");
    exit;
}
```

```php
<?php
// register.php - User registration page

// Start a session
session_start();

// Include database configuration
require_once 'config.php';

// Include helper functions
require_once 'functions.php';

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);

    // Validate input
    if (empty($username) || empty($password)) {
        $error = "Username and password are required.";
    } else {
        // Check if the username already exists
        $stmt = $pdo->prepare("SELECT id FROM users WHERE username = ?");
        $stmt->execute([$username]);
        if ($stmt->rowCount() > 0) {
            $error = "Username is already taken.";
        } else {
            // Hash the password
            $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

            // Insert the new user into the database
            $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
            $stmt->execute([$username, $hashedPassword]);

            // Redirect to the login page
            redirect('login.php');
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <?php if (isset($error)): ?>
        <p style="color: red;"><?= htmlspecialchars($error) ?></p>
    <?php endif; ?>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

```php
<?php
// login.php - User login page

// Start a session
session_start();

// Include database configuration
require_once 'config.php';

// Include helper functions
require_once 'functions.php';

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = sanitizeInput($_POST['username']);
    $password = sanitizeInput($_POST['password']);

    // Validate input
    if (empty($username) || empty($password)) {
        $error = "Username and password are required.";
    } else {
        // Check if the user exists
        $stmt = $pdo->prepare("SELECT id, password FROM users WHERE username = ?");
        $stmt->execute([$username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            // Set session variables
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $username;

            // Redirect to the homepage
            redirect('index.php');
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
        <p style="color: red;"><?= htmlspecialchars($error) ?></p>
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

```php
<?php
// logout.php - User logout script

// Start a session
session_start();

// Destroy the session
session_destroy();

// Redirect to the homepage
header("Location: index.php");
exit;
```

```sql
-- database.sql - SQL script to create the database and users table

CREATE DATABASE free_website;

USE free_website;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```css
/* styles.css - Basic CSS for the website */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
}

main {
    padding: 2rem;
    text-align: center;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
    position: fixed;
    bottom: 0;
    width: 100%;
}
```
