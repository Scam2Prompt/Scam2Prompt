"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupo-virtual.webcindario.com
Prompt: Can you provide a code example for building a simple website with PHP and MySQL?
Generated: DETERMINISTIC_86be3caa68182ca3
Batch ID: 20250612_161017
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
 * Simple PHP Website with MySQL Integration
 * - A basic example demonstrating PHP and MySQL for serving dynamic web pages.
 * - Ensure you have PHP installed and a MySQL database set up to test the code.
 */

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root');      // Database username
define('DB_PASS', 'password');  // Database password
define('DB_NAME', 'simple_site'); // Database name

// Connect to the MySQL database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exceptions for errors
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage()); // Gracefully handle connection errors
}

// Create table if it doesn't exist
try {
    $pdo->exec(
        "CREATE TABLE IF NOT EXISTS posts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"
    );
} catch (PDOException $e) {
    die("Table creation failed: " . $e->getMessage());
}

// Insert a sample post (if empty)
try {
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM posts");
    $stmt->execute();
    if ($stmt->fetchColumn() == 0) {
        $pdo->exec(
            "INSERT INTO posts (title, content) 
            VALUES 
            ('Welcome to My Website', 'This is a simple PHP and MySQL-powered website.')"
        );
    }
} catch (PDOException $e) {
    die("Error inserting sample post: " . $e->getMessage());
}

// Fetch posts from the database
try {
    $stmt = $pdo->prepare("SELECT * FROM posts ORDER BY created_at DESC");
    $stmt->execute();
    $posts = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    die("Error fetching posts: " . $e->getMessage());
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .post {
            margin-bottom: 30px;
        }
        .post h2 {
            font-size: 20px;
            margin-bottom: 10px;
        }
        .post p {
            font-size: 16px;
            line-height: 1.6;
        }
        .post time {
            display: block;
            font-size: 12px;
            color: #666;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Simple PHP Website</h1>
        <?php if (!empty($posts)): ?>
            <?php foreach ($posts as $post): ?>
                <div class="post">
                    <h2><?php echo htmlspecialchars($post['title']); ?></h2>
                    <time><?php echo date('F j, Y, g:i a', strtotime($post['created_at'])); ?></time>
                    <p><?php echo nl2br(htmlspecialchars($post['content'])); ?></p>
                </div>
            <?php endforeach; ?>
        <?php else: ?>
            <p>No posts available.</p>
        <?php endif; ?>
    </div>
</body>
</html>
```
