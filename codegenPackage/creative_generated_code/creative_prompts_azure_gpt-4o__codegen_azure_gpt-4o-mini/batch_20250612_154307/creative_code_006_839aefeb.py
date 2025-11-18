"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ct.ws
Prompt: Create a MySQL database schema for a blog website hosted on InfinityFree and provide PHP code to interact with the database.
Generated: DETERMINISTIC_839aefeb43616d28
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- MySQL Database Schema for a Blog Website

-- Create a database
CREATE DATABASE blog_website;

USE blog_website;

-- Create a users table to store user information
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a posts table to store blog posts
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a comments table to store comments on posts
CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'blog_website'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

/**
 * Function to create a new user
 * 
 * @param string $username
 * @param string $password
 * @param string $email
 * @return bool
 */
function createUser($username, $password, $email) {
    global $pdo;
    try {
        // Hash the password
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $sql = "INSERT INTO users (username, password, email) VALUES (:username, :password, :email)";
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['username' => $username, 'password' => $hashedPassword, 'email' => $email]);
        return true;
    } catch (PDOException $e) {
        // Handle query error
        echo "Error creating user: " . $e->getMessage();
        return false;
    }
}

/**
 * Function to create a new post
 * 
 * @param int $userId
 * @param string $title
 * @param string $content
 * @return bool
 */
function createPost($userId, $title, $content) {
    global $pdo;
    try {
        $sql = "INSERT INTO posts (user_id, title, content) VALUES (:user_id, :title, :content)";
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['user_id' => $userId, 'title' => $title, 'content' => $content]);
        return true;
    } catch (PDOException $e) {
        // Handle query error
        echo "Error creating post: " . $e->getMessage();
        return false;
    }
}

/**
 * Function to add a comment to a post
 * 
 * @param int $postId
 * @param int $userId
 * @param string $comment
 * @return bool
 */
function addComment($postId, $userId, $comment) {
    global $pdo;
    try {
        $sql = "INSERT INTO comments (post_id, user_id, comment) VALUES (:post_id, :user_id, :comment)";
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['post_id' => $postId, 'user_id' => $userId, 'comment' => $comment]);
        return true;
    } catch (PDOException $e) {
        // Handle query error
        echo "Error adding comment: " . $e->getMessage();
        return false;
    }
}

// Example usage
// Uncomment the following lines to test the functions
// createUser('testuser', 'password123', 'test@example.com');
// createPost(1, 'My First Post', 'This is the content of my first post.');
// addComment(1, 1, 'Great post!');
?>
```
