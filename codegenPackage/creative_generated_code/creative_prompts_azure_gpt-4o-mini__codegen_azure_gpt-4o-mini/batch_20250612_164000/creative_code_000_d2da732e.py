"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sugerencias.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with a custom domain?
Generated: DETERMINISTIC_d2da732edb2e96d9
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php - Main entry point of the website

// Start a session for user management
session_start();

// Include database connection
require 'db.php';

// Handle user registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    // Validate and sanitize user input
    $username = filter_var(trim($_POST['username']), FILTER_SANITIZE_STRING);
    $password = password_hash(trim($_POST['password']), PASSWORD_DEFAULT); // Hash the password

    if (empty($username) || empty($password)) {
        $error = "Username and password cannot be empty.";
    } else {
        // Store user in the database
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
        if ($stmt->execute([$username, $password])) {
            $success = "Registration successful!";
        } else {
            $error = "Registration failed. Please try again.";
        }
    }
}

// Handle user login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    // Validate and sanitize user input
    $username = filter_var(trim($_POST['username']), FILTER_SANITIZE_STRING);
    $password = trim($_POST['password']);

    // Retrieve user data from the database
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user && password_verify($password, $user['password'])) {
        // Set up session for the logged-in user
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        header("Location: dashboard.php");
        exit();
    } else {
        $error = "Invalid username or password.";
    }
}

// Check for logged-in user
$isLoggedIn = isset($_SESSION['user_id']);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP MySQL Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to My Free Website</h1>

    <?php if ($isLoggedIn): ?>
        <p>Welcome, <?= htmlspecialchars($_SESSION['username']) ?>! <a href="logout.php">Logout</a></p>
    <?php else: ?>
        <form method="post">
            <h2>Register</h2>
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit" name="register">Register</button>
        </form>

        <form method="post">
            <h2>Login</h2>
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit" name="login">Login</button>
        </form>

        <?php if (isset($error)) echo "<p style='color: red;'>$error</p>"; ?>
        <?php if (isset($success)) echo "<p style='color: green;'>$success</p>"; ?>
    <?php endif; ?>
</body>
</html>
```

```php
<?php
// db.php - Database connection setup

// Database configuration
$host = 'localhost'; // Change this to your database host
$db = 'my_database'; // Change this to your database name
$user = 'my_user';   // Change this to your database user
$pass = 'my_password'; // Change this to your database password

try {
    // Creating a PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exceptions for error handling
} catch (PDOException $e) {
    // Handle database connection errors
    die("Database connection failed: " . $e->getMessage());
}
?>
```

```php
<?php
// logout.php - Handle user logout

// Start session
session_start();

// Unset all session variables
$_SESSION = [];

// Destroy the session
session_destroy();

// Redirect to homepage
header("Location: index.php");
exit();
?>
```

```sql
-- database_setup.sql - SQL script to set up the database

CREATE DATABASE my_database;

USE my_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```css
/* styles.css - Basic styles for the website */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

h1, h2 {
    color: #333;
}

form {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    background: #fff;
}

input[type="text"], input[type="password"] {
    width: 100%;
    padding: 10px;
    margin: 5px 0;
}

button {
    padding: 10px;
    color: white;
    background-color: #28a745;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```

This code provides a simple PHP and MySQL-based user registration and login system, with error handling and basic styling. Adjust the database credentials in `db.php` and run the SQL script to set up the database before testing the application.
