"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstonetrading.biz
Prompt: Write PHP code for a login and registration system that mimics the "DUGEMSLOT LOGIN" and "DUGEMSLOT DAFTAR" functionalities.
Generated: DETERMINISTIC_84970239591aaa33
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Database Configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'dugemslot');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Establish a Database Connection
function getDbConnection() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// User Registration
function registerUser($username, $password) {
    try {
        $db = getDbConnection();

        // Check if username already exists
        $stmt = $db->prepare("SELECT id FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        if ($stmt->fetch()) {
            return "Username already exists.";
        }

        // Hash the password before storing it
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Insert new user into the database
        $stmt = $db->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        $stmt->execute(['username' => $username, 'password' => $hashedPassword]);

        return "Registration successful.";
    } catch (Exception $e) {
        return "Error during registration: " . $e->getMessage();
    }
}

// User Login
function loginUser($username, $password) {
    try {
        $db = getDbConnection();

        // Fetch user details
        $stmt = $db->prepare("SELECT id, password FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$user) {
            return "Invalid username or password.";
        }

        // Verify the password
        if (password_verify($password, $user['password'])) {
            // Simulate user session (in production, use proper session handling)
            session_start();
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $username;

            return "Login successful.";
        } else {
            return "Invalid username or password.";
        }
    } catch (Exception $e) {
        return "Error during login: " . $e->getMessage();
    }
}

// Example Usage (for demonstration purposes only):
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action'])) {
        $action = $_POST['action'];
        $username = $_POST['username'] ?? '';
        $password = $_POST['password'] ?? '';

        if ($action === 'register') {
            echo registerUser($username, $password);
        } elseif ($action === 'login') {
            echo loginUser($username, $password);
        }
    }
}

?>

<!-- HTML Form for Login and Registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DUGEMSLOT Login and Registration</title>
</head>
<body>
    <h1>DUGEMSLOT LOGIN</h1>
    <form method="POST">
        <input type="hidden" name="action" value="login">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Login</button>
    </form>

    <h1>DUGEMSLOT DAFTAR</h1>
    <form method="POST">
        <input type="hidden" name="action" value="register">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```
