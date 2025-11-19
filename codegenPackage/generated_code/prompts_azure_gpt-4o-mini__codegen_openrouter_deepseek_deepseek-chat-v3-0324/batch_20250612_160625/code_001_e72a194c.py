"""
Generated Code Metadata:
========================
Original URL: https://appvirtuals.webcindario.com
Prompt: What are the steps to set up a website with PHP and MySQL for free, according to the information on appvirtuals.webcindario.com?
Generated: DETERMINISTIC_e72a194cfe79a4a9
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'username');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'database_name');

// Attempt to connect to MySQL database
try {
    $pdo = new PDO("mysql:host=" . DB_SERVER . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

// Create tables if they don't exist
try {
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";
    
    $pdo->exec($sql);
} catch(PDOException $e) {
    die("ERROR: Could not create table. " . $e->getMessage());
}

// Simple user registration function
function registerUser($username, $password, $pdo) {
    try {
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);
        
        $sql = "INSERT INTO users (username, password) VALUES (:username, :password)";
        $stmt = $pdo->prepare($sql);
        
        $stmt->bindParam(':username', $username, PDO::PARAM_STR);
        $stmt->bindParam(':password', $hashed_password, PDO::PARAM_STR);
        
        $stmt->execute();
        return true;
    } catch(PDOException $e) {
        return false;
    }
}

// Simple user login function
function loginUser($username, $password, $pdo) {
    try {
        $sql = "SELECT id, username, password FROM users WHERE username = :username";
        $stmt = $pdo->prepare($sql);
        
        $stmt->bindParam(':username', $username, PDO::PARAM_STR);
        $stmt->execute();
        
        if($stmt->rowCount() == 1) {
            $row = $stmt->fetch();
            if(password_verify($password, $row['password'])) {
                return true;
            }
        }
        return false;
    } catch(PDOException $e) {
        return false;
    }
}

// Basic HTML template
function renderPage($title, $content) {
    echo <<<HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        .form-group { margin-bottom: 15px; }
        input[type="text"], input[type="password"] { padding: 8px; width: 100%; }
        button { padding: 10px 15px; background: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background: #0056b3; }
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <div class="container">
        <h1>$title</h1>
        $content
    </div>
</body>
</html>
HTML;
}

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);
        
        if (registerUser($username, $password, $pdo)) {
            $content = '<p class="success">Registration successful!</p>';
        } else {
            $content = '<p class="error">Registration failed. Username may already exist.</p>';
        }
        renderPage('Registration', $content);
        
    } elseif (isset($_POST['login'])) {
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);
        
        if (loginUser($username, $password, $pdo)) {
            $content = '<p class="success">Login successful!</p>';
        } else {
            $content = '<p class="error">Login failed. Invalid credentials.</p>';
        }
        renderPage('Login', $content);
    }
} else {
    // Show registration form by default
    $content = <<<HTML
    <form method="post">
        <h2>Register</h2>
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" name="username" required>
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" name="password" required>
        </div>
        <button type="submit" name="register">Register</button>
    </form>
    
    <hr>
    
    <form method="post">
        <h2>Login</h2>
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" name="username" required>
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" name="password" required>
        </div>
        <button type="submit" name="login">Login</button>
    </form>
HTML;
    
    renderPage('Welcome', $content);
}
?>
```
