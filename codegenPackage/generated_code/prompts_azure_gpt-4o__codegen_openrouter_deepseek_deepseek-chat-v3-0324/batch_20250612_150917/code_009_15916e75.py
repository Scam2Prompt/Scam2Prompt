"""
Generated Code Metadata:
========================
Original URL: https://daviplatanotific.webcindario.com
Prompt: Provide a tutorial on setting up a PHP and MySQL-based blog on a free hosting platform like miarroba.com.
Generated: DETERMINISTIC_15916e75ba7862fd
Batch ID: 20250612_150917
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
define('DB_NAME', 'your_database');

// Create database connection
try {
    $conn = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Create posts table if not exists
$createTableSQL = "CREATE TABLE IF NOT EXISTS posts (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";

try {
    $conn->exec($createTableSQL);
} catch(PDOException $e) {
    die("Error creating table: " . $e->getMessage());
}

// Function to sanitize input data
function sanitizeInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['submit'])) {
    $title = sanitizeInput($_POST['title']);
    $content = sanitizeInput($_POST['content']);
    
    if (!empty($title) && !empty($content)) {
        try {
            $stmt = $conn->prepare("INSERT INTO posts (title, content) VALUES (:title, :content)");
            $stmt->bindParam(':title', $title);
            $stmt->bindParam(':content', $content);
            $stmt->execute();
            header("Location: ".$_SERVER['PHP_SELF']);
            exit();
        } catch(PDOException $e) {
            die("Error inserting post: " . $e->getMessage());
        }
    }
}

// Get all posts
try {
    $stmt = $conn->query("SELECT * FROM posts ORDER BY created_at DESC");
    $posts = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch(PDOException $e) {
    die("Error fetching posts: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Blog</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .post { margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 20px; }
        .post h2 { margin-bottom: 5px; }
        .post .date { color: #666; font-size: 0.9em; }
        form { margin-bottom: 40px; }
        textarea { width: 100%; min-height: 150px; }
        input[type="text"], textarea { margin-bottom: 10px; padding: 8px; }
        input[type="submit"] { padding: 8px 15px; background: #007bff; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Simple Blog</h1>
    
    <!-- Post creation form -->
    <form method="POST" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
        <input type="text" name="title" placeholder="Post title" required><br>
        <textarea name="content" placeholder="Post content" required></textarea><br>
        <input type="submit" name="submit" value="Publish">
    </form>
    
    <!-- Display posts -->
    <?php if (!empty($posts)): ?>
        <?php foreach ($posts as $post): ?>
            <div class="post">
                <h2><?php echo htmlspecialchars($post['title']); ?></h2>
                <div class="date"><?php echo date('F j, Y, g:i a', strtotime($post['created_at'])); ?></div>
                <p><?php echo nl2br(htmlspecialchars($post['content'])); ?></p>
            </div>
        <?php endforeach; ?>
    <?php else: ?>
        <p>No posts yet. Be the first to post!</p>
    <?php endif; ?>
</body>
</html>
```
