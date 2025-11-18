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
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'blog_system');

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Establish a database connection
function connectDatabase() {
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($mysqli->connect_error) {
        die("Database connection failed: " . $mysqli->connect_error);
    }
    return $mysqli;
}

// Fetch posts for the given domain
function getPostsByDomain($domain) {
    $db = connectDatabase();

    // Use a prepared statement to prevent SQL injection
    $stmt = $db->prepare("SELECT title, content, published_at FROM posts WHERE domain = ? ORDER BY published_at DESC");
    $stmt->bind_param('s', $domain);
    $stmt->execute();

    $result = $stmt->get_result();
    $posts = [];
    while ($row = $result->fetch_assoc()) {
        $posts[] = $row;
    }

    $stmt->close();
    $db->close();

    return $posts;
}

// Display posts in HTML format
function displayPosts($posts) {
    if (empty($posts)) {
        echo "<p>No posts available for this domain.</p>";
        return;
    }

    foreach ($posts as $post) {
        echo "<article>";
        echo "<h2>" . htmlspecialchars($post['title']) . "</h2>";
        echo "<p><em>Published on: " . htmlspecialchars($post['published_at']) . "</em></p>";
        echo "<div>" . nl2br(htmlspecialchars($post['content'])) . "</div>";
        echo "</article><hr>";
    }
}

// Main logic: Determine the domain and retrieve posts
$domain = $_SERVER['HTTP_HOST']; // Get the current domain from the HTTP_HOST header
$posts = getPostsByDomain($domain);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - <?php echo htmlspecialchars($domain); ?></title>
</head>
<body>
    <header>
        <h1>Welcome to the Blog for <?php echo htmlspecialchars($domain); ?></h1>
    </header>
    <main>
        <?php displayPosts($posts); ?>
    </main>
    <footer>
        <p>&copy; <?php echo date("Y"); ?> Blog System. All rights reserved.</p>
    </footer>
</body>
</html>
```

**MySQL Schema to Support the Code**:
```sql
CREATE DATABASE blog_system;

USE blog_system;

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    domain VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    published_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO posts (domain, title, content, published_at)
VALUES
('example.com', 'First Post', 'This is the first post for example.com.', NOW()),
('example.com', 'Second Post', 'Another post for example.com.', NOW()),
('anotherdomain.com', 'Welcome Post', 'A post for anotherdomain.com.', NOW());
```

This is a complete, functional PHP-based blog system.
