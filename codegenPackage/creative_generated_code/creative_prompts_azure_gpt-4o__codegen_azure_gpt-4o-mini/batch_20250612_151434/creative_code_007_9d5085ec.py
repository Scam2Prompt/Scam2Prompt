"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://security23.webcindario.com
Prompt: Write a tutorial on integrating PHP and MySQL for building a blog, optimized for deployment on free hosting services like miarroba.com.
Generated: DETERMINISTIC_9d5085ec32d3ffa7
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php - Database configuration file

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username'); // Replace with your database username
define('DB_PASS', 'your_password'); // Replace with your database password
define('DB_NAME', 'your_database'); // Replace with your database name

// Create a connection to the database
function dbConnect() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection error
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    
    return $connection;
}
?>
```

```php
<?php
// create_post.php - Create a new blog post

require 'config.php'; // Include the database configuration

// Function to create a new post
function createPost($title, $content) {
    $connection = dbConnect();
    
    // Prepare an SQL statement
    $stmt = $connection->prepare("INSERT INTO posts (title, content) VALUES (?, ?)");
    
    // Bind parameters
    $stmt->bind_param("ss", $title, $content);

    // Execute the statement
    if (!$stmt->execute()) {
        die("Error: " . $stmt->error);
    }

    // Close the statement and connection
    $stmt->close();
    $connection->close();
}

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $title = $_POST['title'];
    $content = $_POST['content'];

    createPost($title, $content);
    header("Location: index.php"); // Redirect to index after creating post
    exit();
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
    <form method="post" action="">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```php
<?php
// index.php - Display all blog posts

require 'config.php'; // Include the database configuration

// Function to fetch all posts
function getPosts() {
    $connection = dbConnect();
    $posts = [];

    // Prepare an SQL statement
    $stmt = $connection->prepare("SELECT id, title, content FROM posts");
    $stmt->execute();
    
    // Store the result
    $result = $stmt->get_result();

    // Fetch all posts into an array
    while ($row = $result->fetch_assoc()) {
        $posts[] = $row;
    }

    // Close the statement and connection
    $stmt->close();
    $connection->close();
    
    return $posts;
}

// Fetch posts
$posts = getPosts();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <a href="create_post.php">Create a New Post</a>
    <ul>
        <?php foreach ($posts as $post): ?>
            <li>
                <h2><?php echo htmlspecialchars($post['title']); ?></h2>
                <p><?php echo nl2br(htmlspecialchars($post['content'])); ?></p>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

```sql
-- install.sql - SQL script to create the database and table

CREATE DATABASE your_database;

USE your_database;

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Important Notes:**
- Replace `your_username`, `your_password`, and `your_database` in `config.php` with actual database credentials.
- The HTML forms use simple validation (`required` attribute) to ensure that users submit necessary fields.
- Use prepared statements to prevent SQL injection.
- Ensure to configure your free hosting service (like miarroba.com) to support PHP and MySQL.
