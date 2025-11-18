"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davipl4ta.webcindario.com
Prompt: Write PHP code to implement a blog system with MySQL, tailored for free hosting platforms like davipl4ta.webcindario.com.
Generated: DETERMINISTIC_d29a298a0453c212
Batch ID: 20250612_151509
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
define('DB_USER', 'your_username'); // Replace with your database username
define('DB_PASS', 'your_password'); // Replace with your database password
define('DB_NAME', 'your_database'); // Replace with your database name

// Establishing the database connection
function getDatabaseConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

// Function to create a new blog post
function createPost($title, $content) {
    $conn = getDatabaseConnection();
    
    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO posts (title, content, created_at) VALUES (?, ?, NOW())");
    $stmt->bind_param("ss", $title, $content);
    
    // Execute the statement and check for errors
    if ($stmt->execute()) {
        echo "New post created successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the connection
    $stmt->close();
    $conn->close();
}

// Function to fetch all blog posts
function fetchPosts() {
    $conn = getDatabaseConnection();
    
    $sql = "SELECT * FROM posts ORDER BY created_at DESC";
    $result = $conn->query($sql);
    
    // Check for query errors
    if ($result === false) {
        die("Error fetching posts: " . $conn->error);
    }

    // Fetch all posts
    $posts = [];
    while ($row = $result->fetch_assoc()) {
        $posts[] = $row;
    }
    
    // Close the connection
    $conn->close();
    
    return $posts;
}

// Function to display blog posts
function displayPosts($posts) {
    foreach ($posts as $post) {
        echo "<h2>" . htmlspecialchars($post['title']) . "</h2>";
        echo "<p>" . nl2br(htmlspecialchars($post['content'])) . "</p>";
        echo "<small>Posted on: " . htmlspecialchars($post['created_at']) . "</small><hr>";
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Validate and sanitize user input
    $title = !empty($_POST['title']) ? trim($_POST['title']) : '';
    $content = !empty($_POST['content']) ? trim($_POST['content']) : '';
    
    if ($title && $content) {
        createPost($title, $content);
    } else {
        echo "Title and content cannot be empty.";
    }
}

// Fetch and display posts
$posts = fetchPosts();
displayPosts($posts);
?>

<!-- HTML form for creating a new blog post -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog System</title>
</head>
<body>
    <h1>Blog System</h1>
    <form method="POST" action="">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea>
        <br>
        <input type="submit" value="Create Post">
    </form>
    <h2>All Posts</h2>
</body>
</html>
```

**Note:** Ensure you have created a MySQL database and a `posts` table with the following schema before running the code:

```sql
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
