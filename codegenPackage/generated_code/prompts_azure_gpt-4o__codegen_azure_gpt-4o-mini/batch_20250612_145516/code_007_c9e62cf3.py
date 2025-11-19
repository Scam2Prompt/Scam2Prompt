"""
Generated Code Metadata:
========================
Original URL: https://validardvplta.webcindario.com
Prompt: Generate code for a PHP-based blog system that uses MySQL for content storage and supports custom domains.
Generated: DETERMINISTIC_c9e62cf36a8dda87
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'blog_db');

// Establish a database connection
function dbConnect() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    
    return $connection;
}

// Function to create a new blog post
function createPost($title, $content, $domain) {
    $connection = dbConnect();
    
    // Prepare and bind
    $stmt = $connection->prepare("INSERT INTO posts (title, content, domain) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $title, $content, $domain);
    
    // Execute the statement and check for errors
    if ($stmt->execute()) {
        echo "New post created successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }
    
    // Close the statement and connection
    $stmt->close();
    $connection->close();
}

// Function to retrieve all blog posts
function getPosts() {
    $connection = dbConnect();
    $result = $connection->query("SELECT * FROM posts ORDER BY created_at DESC");
    
    // Check for query errors
    if (!$result) {
        die("Query failed: " . $connection->error);
    }
    
    $posts = [];
    while ($row = $result->fetch_assoc()) {
        $posts[] = $row;
    }
    
    // Close the connection
    $connection->close();
    
    return $posts;
}

// Function to display blog posts
function displayPosts() {
    $posts = getPosts();
    
    foreach ($posts as $post) {
        echo "<h2>" . htmlspecialchars($post['title']) . "</h2>";
        echo "<p>" . nl2br(htmlspecialchars($post['content'])) . "</p>";
        echo "<p><em>Domain: " . htmlspecialchars($post['domain']) . "</em></p>";
        echo "<hr>";
    }
}

// Function to handle form submission for creating a new post
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = $_POST['title'] ?? '';
    $content = $_POST['content'] ?? '';
    $domain = $_POST['domain'] ?? '';
    
    // Basic validation
    if (!empty($title) && !empty($content) && !empty($domain)) {
        createPost($title, $content, $domain);
    } else {
        echo "All fields are required.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Blog System</title>
</head>
<body>
    <h1>My Blog</h1>
    
    <form method="POST" action="">
        <input type="text" name="title" placeholder="Post Title" required>
        <textarea name="content" placeholder="Post Content" required></textarea>
        <input type="text" name="domain" placeholder="Custom Domain" required>
        <button type="submit">Create Post</button>
    </form>
    
    <h2>Blog Posts</h2>
    <?php displayPosts(); ?>
</body>
</html>
```

**Database Schema:**
```sql
CREATE DATABASE blog_db;

USE blog_db;

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    domain VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
