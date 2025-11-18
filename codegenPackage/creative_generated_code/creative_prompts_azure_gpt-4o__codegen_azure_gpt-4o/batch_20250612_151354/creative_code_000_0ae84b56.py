"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingreseeaquii.webcindario.com
Prompt: Write PHP code to create a simple website with MySQL integration, including user authentication and a custom domain setup.
Generated: DETERMINISTIC_0ae84b56bbe0f086
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php
// Database configuration file for MySQL connection

define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'your_database_name'); // Replace with your database name
define('DB_USER', 'your_database_user'); // Replace with your database user
define('DB_PASS', 'your_database_password'); // Replace with your database password

try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
?>
```

```php
<?php
// register.php
// Handles user registration

require 'config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Fetch input fields
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT); // Hash the password

    // Check for empty fields
    if (empty($username) || empty($password)) {
        die("All fields are required.");
    }

    try {
        // Insert user into database
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        $stmt->execute(['username' => $username, 'password' => $hashedPassword]);
        echo "Registration successful!";
    } catch (PDOException $e) {
        if ($e->getCode() === '23000') { // Handle duplicate username error
            die("Username already exists.");
        }
        die("Error: " . $e->getMessage());
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form action="register.php" method="POST">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

```php
<?php
// login.php
// Handles user authentication

require 'config.php';

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Fetch input fields
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Check for empty fields
    if (empty($username) || empty($password)) {
        die("All fields are required.");
    }

    try {
        // Fetch user from database
        $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            // Successful login
            $_SESSION['username'] = $user['username'];
            echo "Login successful!";
            header("Location: welcome.php");
            exit;
        } else {
            die("Invalid username or password.");
        }
    } catch (PDOException $e) {
        die("Error: " . $e->getMessage());
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="login.php" method="POST">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

```php
<?php
// welcome.php
// Displays a welcome page for authenticated users

session_start();

// Check if the user is logged in
if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit;
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome, <?php echo htmlspecialchars($_SESSION['username']); ?>!</h1>
    <a href="logout.php">Logout</a>
</body>
</html>
```

```php
<?php
// logout.php
// Logs out the user

session_start();
session_destroy(); // Destroy session data
header("Location: login.php"); // Redirect to the login page
exit;
?>
```

```sql
-- MySQL setup script
-- Run this script to create the database and table

CREATE DATABASE your_database_name;

USE your_database_name;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Notes for Custom Domain Setup:
To use a custom domain, update your web server (e.g., Apache or Nginx) configuration files, pointing the domain to the directory containing the PHP files above. Configure DNS records of your domain to resolve to your server's IP address.
