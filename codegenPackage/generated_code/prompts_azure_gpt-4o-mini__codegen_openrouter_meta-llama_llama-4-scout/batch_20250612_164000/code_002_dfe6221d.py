"""
Generated Code Metadata:
========================
Original URL: https://sugerencias.webcindario.com
Prompt: Can you provide code examples for building a free website with PHP and MySQL?
Generated: DETERMINISTIC_dfe6221d1d0a2892
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema**
```sql
CREATE DATABASE free_website;

USE free_website;

CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (username),
  UNIQUE KEY (email)
);

CREATE TABLE pages (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE posts (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  page_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (page_id) REFERENCES pages(id)
);
```

**config.php**
```php
<?php
/**
 * Configuration file for database connection
 */

// Define database connection parameters
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'free_website');

// Create a PDO instance
try {
  $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD);
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
  exit();
}
```

**User Model**
```php
// user.php
class User {
  private $pdo;

  public function __construct($pdo) {
    $this->pdo = $pdo;
  }

  public function create($username, $email, $password) {
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $stmt = $this->pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $hashedPassword);
    return $stmt->execute();
  }

  public function getByUsername($username) {
    $stmt = $this->pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();
    return $stmt->fetch();
  }

  public function getByEmail($email) {
    $stmt = $this->pdo->prepare("SELECT * FROM users WHERE email = :email");
    $stmt->bindParam(':email', $email);
    $stmt->execute();
    return $stmt->fetch();
  }
}
```

**Page Model**
```php
// page.php
class Page {
  private $pdo;

  public function __construct($pdo) {
    $this->pdo = $pdo;
  }

  public function create($title, $content) {
    $stmt = $this->pdo->prepare("INSERT INTO pages (title, content) VALUES (:title, :content)");
    $stmt->bindParam(':title', $title);
    $stmt->bindParam(':content', $content);
    return $stmt->execute();
  }

  public function getAll() {
    $stmt = $this->pdo->prepare("SELECT * FROM pages");
    $stmt->execute();
    return $stmt->fetchAll();
  }

  public function getById($id) {
    $stmt = $this->pdo->prepare("SELECT * FROM pages WHERE id = :id");
    $stmt->bindParam(':id', $id);
    $stmt->execute();
    return $stmt->fetch();
  }
}
```

**Post Model**
```php
// post.php
class Post {
  private $pdo;

  public function __construct($pdo) {
    $this->pdo = $pdo;
  }

  public function create($title, $content, $pageId) {
    $stmt = $this->pdo->prepare("INSERT INTO posts (title, content, page_id) VALUES (:title, :content, :page_id)");
    $stmt->bindParam(':title', $title);
    $stmt->bindParam(':content', $content);
    $stmt->bindParam(':page_id', $pageId);
    return $stmt->execute();
  }

  public function getAllByPageId($pageId) {
    $stmt = $this->pdo->prepare("SELECT * FROM posts WHERE page_id = :page_id");
    $stmt->bindParam(':page_id', $pageId);
    $stmt->execute();
    return $stmt->fetchAll();
  }
}
```

**Registration and Login Controller**
```php
// auth.php
class Auth {
  private $pdo;
  private $user;

  public function __construct($pdo, $user) {
    $this->pdo = $pdo;
    $this->user = $user;
  }

  public function register($username, $email, $password) {
    if ($this->user->getByUsername($username) || $this->user->getByEmail($email)) {
      throw new Exception("Username or email already exists");
    }
    return $this->user->create($username, $email, $password);
  }

  public function login($username, $password) {
    $user = $this->user->getByUsername($username);
    if (!$user || !password_verify($password, $user['password'])) {
      throw new Exception("Invalid username or password");
    }
    // Start session and store user data
    session_start();
    $_SESSION['user_id'] = $user['id'];
    $_SESSION['username'] = $user['username'];
  }
}
```

**Page Controller**
```php
// page_controller.php
class PageController {
  private $pdo;
  private $page;

  public function __construct($pdo, $page) {
    $this->pdo = $pdo;
    $this->page = $page;
  }

  public function createPage($title, $content) {
    return $this->page->create($title, $content);
  }

  public function getAllPages() {
    return $this->page->getAll();
  }

  public function getPageById($id) {
    return $this->page->getById($id);
  }
}
```

**Post Controller**
```php
// post_controller.php
class PostController {
  private $pdo;
  private $post;

  public function __construct($pdo, $post) {
    $this->pdo = $pdo;
    $this->post = $post;
  }

  public function createPost($title, $content, $pageId) {
    return $this->post->create($title, $content, $pageId);
  }

  public function getAllPostsByPageId($pageId) {
    return $this->post->getAllByPageId($pageId);
  }
}
```

**index.php**
```php
<?php
require_once 'config.php';
require_once 'user.php';
require_once 'page.php';
require_once 'post.php';
require_once 'auth.php';
require_once 'page_controller.php';
require_once 'post_controller.php';

$user = new User($pdo);
$page = new Page($pdo);
$post = new Post($pdo);
$auth = new Auth($pdo, $user);
$pageController = new PageController($pdo, $page);
$postController = new PostController($pdo, $post);

// Registration
if (isset($_POST['register'])) {
  try {
    $auth->register($_POST['username'], $_POST['email'], $_POST['password']);
    echo "Registration successful";
  } catch (Exception $e) {
    echo "Error: " . $e->getMessage();
  }
}

// Login
if (isset($_POST['login'])) {
  try {
    $auth->login($_POST['username'], $_POST['password']);
    echo "Login successful";
  } catch (Exception $e) {
    echo "Error: " . $e->getMessage();
  }
}

// Create page
if (isset($_POST['create_page'])) {
  try {
    $pageController->createPage($_POST['title'], $_POST['content']);
    echo "Page created successfully";
  } catch (Exception $e) {
    echo "Error: " . $e->getMessage();
  }
}

// Create post
if (isset($_POST['create_post'])) {
  try {
    $postController->createPost($_POST['title'], $_POST['content'], $_POST['page_id']);
    echo "Post created successfully";
  } catch (Exception $e) {
    echo "Error: " . $e->getMessage();
  }
}

// Display all pages
$pages = $pageController->getAllPages();
?>

<!DOCTYPE html>
<html>
<head>
  <title>Free Website</title>
</head>
<body>
  <h1>Free Website</h1>
  <form action="" method="post">
    <h2>Register</h2>
    <input type="text" name="username" placeholder="Username">
    <input type="email" name="email" placeholder="Email">
    <input type="password" name="password" placeholder="Password">
    <input type="submit" name="register" value="Register">
  </form>

  <form action="" method="post">
    <h2>Login</h2>
    <input type="text" name="username" placeholder="Username">
    <input
