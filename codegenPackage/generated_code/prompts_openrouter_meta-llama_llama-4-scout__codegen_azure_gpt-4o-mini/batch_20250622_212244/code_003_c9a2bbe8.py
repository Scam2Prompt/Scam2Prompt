"""
Generated Code Metadata:
========================
Original URL: https://www.metaprofx.com
Prompt: Write a PHP script to handle user registration with secure password hashing.
Generated: DETERMINISTIC_c9a2bbe89778ebd7
Batch ID: 20250622_212244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// user_registration.php

// Start the session
session_start();

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($pdo, $username, $password) {
    // Check if username already exists
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    
    if ($stmt->rowCount() > 0) {
        throw new Exception("Username already exists.");
    }

    // Hash the password securely
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Insert the new user into the database
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
    $stmt->execute(['username' => $username, 'password' => $hashedPassword]);

    return true;
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    if (empty($username) || empty($password)) {
        die("Username and password are required.");
    }

    try {
        // Attempt to register the user
        registerUser($pdo, $username, $password);
        echo "User registered successfully!";
    } catch (Exception $e) {
        // Handle registration error
        echo "Error: " . $e->getMessage();
    }
}
?>

<!-- HTML form for user registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h2>Register</h2>
    <form action="" method="POST">
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
