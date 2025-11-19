"""
Generated Code Metadata:
========================
Original URL: https://credidavivienta.webcindario.com
Prompt: Write a PHP script to handle user registration and login using MySQL, suitable for a free website hosted on platforms like the one mentioned in the provided content.
Generated: DETERMINISTIC_4ec9a802d8631e8b
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration
$config = [
    'host' => 'localhost',
    'username' => 'your_username',
    'password' => 'your_password',
    'database' => 'your_database',
];

// Create a PDO instance
try {
    $pdo = new PDO(
        'mysql:host=' . $config['host'] . ';dbname=' . $config['database'],
        $config['username'],
        $config['password']
    );
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Connection failed: ' . $e->getMessage());
}

// Register user function
function registerUser($pdo, $username, $email, $password) {
    // Check if user already exists
    $stmt = $pdo->prepare('SELECT * FROM users WHERE username = :username OR email = :email');
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':email', $email);
    $stmt->execute();
    if ($stmt->rowCount() > 0) {
        throw new Exception('User already exists');
    }

    // Hash password
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Insert user into database
    $stmt = $pdo->prepare('INSERT INTO users (username, email, password) VALUES (:username, :email, :password)');
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $hashedPassword);
    $stmt->execute();
}

// Login user function
function loginUser($pdo, $username, $password) {
    // Check if user exists
    $stmt = $pdo->prepare('SELECT * FROM users WHERE username = :username');
    $stmt->bindParam(':username', $username);
    $stmt->execute();
    $user = $stmt->fetch();
    if (!$user) {
        throw new Exception('User not found');
    }

    // Check password
    if (!password_verify($password, $user['password'])) {
        throw new Exception('Invalid password');
    }

    // Return user data
    return $user;
}

// Main script
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        try {
            $username = trim($_POST['username']);
            $email = trim($_POST['email']);
            $password = trim($_POST['password']);
            registerUser($pdo, $username, $email, $password);
            echo 'User registered successfully';
        } catch (Exception $e) {
            echo 'Error: ' . $e->getMessage();
        }
    } elseif (isset($_POST['login'])) {
        try {
            $username = trim($_POST['username']);
            $password = trim($_POST['password']);
            $user = loginUser($pdo, $username, $password);
            echo 'Login successful';
            // You can add session handling here
        } catch (Exception $e) {
            echo 'Error: ' . $e->getMessage();
        }
    }
}

// Close PDO connection
$pdo = null;

?>
```

**users table SQL schema**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Example usage**
```html
<form action="" method="post">
    <h2>Register</h2>
    <input type="text" name="username" required>
    <input type="email" name="email" required>
    <input type="password" name="password" required>
    <input type="submit" name="register" value="Register">
</form>

<form action="" method="post">
    <h2>Login</h2>
    <input type="text" name="username" required>
    <input type="password" name="password" required>
    <input type="submit" name="login" value="Login">
</form>
```
