"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validardvplta.webcindario.com
Prompt: Generate code for a PHP-based blog system that uses MySQL for content storage and supports custom domains.
Generated: DETERMINISTIC_c9e62cf36a8dda87
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username'); // Change to your database username
define('DB_PASS', 'password'); // Change to your database password
define('DB_NAME', 'blog_db'); // Change to your database name

// Establish a connection to the MySQL database
function dbConnect() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

// Create a function to fetch all blog posts
function getPosts($conn) {
    $sql = "SELECT id, title, content, created_at FROM posts ORDER BY created_at DESC";
    $result = $conn->query($sql);
    
    if (!$result) {
        throw new Exception("Database query error: " . $conn->error);
    }
    
    return $result->fetch_all(MYSQLI_ASSOC);
}

// Create a function to add a new post
function addPost($conn, $title, $content) {
    $stmt = $conn->prepare("INSERT INTO posts (title, content, created_at) VALUES (?, ?, NOW())");
    $stmt->bind_param("ss", $title, $content);
    
    if (!$stmt->execute()) {
        throw new Exception("Error adding post: " . $stmt->error);
    }
    
    $stmt->close();
}

// Create a function to delete a post
function deletePost($conn, $id) {
    $stmt = $conn->prepare("DELETE FROM posts WHERE id = ?");
    $stmt->bind_param("i", $id);
    
    if (!$stmt->execute()) {
        throw new Exception("Error deleting post: " . $stmt->error);
    }
    
    $stmt->close();
}

// Create a function to display posts on the page
function displayPosts($posts) {
    foreach ($posts as $post) {
        echo "<h2>" . htmlspecialchars($post['title']) . "</h2>";
        echo "<p>" . nl2br(htmlspecialchars($post['content'])) . "</p>";
        echo "<small>Posted on " . date("F j, Y", strtotime($post['created_at'])) . "</small>";
        echo "<hr>";
    }
}

// Main execution
try {
    // Connect to the database
    $conn = dbConnect();
    
    // Check if the form is submitted to add a new post
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['title'], $_POST['content'])) {
        addPost($conn, $_POST['title'], $_POST['content']);
        header("Location: " . $_SERVER['PHP_SELF']);
        exit;
    }
    
    // Fetch all posts
    $posts = getPosts($conn);
    
} catch (Exception $e) {
    // Display error messages
    echo "Error: " . $e->getMessage();
} finally {
    // Close the database connection
    if (isset($conn) && $conn) {
        $conn->close();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Blog</title>
</head>
<body>
    <h1>My Blog</h1>
    
    <!-- Form to add a new post -->
    <form method="POST">
        <input type="text" name="title" placeholder="Post Title" required>
        <textarea name="content" placeholder="Post Content" required></textarea>
        <button type="submit">Add Post</button>
    </form>
    
    <hr>
    
    <!-- Display posts -->
    <?php displayPosts($posts); ?>
</body>
</html>
```

**Database Table Structure:**

```sql
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Note:** Remember to replace the database credentials and adjust any configurations as per your server setup. Additionally, consider using environment variables for sensitive information in a real production environment.
