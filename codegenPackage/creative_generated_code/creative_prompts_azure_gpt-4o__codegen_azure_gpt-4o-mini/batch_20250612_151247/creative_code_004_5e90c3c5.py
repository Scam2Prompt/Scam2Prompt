"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seguritydecuenta.webcindario.com
Prompt: Write a PHP script to handle user registration and login functionality for a website hosted on a free platform with MySQL support.
Generated: DETERMINISTIC_5e90c3c573093e8e
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php
// This file contains the database connection settings and functions

// Database configuration
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_DATABASE', 'your_database');

function getDB() {
    $conn = null;
    try {
        $conn = new PDO("mysql:host=".DB_SERVER.";dbname=".DB_DATABASE, DB_USERNAME, DB_PASSWORD);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
        // Log error and display a friendly message
        error_log($e->getMessage());
        die("Database connection error. Please try again later.");
    }
    return $conn;
}
?>

<?php
// register.php
// This file handles user registration

require 'database.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if form data is submitted
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);
    
    if (empty($username) || empty($password)) {
        die("Username and password cannot be empty.");
    }

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Insert user into the database
    $conn = getDB();
    try {
        $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);
        $stmt->execute();
        
        echo "Registration successful. You can now log in.";
    } catch (PDOException $e) {
        // Log error and notify user
        error_log($e->getMessage());
        die("Error occurred during registration. Please try again.");
    }
}
?>

<?php
// login.php
// This file handles user login

require 'database.php';

session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if form data is submitted
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);
    
    if (empty($username) || empty($password)) {
        die("Username and password cannot be empty.");
    }

    // Fetch user from the database
    $conn = getDB();
    try {
        $stmt = $conn->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->bindParam(':username', $username);
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Verify password
        if ($user && password_verify($password, $user['password'])) {
            // Set session variables on successful login
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            echo "Login successful. Welcome, " . htmlspecialchars($user['username']) . "!";
        } else {
            echo "Invalid username or password.";
        }
    } catch (PDOException $e) {
        // Log error and notify user
        error_log($e->getMessage());
        die("Error occurred during login. Please try again.");
    }
}
?>

<!-- registration.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h2>User Registration</h2>
    <form action="register.php" method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>

<!-- login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Login</title>
</head>
<body>
    <h2>User Login</h2>
    <form action="login.php" method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

Make sure to replace `your_username`, `your_password`, and `your_database` in `database.php` with actual database credentials.
