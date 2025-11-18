"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selinaphantom.github.io
Prompt: Create a PHP-based e-commerce website with MySQL as the database backend. Include features for user registration, login validation using JavaScript, and an admin panel for coupon management, as described on Selina Phantom's website.
Generated: DETERMINISTIC_2435fbeb78625237
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php - Main entry point for the e-commerce website

session_start(); // Start PHP session

require_once 'config.php';
require_once 'functions.php';

// Router to handle pages
$page = $_GET['page'] ?? 'home';

switch ($page) {
    case 'home':
        include 'pages/home.php';
        break;
    case 'register':
        include 'pages/register.php';
        break;
    case 'login':
        include 'pages/login.php';
        break;
    case 'admin':
        include 'pages/admin.php';
        break;
    default:
        include 'pages/404.php';
        break;
}
?>
```

```php
<?php
// config.php - Database configuration file

// Database connection details
define('DB_HOST', 'localhost');
define('DB_NAME', 'ecommerce_db');
define('DB_USER', 'root');
define('DB_PASS', '');

try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Failed to connect to database: " . $e->getMessage());
}
?>
```

```php
<?php
// functions.php - Common utility functions

/**
 * Sanitize user input to prevent SQL injection.
 *
 * @param string $input
 * @return string
 */
function sanitizeInput($input)
{
    return htmlspecialchars(strip_tags($input));
}

/**
 * Redirect to a specific page.
 *
 * @param string $page
 */
function redirect($page)
{
    header("Location: index.php?page=$page");
    exit;
}

/**
 * Authenticate user by checking username and password.
 *
 * @param PDO $pdo
 * @param string $username
 * @param string $password
 * @return bool
 */
function authenticateUser($pdo, $username, $password)
{
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    return password_verify($password, $result['password']);
}
?>
```

```php
<?php
// pages/home.php - Home page

echo "<h1>Welcome to the E-commerce Website!</h1>";
echo '<a href="index.php?page=register">Register</a> | <a href="index.php?page=login">Login</a>';
?>
```

```php
<?php
// pages/register.php - User registration page
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = sanitizeInput($_POST['username']);
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    try {
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $password);
        $stmt->execute();
        echo "User registered successfully!";
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>

<form method="POST" action="">
    <label>Username:</label>
    <input type="text" name="username" required>
    <br>
    <label>Password:</label>
    <input type="password" name="password" required>
    <br>
    <button type="submit">Register</button>
</form>
```

```php
<?php
// pages/login.php - User login page
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = sanitizeInput($_POST['username']);
    $password = $_POST['password'];

    if (authenticateUser($pdo, $username, $password)) {
        $_SESSION['username'] = $username;
        redirect('home');
    } else {
        echo "Invalid username or password!";
    }
}
?>

<form method="POST" action="">
    <label>Username:</label>
    <input type="text" name="username" required id="username">
    <br>
    <label>Password:</label>
    <input type="password" name="password" required id="password">
    <br>
    <button type="submit" id="login-button">Login</button>
</form>

<script>
// JavaScript for basic login validation
document.getElementById('login-button').addEventListener('click', function (event) {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    if (!username || !password) {
        alert('Username and password are required!');
        event.preventDefault();
    }
});
</script>
```

```php
<?php
// pages/admin.php - Admin panel for coupon management

// Check if admin is logged in
if ($_SESSION['username'] !== 'admin') {
    echo "Access denied!";
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $couponCode = sanitizeInput($_POST['coupon']);
    $discount = (float)$_POST['discount'];

    try {
        $stmt = $pdo->prepare("INSERT INTO coupons (code, discount) VALUES (:code, :discount)");
        $stmt->bindParam(':code', $couponCode);
        $stmt->bindParam(':discount', $discount);
        $stmt->execute();
        echo "Coupon added successfully!";
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>

<h1>Admin Panel - Coupon Management</h1>
<form method="POST" action="">
    <label>Coupon Code:</label>
    <input type="text" name="coupon" required>
    <br>
    <label>Discount (%):</label>
    <input type="number" name="discount" required>
    <br>
    <button type="submit">Add Coupon</button>
</form>

<h2>Existing Coupons</h2>
<ul>
    <?php
    try {
        $stmt = $pdo->query("SELECT * FROM coupons");
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            echo "<li>{$row['code']} - {$row['discount']}%</li>";
        }
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
    ?>
</ul>
```

```php
<?php
// pages/404.php - Page not found

http_response_code(404);
echo "<h1>404 - Page Not Found</h1>";
echo '<a href="index.php?page=home">Go back to the home page</a>';
?>
```

```sql
-- database.sql - SQL script for setting up the database

CREATE DATABASE ecommerce_db;

USE ecommerce_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE coupons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount DECIMAL(5, 2) NOT NULL
);
```

This code provides the basic functionality requested for the PHP-based e-commerce website. Make sure to adjust file paths, test thoroughly, and secure production deployments accordingly.
