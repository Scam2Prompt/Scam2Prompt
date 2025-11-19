"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idn-hosting.com
Prompt: Develop a simple web application using PHP and MySQL that can be hosted on IDN Hosting's SSD shared hosting platform.
Generated: DETERMINISTIC_89841e993bcfe155
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php - Main entry point for the web application

// Start the session
session_start();

// Include database configuration
require 'config.php';

// Check for user login
if (isset($_SESSION['user_id'])) {
    $user_id = $_SESSION['user_id'];
    // Fetch user details from the database
    $stmt = $pdo->prepare("SELECT username FROM users WHERE id = ?");
    $stmt->execute([$user_id]);
    $user = $stmt->fetch();
} else {
    $user = null;
}

// Handle logout
if (isset($_GET['logout'])) {
    session_destroy();
    header("Location: index.php");
    exit;
}

// HTML for the application
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP MySQL Web App</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Welcome to the Simple Web App</h1>
        <?php if ($user): ?>
            <p>Hello, <?= htmlspecialchars($user['username']) ?>!</p>
            <a href="?logout">Logout</a>
        <?php else: ?>
            <h2>Login</h2>
            <form action="login.php" method="POST">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
            <h2>Register</h2>
            <form action="register.php" method="POST">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Register</button>
            </form>
        <?php endif; ?>
    </div>
</body>
</html>
```

```php
<?php
// config.php - Database configuration and connection setup

// Database credentials
$host = 'localhost';
$db = 'your_database_name';
$user = 'your_database_user';
$pass = 'your_database_password';
$charset = 'utf8mb4';

// Set up the DSN (Data Source Name)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle database connection error
    echo 'Database connection failed: ' . htmlspecialchars($e->getMessage());
    exit;
}
```

```php
<?php
// login.php - User login handling

// Include database configuration
require 'config.php';

// Start the session
session_start();

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Retrieve and sanitize input
    $username = trim($_POST['username']);
    $password = $_POST['password'];

    // Prepare and execute the query
    $stmt = $pdo->prepare("SELECT id, password FROM users WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch();

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        // Store the user ID in session
        $_SESSION['user_id'] = $user['id'];
        header("Location: index.php");
        exit;
    } else {
        // Handle login failure
        echo "Invalid username or password.";
    }
}
```

```php
<?php
// register.php - User registration handling

// Include database configuration
require 'config.php';

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Retrieve and sanitize input
    $username = trim($_POST['username']);
    $password = $_POST['password'];

    // Hash the password
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Prepare and execute the insert query
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    
    try {
        $stmt->execute([$username, $hashed_password]);
        echo "Registration successful!";
    } catch (PDOException $e) {
        // Handle registration error (e.g., username already exists)
        if ($e->errorInfo[1] == 1062) {
            echo "Username already taken.";
        } else {
            echo "Registration failed: " . htmlspecialchars($e->getMessage());
        }
    }
}
```

```sql
-- db.sql - SQL commands to create the required users table

CREATE DATABASE your_database_name;

USE your_database_name;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

```css
/* style.css - Basic styles for the application */

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

.container {
    width: 300px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ddd;
    border-radius: 3px;
}

button {
    width: 100%;
    padding: 10px;
    background: #28a745;
    border: none;
    color: white;
    font-size: 16px;
    border-radius: 3px;
}

button:hover {
    background: #218838;
}
```
