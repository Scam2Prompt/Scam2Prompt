"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivienprotec.webcindario.com
Prompt: Explain how to use PHP and MySQL to create a basic content management system (CMS) for a free website hosted on miarroba.com.
Generated: DETERMINISTIC_2d5e1a3ed3fa6e62
Batch ID: 20250612_154355
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
// This file handles the database connection

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

/**
 * Creates a connection to the MySQL database
 *
 * @return mysqli
 */
function dbConnect() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die('Connection failed: ' . $connection->connect_error);
    }

    return $connection;
}
?>
```

```php
<?php
// index.php
// Main entry point of the CMS

require 'database.php'; // Include the database connection file

// Connect to the database
$connection = dbConnect();

// Fetch all posts from the database
function fetchPosts($connection) {
    $sql = "SELECT * FROM posts ORDER BY created_at DESC";
    $result = $connection->query($sql);

    // Check for query errors
    if (!$result) {
        die('Query failed: ' . $connection->error);
    }
    
    return $result;
}

// Render posts in HTML
function renderPosts($posts) {
    while ($post = $posts->fetch_assoc()) {
        echo "<h2>" . htmlspecialchars($post['title']) . "</h2>";
        echo "<p>" . htmlspecialchars($post['content']) . "</p>";
        echo "<small>Posted on " . htmlspecialchars($post['created_at']) . "</small><hr>";
    }
}

// Fetch and display posts
$posts = fetchPosts($connection);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic CMS</title>
</head>
<body>
    <h1>Welcome to the Basic Content Management System</h1>
    <?php renderPosts($posts); ?>
</body>
</html>
```

```php
<?php
// create_post.php
// This file handles the creation of new posts

require 'database.php'; // Include the database connection file

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $title = trim($_POST['title']);
    $content = trim($_POST['content']);

    if (empty($title) || empty($content)) {
        die('Please fill in all fields');
    }

    // Prepare and bind statement
    $connection = dbConnect();
    $stmt = $connection->prepare("INSERT INTO posts (title, content, created_at) VALUES (?, ?, NOW())");
    $stmt->bind_param("ss", $title, $content);

    // Execute the statement
    if ($stmt->execute()) {
        echo "New post created successfully";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $connection->close();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Post</title>
</head>
<body>
    <h1>Create a New Post</h1>
    <form method="POST" action="create_post.php">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" required><br>
        
        <label for="content">Content:</label><br>
        <textarea id="content" name="content" required></textarea><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```sql
-- setup.sql
-- SQL script to set up the database and posts table

CREATE DATABASE your_database;

USE your_database;

CREATE TABLE posts (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Usage:
1. Create a MySQL database using the `setup.sql` script.
2. Update the database credentials in `database.php`.
3. Place all files on your PHP-enabled web server (like miarroba.com).
4. Access `index.php` to view posts and `create_post.php` to add new posts.
