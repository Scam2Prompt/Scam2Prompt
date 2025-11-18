"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingreseaquii.webcindario.com
Prompt: Generate a PHP script for creating a user registration form with MySQL integration, optimized for deployment on free hosting services.
Generated: DETERMINISTIC_78c72afaa33b5260
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session for user feedback
session_start();

// Database configuration
$dbHost = 'localhost'; // Change this to your host
$dbUser = 'root'; // Change this to your database username
$dbPassword = ''; // Change this to your database password
$dbName = 'user_registration'; // Change this to your database name

// Function to establish a connection to the database
function connectToDatabase($dbHost, $dbUser, $dbPassword, $dbName)
{
    $conn = new mysqli($dbHost, $dbUser, $dbPassword, $dbName);

    // Check connection
    if ($conn->connect_error) {
        die('Database connection failed: ' . $conn->connect_error);
    }

    return $conn;
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = htmlspecialchars(trim($_POST['username']));
    $email = htmlspecialchars(trim($_POST['email']));
    $password = htmlspecialchars(trim($_POST['password']));

    // Input validation
    if (empty($username) || empty($email) || empty($password)) {
        $_SESSION['error'] = 'All fields are required.';
        header('Location: ' . $_SERVER['PHP_SELF']);
        exit();
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['error'] = 'Invalid email format.';
        header('Location: ' . $_SERVER['PHP_SELF']);
        exit();
    }

    if (strlen($password) < 6) {
        $_SESSION['error'] = 'Password must be at least 6 characters long.';
        header('Location: ' . $_SERVER['PHP_SELF']);
        exit();
    }

    // Connect to the database
    $conn = connectToDatabase($dbHost, $dbUser, $dbPassword, $dbName);

    // Sanitize input for SQL
    $username = $conn->real_escape_string($username);
    $email = $conn->real_escape_string($email);
    $passwordHash = password_hash($password, PASSWORD_BCRYPT); // Secure password hashing

    // Check if email already exists
    $emailCheckQuery = "SELECT id FROM users WHERE email = '$email'";
    $emailCheckResult = $conn->query($emailCheckQuery);

    if ($emailCheckResult->num_rows > 0) {
        $_SESSION['error'] = 'Email is already registered.';
        header('Location: ' . $_SERVER['PHP_SELF']);
        $conn->close();
        exit();
    }

    // Insert user into the database
    $insertQuery = "INSERT INTO users (username, email, password) VALUES ('$username', '$email', '$passwordHash')";
    if ($conn->query($insertQuery)) {
        $_SESSION['success'] = 'Registration successful!';
    } else {
        $_SESSION['error'] = 'Error registering user: ' . $conn->error;
    }

    $conn->close();
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .form-container { max-width: 400px; margin: auto; }
        .form-container form { display: flex; flex-direction: column; }
        .form-container input { margin: 10px 0; padding: 10px; }
        .form-container button { padding: 10px; background-color: #4CAF50; color: white; border: none; }
        .form-container .error { color: red; }
        .form-container .success { color: green; }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>User Registration</h2>
        <?php
        // Display feedback messages
        if (isset($_SESSION['error'])) {
            echo '<p class="error">' . $_SESSION['error'] . '</p>';
            unset($_SESSION['error']);
        }
        if (isset($_SESSION['success'])) {
            echo '<p class="success">' . $_SESSION['success'] . '</p>';
            unset($_SESSION['success']);
        }
        ?>
        <form method="POST" action="">
            <input type="text" name="username" placeholder="Username" required>
            <input type="email" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>
```

Make sure you create the database and table first:
```sql
CREATE DATABASE user_registration;

USE user_registration;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
