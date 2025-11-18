"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplatanotific.webcindario.com
Prompt: Provide a tutorial on setting up a PHP and MySQL-based blog on a free hosting platform like miarroba.com.
Generated: DETERMINISTIC_15916e75ba7862fd
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/*
 * Blog Setup Script
 * This script initializes a simple PHP and MySQL-based blog.
 * It includes database connection, table creation, and a basic blog post display.
 * Ensure the hosting platform (e.g., miarroba.com) supports PHP and MySQL.
 */

// Database configuration
define('DB_HOST', 'your_host');          // Replace with your database host
define('DB_USER', 'your_username');      // Replace with your database username
define('DB_PASSWORD', 'your_password');  // Replace with your database password
define('DB_NAME', 'your_database_name'); // Replace with your database name

// Connect to the database
try {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        throw new Exception("Connection failed: " . $conn->connect_error);
    }
} catch (Exception $e) {
    die("Error: " . $e->getMessage());
}

// Create the blog_posts table if it doesn't exist
$table_creation_query = "
    CREATE TABLE IF NOT EXISTS blog_posts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
";

if (!$conn->query($table_creation_query)) {
    die("Error creating table: " . $conn->error);
}

// Insert sample blog post (only if table is empty)
$check_posts_query = "SELECT COUNT(*) AS post_count FROM blog_posts";
$result = $conn->query($check_posts_query);

if ($result) {
    $row = $result->fetch_assoc();
    if ($row['post_count'] == 0) {
        $insert_sample_post_query = "
            INSERT INTO blog_posts (title, content)
            VALUES ('Welcome to My Blog', 'This is your first blog post! Edit this content to personalize your blog.')
        ";

        if (!$conn->query($insert_sample_post_query)) {
            die("Error inserting sample post: " . $conn->error);
        }
    }
}

// Fetch all blog posts for display
$fetch_posts_query = "SELECT * FROM blog_posts ORDER BY created_at DESC";
$posts_result = $conn->query($fetch_posts_query);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Blog</title>
    <!-- Basic CSS for styling -->
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        .post {
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .post h2 {
            margin: 0 0 10px;
        }
        .post p {
            margin: 0;
        }
        .post time {
            display: block;
            margin-bottom: 10px;
            color: #666;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Blog</h1>

    <?php
    // Display all blog posts
    if ($posts_result && $posts_result->num_rows > 0) {
        while ($post = $posts_result->fetch_assoc()) {
            echo "<div class='post'>";
            echo "<h2>" . htmlspecialchars($post['title']) . "</h2>";
            echo "<time>Posted on " . htmlspecialchars($post['created_at']) . "</time>";
            echo "<p>" . nl2br(htmlspecialchars($post['content'])) . "</p>";
            echo "</div>";
        }
    } else {
        echo "<p>No posts available. Start writing your blog!</p>";
    }

    // Close the database connection
    $conn->close();
    ?>
</body>
</html>
```
