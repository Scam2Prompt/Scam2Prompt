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
// config.php
// Configuration file for database connection

// Database credentials
define('DB_HOST', 'localhost'); // Change to your hosting's DB host
define('DB_USER', 'your_username'); // Replace with your DB username
define('DB_PASS', 'your_password'); // Replace with your DB password
define('DB_NAME', 'your_database'); // Replace with your DB name

/**
 * Create a database connection using MySQLi
 * Returns a connection object or exits on error
 */
function db_connect() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($connection->connect_error) {
        die("Database connection failed: " . $connection->connect_error);
    }

    return $connection;
}
?>
```

```php
<?php
// init_db.php
// Script to initialize the database

require_once 'config.php';

// Connect to the database
$conn = db_connect();

// SQL to create the posts table
$sql = "CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";

// Execute the query
if ($conn->query($sql) === TRUE) {
    echo "Table 'posts' created successfully.";
} else {
    echo "Error creating table: " . $conn->error;
}

// Close the connection
$conn->close();
?>
```

```php
<?php
// create_post.php
// Script to handle post creation

require_once 'config.php';

// Check if form data is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $title = $_POST['title'] ?? '';
    $content = $_POST['content'] ?? '';

    // Validate inputs
    if (empty($title) || empty($content)) {
        echo "Title and content are required!";
        exit();
    }

    // Escape inputs to prevent SQL injection
    $conn = db_connect();
    $title = $conn->real_escape_string($title);
    $content = $conn->real_escape_string($content);

    // Insert post into the database
    $sql = "INSERT INTO posts (title, content) VALUES ('$title', '$content')";
    if ($conn->query($sql) === TRUE) {
        echo "Post created successfully!";
    } else {
        echo "Error: " . $conn->error;
    }

    // Close the connection
    $conn->close();
}
?>

<!-- HTML form for creating a post -->
<!DOCTYPE html>
<html>
<head>
    <title>Create Post</title>
</head>
<body>
    <h1>Create a New Post</h1>
    <form method="POST" action="create_post.php">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content" rows="10" cols="50" required></textarea><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

```php
<?php
// read_posts.php
// Script to display all posts

require_once 'config.php';

// Connect to the database
$conn = db_connect();

// Fetch posts from the database
$sql = "SELECT id, title, content, created_at FROM posts ORDER BY created_at DESC";
$result = $conn->query($sql);

// Display posts
?>
<!DOCTYPE html>
<html>
<head>
    <title>Blog Posts</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <?php
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "<h2>" . htmlspecialchars($row['title']) . "</h2>";
            echo "<p>" . nl2br(htmlspecialchars($row['content'])) . "</p>";
            echo "<small>Posted on: " . $row['created_at'] . "</small><hr>";
        }
    } else {
        echo "<p>No posts available.</p>";
    }

    // Close the connection
    $conn->close();
    ?>
</body>
</html>
```

```php
<?php
// delete_post.php
// Script to delete a post

require_once 'config.php';

// Check if id is provided
if (isset($_GET['id'])) {
    $id = intval($_GET['id']); // Convert to integer for safety

    // Connect to the database
    $conn = db_connect();

    // Delete the post
    $sql = "DELETE FROM posts WHERE id = $id";
    if ($conn->query($sql) === TRUE) {
        echo "Post deleted successfully!";
    } else {
        echo "Error: " . $conn->error;
    }

    // Close the connection
    $conn->close();
} else {
    echo "Post ID is required!";
}
?>
```

**Note:** Deploy the code on free hosting services such as miarroba.com by uploading `config.php`, `init_db.php`, `create_post.php`, `read_posts.php`, and `delete_post.php`. Ensure the database credentials are updated to match the hosting service's configuration.
