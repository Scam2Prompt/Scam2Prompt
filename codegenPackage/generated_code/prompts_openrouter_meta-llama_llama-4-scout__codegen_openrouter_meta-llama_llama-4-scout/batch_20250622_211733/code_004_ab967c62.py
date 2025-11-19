"""
Generated Code Metadata:
========================
Original URL: https://tante4dx43.com
Prompt: "Create a simple PHP script to handle user registration and login functionality for a website like TANTE4D, including validation and secure password storage."
Generated: DETERMINISTIC_ab967c62c7d167ca
Batch ID: 20250622_211733
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
    'dbHost' => 'localhost',
    'dbUsername' => 'root',
    'dbPassword' => '',
    'dbName' => 'tante4d',
    'salt' => 'tante4d_salt',
];

// Database Connection
function connectDB($config) {
    try {
        $conn = new PDO("mysql:host={$config['dbHost']};dbname={$config['dbName']}", $config['dbUsername'], $config['dbPassword']);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $conn;
    } catch (PDOException $e) {
        die("ERROR: Could not connect. " . $e->getMessage());
    }
}

// Validate Input
function validateInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Register User
function registerUser($conn, $username, $email, $password) {
    $username = validateInput($username);
    $email = validateInput($email);
    $password = validateInput($password);

    $query = $conn->prepare("SELECT * FROM users WHERE username=:username OR email=:email");
    $query->bindParam(':username', $username);
    $query->bindParam(':email', $email);
    $query->execute();

    if ($query->rowCount() > 0) {
        throw new Exception("Username or email already exists.");
    }

    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $query = $conn->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
    $query->bindParam(':username', $username);
    $query->bindParam(':email', $email);
    $query->bindParam(':password', $hashedPassword);
    $query->execute();
}

// Login User
function loginUser($conn, $username, $password) {
    $username = validateInput($username);
    $password = validateInput($password);

    $query = $conn->prepare("SELECT * FROM users WHERE username=:username");
    $query->bindParam(':username', $username);
    $query->execute();

    if ($query->rowCount() < 1) {
        throw new Exception("Invalid username or password.");
    }

    $user = $query->fetch();
    if (!password_verify($password, $user['password'])) {
        throw new Exception("Invalid username or password.");
    }

    return $user;
}

// Main Script
try {
    $conn = connectDB($config);

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (isset($_POST['register'])) {
            $username = $_POST['username'];
            $email = $_POST['email'];
            $password = $_POST['password'];
            registerUser($conn, $username, $email, $password);
            echo "Registration successful!";
        } elseif (isset($_POST['login'])) {
            $username = $_POST['username'];
            $password = $_POST['password'];
            $user = loginUser($conn, $username, $password);
            echo "Login successful! Welcome, " . $user['username'];
        }
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}

// Close Database Connection
$conn = null;

?>

<!-- HTML Form -->
<form action="" method="post">
    <h2>Register</h2>
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" name="register" value="Register">
</form>

<form action="" method="post">
    <h2>Login</h2>
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" name="login" value="Login">
</form>
```
