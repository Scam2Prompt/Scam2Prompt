"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Develop a PHP application that provides a community support system for users to share insights and celebrate wins, similar to the features of the Action Accelerator Academy.
Generated: DETERMINISTIC_ef269e6df1f05b08
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Community Support System Application

// Start session for user management
session_start();

// Database connection configuration
$host = 'localhost';
$db = 'community_support';
$user = 'root';
$password = 'password'; // Change to your database password

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to add a new post
function addPost($userId, $content) {
    global $pdo;
    $sql = "INSERT INTO posts (user_id, content, created_at) VALUES (:user_id, :content, NOW())";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['user_id' => $userId, 'content' => $content]);
}

// Function to get all posts
function getPosts() {
    global $pdo;
    $sql = "SELECT posts.id, posts.content, posts.created_at, users.username 
            FROM posts 
            JOIN users ON posts.user_id = users.id 
            ORDER BY posts.created_at DESC";
    $stmt = $pdo->query($sql);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Function to register a new user
function registerUser($username, $password) {
    global $pdo;
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $sql = "INSERT INTO users (username, password) VALUES (:username, :password)";
    
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['username' => $username, 'password' => $hashedPassword]);
}

// Function to authenticate user
function loginUser($username, $password) {
    global $pdo;
    $sql = "SELECT * FROM users WHERE username = :username";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    
    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        return true;
    }
    return false;
}

// Function to logout user
function logoutUser() {
    session_destroy();
}

// Check for form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Register user
        registerUser($_POST['username'], $_POST['password']);
    } elseif (isset($_POST['login'])) {
        // Login user
        if (loginUser($_POST['username'], $_POST['password'])) {
            header("Location: index.php");
            exit();
        } else {
            $error = "Invalid username or password.";
        }
    } elseif (isset($_POST['post'])) {
        // Add new post
        addPost($_SESSION['user_id'], $_POST['content']);
    } elseif (isset($_POST['logout'])) {
        // Logout user
        logoutUser();
        header("Location: index.php");
        exit();
    }
}

// Get all posts for display
$posts = getPosts();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Community Support System</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>Community Support System</h1>

    <?php if (!isset($_SESSION['user_id'])): ?>
        <h2>Login or Register</h2>
        <form method="POST">
            <input type="text" name="username" required placeholder="Username">
            <input type="password" name="password" required placeholder="Password">
            <button type="submit" name="login">Login</button>
            <button type="submit" name="register">Register</button>
        </form>
        <?php if (isset($error)) echo "<p>$error</p>"; ?>
    <?php else: ?>
        <h2>Welcome, <?= htmlspecialchars($_SESSION['username']) ?></h2>
        <form method="POST">
            <textarea name="content" required placeholder="Share your insights or celebrate a win..."></textarea>
            <button type="submit" name="post">Post</button>
            <button type="submit" name="logout">Logout</button>
        </form>
    <?php endif; ?>

    <h2>Community Posts</h2>
    <ul>
        <?php foreach ($posts as $post): ?>
            <li>
                <strong><?= htmlspecialchars($post['username']) ?>:</strong>
                <p><?= htmlspecialchars($post['content']) ?></p>
                <small><?= htmlspecialchars($post['created_at']) ?></small>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

```sql
-- SQL to create the necessary tables
CREATE DATABASE community_support;

USE community_support;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

Make sure to create a 'styles.css' file for styling and adjust the database credentials as needed.
