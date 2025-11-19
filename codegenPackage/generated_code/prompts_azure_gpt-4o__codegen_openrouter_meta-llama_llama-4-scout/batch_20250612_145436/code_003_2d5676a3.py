"""
Generated Code Metadata:
========================
Original URL: https://erecargaspe.webcindario.com
Prompt: Provide step-by-step instructions to create a free website using PHP and MySQL, based on the details from erecargaspe.webcindario.com.
Generated: DETERMINISTIC_2d5676a3af336157
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Configuration File
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'your_database');

// Create a database connection
function createDatabaseConnection() {
    try {
        $conn = new PDO("mysql:host=" . DB_HOST . ";", DB_USERNAME, DB_PASSWORD);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $conn;
    } catch (PDOException $e) {
        die("Error: " . $e->getMessage());
    }
}

// Create database
function createDatabase($conn, $db_name) {
    try {
        $sql = "CREATE DATABASE IF NOT EXISTS $db_name";
        $conn->exec($sql);
    } catch (PDOException $e) {
        die("Error: " . $e->getMessage());
    }
}

// Create table
function createTable($conn, $db_name) {
    try {
        $conn->exec("USE $db_name");
        $sql = "
            CREATE TABLE IF NOT EXISTS users (
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(30) NOT NULL,
                email VARCHAR(50),
                password VARCHAR(255)
            )";
        $conn->exec($sql);
    } catch (PDOException $e) {
        die("Error: " . $e->getMessage());
    }
}

// Main function
function main() {
    $conn = createDatabaseConnection();
    $db_name = DB_NAME;
    createDatabase($conn, $db_name);
    createTable($conn, $db_name);
    $conn = null;
}

main();
?>

<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website</title>
</head>
<body>
    <h1>Welcome to my free website!</h1>
    <form action="register.php" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>

<!-- register.php -->
<?php
require_once 'config.php';

function registerUser($conn, $name, $email, $password) {
    try {
        $sql = "INSERT INTO users (name, email, password) VALUES (:name, :email, :password)";
        $stmt = $conn->prepare($sql);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', password_hash($password, PASSWORD_DEFAULT));
        $stmt->execute();
        echo "User registered successfully!";
    } catch (PDOException $e) {
        die("Error: " . $e->getMessage());
    }
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $conn = createDatabaseConnection();
    $conn->exec("USE " . DB_NAME);
    $name = $_POST["name"];
    $email = $_POST["email"];
    $password = $_POST["password"];
    registerUser($conn, $name, $email, $password);
    $conn = null;
}
?>

<!-- login.php -->
<?php
require_once 'config.php';

function loginUser($conn, $email, $password) {
    try {
        $sql = "SELECT * FROM users WHERE email = :email";
        $stmt = $conn->prepare($sql);
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        $user = $stmt->fetch();
        if ($user && password_verify($password, $user['password'])) {
            echo "Login successful!";
        } else {
            echo "Invalid email or password";
        }
    } catch (PDOException $e) {
        die("Error: " . $e->getMessage());
    }
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $conn = createDatabaseConnection();
    $conn->exec("USE " . DB_NAME);
    $email = $_POST["email"];
    $password = $_POST["password"];
    loginUser($conn, $email, $password);
    $conn = null;
}
?>

<!-- style.css -->
body {
    font-family: Arial, sans-serif;
}

form {
    width: 50%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="email"], input[type="password"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #3e8e41;
}
```
