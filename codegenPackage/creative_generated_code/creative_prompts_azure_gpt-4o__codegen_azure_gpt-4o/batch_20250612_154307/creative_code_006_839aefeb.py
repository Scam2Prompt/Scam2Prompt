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

-- Create the database
CREATE DATABASE IF NOT EXISTS blog_website;

-- Use the database
USE blog_website;

-- Users table to store information about blog authors and readers
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Username for login
    email VARCHAR(100) NOT NULL UNIQUE,     -- User's email address
    password_hash VARCHAR(255) NOT NULL,    -- Securely hashed password
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user is created
);

-- Posts table to store blog posts
CREATE TABLE IF NOT EXISTS posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each post
    user_id INT NOT NULL,                   -- Reference to the author (user_id from users table)
    title VARCHAR(255) NOT NULL,            -- Title of the blog post
    content TEXT NOT NULL,                  -- Content of the blog post
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the post is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the post is last updated
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete if the user is deleted
);

-- Comments table to store comments on blog posts
CREATE TABLE IF NOT EXISTS comments (
    comment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comment
    post_id INT NOT NULL,                      -- Reference to the blog post (post_id from posts table)
    user_id INT NOT NULL,                      -- Reference to the user who made the comment
    content TEXT NOT NULL,                     -- Content of the comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the comment is created
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE, -- Cascade delete if the post is deleted
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Cascade delete if the user is deleted
);
```

```php
<?php
// PHP Code to interact with the MySQL database

// Database connection settings
$servername = "localhost"; // Replace with your InfinityFree server name
$username = "YOUR_USERNAME"; // Replace with your database username
$password = "YOUR_PASSWORD"; // Replace with your database password
$dbname = "blog_website"; // Replace with your database name

try {
    // Create a PDO instance for database connection
    $pdo = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exception handling

    // Example query: Fetch all blog posts
    $stmt = $pdo->query("SELECT posts.post_id, posts.title, posts.content, posts.created_at, users.username 
                        FROM posts 
                        JOIN users ON posts.user_id = users.user_id 
                        ORDER BY posts.created_at DESC");

    // Fetch all posts
    $posts = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Example: Print fetched posts
    foreach ($posts as $post) {
        echo "Post ID: " . htmlspecialchars($post['post_id']) . "<br>";
        echo "Title: " . htmlspecialchars($post['title']) . "<br>";
        echo "Author: " . htmlspecialchars($post['username']) . "<br>";
        echo "Content: " . nl2br(htmlspecialchars($post['content'])) . "<br>";
        echo "Created At: " . htmlspecialchars($post['created_at']) . "<br>";
        echo "<hr>";
    }
} catch (PDOException $e) {
    // Handle database connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function: Insert a new user
function insertUser($pdo, $username, $email, $password) {
    $passwordHash = password_hash($password, PASSWORD_DEFAULT); // Hash the password securely
    $sql = "INSERT INTO users (username, email, password_hash) VALUES (:username, :email, :password_hash)";
    $stmt = $pdo->prepare($sql);
    try {
        $stmt->execute(['username' => $username, 'email' => $email, 'password_hash' => $passwordHash]);
        echo "User created successfully.<br>";
    } catch (PDOException $e) {
        echo "Error creating user: " . $e->getMessage() . "<br>";
    }
}

// Function: Insert a new blog post
function insertPost($pdo, $userId, $title, $content) {
    $sql = "INSERT INTO posts (user_id, title, content) VALUES (:user_id, :title, :content)";
    $stmt = $pdo->prepare($sql);
    try {
        $stmt->execute(['user_id' => $userId, 'title' => $title, 'content' => $content]);
        echo "Post created successfully.<br>";
    } catch (PDOException $e) {
        echo "Error creating post: " . $e->getMessage() . "<br>";
    }
}

// Function: Insert a new comment
function insertComment($pdo, $postId, $userId, $content) {
    $sql = "INSERT INTO comments (post_id, user_id, content) VALUES (:post_id, :user_id, :content)";
    $stmt = $pdo->prepare($sql);
    try {
        $stmt->execute(['post_id' => $postId, 'user_id' => $userId, 'content' => $content]);
        echo "Comment added successfully.<br>";
    } catch (PDOException $e) {
        echo "Error adding comment: " . $e->getMessage() . "<br>";
    }
}
?>
```
