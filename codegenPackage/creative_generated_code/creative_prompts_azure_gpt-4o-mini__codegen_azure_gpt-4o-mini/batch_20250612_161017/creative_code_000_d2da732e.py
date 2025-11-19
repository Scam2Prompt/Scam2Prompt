"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupo-virtual.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with a custom domain?
Generated: DETERMINISTIC_d2da732edb2e96d9
Batch ID: 20250612_161017
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
    // Creating a PDO instance for database interaction
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

// Destroy the session to log the user out
session_destroy();

// Redirect to the main page
header("Location: index.php");
exit();
?>
```

```sql
-- database.sql - SQL script to create the required database and table

CREATE DATABASE my_database;

USE my_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

```css
/* styles.css - Basic styles for the website */

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
}

h1 {
    color: #333;
}

form {
    margin-bottom: 20px;
}

input {
    display: block;
    margin: 10px 0;
    padding: 10px;
    width: 300px;
}
```

Make sure to replace placeholders in the configuration with your actual database credentials. This code provides a simple registration and login system using PHP and MySQL.
