"""
Generated Code Metadata:
========================
Original URL: https://pers-daviplata.webcindario.com
Prompt: Create a PHP and MySQL-based website template optimized for free hosting platforms like those discussed on "miarroba.com."
Generated: DETERMINISTIC_26d144ca9f8df311
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema**
```sql
CREATE DATABASE IF NOT EXISTS mirobroba_template;

USE mirobroba_template;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS posts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**config.php**
```php
<?php
/**
 * Configuration file for the website template.
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'mirobroba_template');

// Website settings
define('WEBSITE_TITLE', 'Miarroba Template');
define('WEBSITE_DESCRIPTION', 'A PHP and MySQL-based website template');

// Error reporting settings
error_reporting(E_ALL);
ini_set('display_errors', 1);
```

**db.php**
```php
<?php
/**
 * Database connection class.
 */

class Database {
  private $host;
  private $username;
  private $password;
  private $name;

  public function __construct($host, $username, $password, $name) {
    $this->host = $host;
    $this->username = $username;
    $this->password = $password;
    $this->name = $name;
  }

  public function connect() {
    try {
      $conn = new PDO("mysql:host=$this->host;dbname=$this->name", $this->username, $this->password);
      $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      return $conn;
    } catch (PDOException $e) {
      die("Error: " . $e->getMessage());
    }
  }
}
```

**functions.php**
```php
<?php
/**
 * General functions for the website template.
 */

function get_pages($conn) {
  $stmt = $conn->prepare("SELECT * FROM pages ORDER BY created_at DESC");
  $stmt->execute();
  return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function get_posts($conn) {
  $stmt = $conn->prepare("SELECT * FROM posts ORDER BY created_at DESC");
  $stmt->execute();
  return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function get_user($conn, $id) {
  $stmt = $conn->prepare("SELECT * FROM users WHERE id = :id");
  $stmt->bindParam(':id', $id);
  $stmt->execute();
  return $stmt->fetch(PDO::FETCH_ASSOC);
}

function authenticate_user($conn, $username, $password) {
  $stmt = $conn->prepare("SELECT * FROM users WHERE username = :username AND password = :password");
  $stmt->bindParam(':username', $username);
  $stmt->bindParam(':password', $password);
  $stmt->execute();
  return $stmt->fetch(PDO::FETCH_ASSOC);
}
```

**index.php**
```php
<?php
require_once 'config.php';
require_once 'db.php';
require_once 'functions.php';

$conn = (new Database(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME))->connect();

$pages = get_pages($conn);
$posts = get_posts($conn);

require_once 'header.php';
require_once 'footer.php';
?>

<!-- Homepage content -->
<h1><?= WEBSITE_TITLE ?></h1>
<p><?= WEBSITE_DESCRIPTION ?></p>

<ul>
  <?php foreach ($pages as $page) : ?>
    <li><a href="page.php?id=<?= $page['id'] ?>"><?= $page['title'] ?></a></li>
  <?php endforeach; ?>
</ul>

<ul>
  <?php foreach ($posts as $post) : ?>
    <li><a href="post.php?id=<?= $post['id'] ?>"><?= $post['title'] ?></a></li>
  <?php endforeach; ?>
</ul>
```

**header.php**
```php
<?php
/**
 * Website header.
 */
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><?= WEBSITE_TITLE ?></title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <nav>
      <ul>
        <li><a href="index.php">Home</a></li>
        <li><a href="login.php">Login</a></li>
        <li><a href="register.php">Register</a></li>
      </ul>
    </nav>
  </header>
```

**footer.php**
```php
<?php
/**
 * Website footer.
 */
?>

  <footer>
    <p>&copy; <?= date('Y') ?> <?= WEBSITE_TITLE ?></p>
  </footer>
</body>
</html>
```

**login.php**
```php
<?php
require_once 'config.php';
require_once 'db.php';
require_once 'functions.php';

$conn = (new Database(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME))->connect();

if (isset($_POST['login'])) {
  $username = $_POST['username'];
  $password = $_POST['password'];

  $user = authenticate_user($conn, $username, $password);

  if ($user) {
    // Login successful
    session_start();
    $_SESSION['user_id'] = $user['id'];
    header('Location: index.php');
  } else {
    // Login failed
    $error = 'Invalid username or password';
  }
}

require_once 'header.php';
?>

<!-- Login form -->
<form action="" method="post">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="password">Password:</label>
  <input type="password" id="password" name="password"><br><br>
  <input type="submit" name="login" value="Login">
</form>

<?php if (isset($error)) : ?>
  <p style="color: red"><?= $error ?></p>
<?php endif; ?>

<?php require_once 'footer.php'; ?>
```

**register.php**
```php
<?php
require_once 'config.php';
require_once 'db.php';
require_once 'functions.php';

$conn = (new Database(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME))->connect();

if (isset($_POST['register'])) {
  $username = $_POST['username'];
  $email = $_POST['email'];
  $password = $_POST['password'];

  $stmt = $conn->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
  $stmt->bindParam(':username', $username);
  $stmt->bindParam(':email', $email);
  $stmt->bindParam(':password', $password);
  $stmt->execute();

  // Registration successful
  $success = 'Registration successful';
}

require_once 'header.php';
?>

<!-- Registration form -->
<form action="" method="post">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="email">Email:</label>
  <input type="email" id="email" name="email"><br><br>
  <label for="password">Password:</label>
  <input type="password" id="password" name="password"><br><br>
  <input type="submit" name="register" value="Register">
</form>

<?php if (isset($success)) : ?>
  <p style="color: green"><?= $success ?></p>
<?php endif; ?>

<?php require_once 'footer.php'; ?>
```
