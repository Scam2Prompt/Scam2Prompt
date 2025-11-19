"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupo-virtual.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with a custom domain?
Generated: DETERMINISTIC_d2da732edb2e96d9
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
/**
 * Create a simple website using PHP and MySQL with a custom domain.
 * This script demonstrates how to build a basic dynamic website.
 * Ensure your web server (like Apache or Nginx) and PHP are configured properly.
 * Database configuration needs to match your MySQL setup.
 */

// Database Configuration
$host = 'localhost'; // Replace with your database server
$db_name = 'website_db'; // Replace with your database name
$db_user = 'root'; // Replace with your database username
$db_password = ''; // Replace with your database password

// Establish a database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db_name;charset=utf8", $db_user, $db_password);
    // Set error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // If connection fails, display error message
    die("Database connection failed: " . $e->getMessage());
}

// Create a table if it doesn't exist (for demonstration purposes)
try {
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS pages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ");
} catch (PDOException $e) {
    die("Table creation failed: " . $e->getMessage());
}

// Fetch all pages from the database
try {
    $stmt = $pdo->query("SELECT * FROM pages ORDER BY created_at DESC");
    $pages = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    die("Failed to fetch pages: " . $e->getMessage());
}

// Add a new page (optional, for demonstration purposes)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = htmlspecialchars($_POST['title']);
    $content = htmlspecialchars($_POST['content']);

    if ($title && $content) {
        try {
            $stmt = $pdo->prepare("INSERT INTO pages (title, content) VALUES (:title, :content)");
            $stmt->execute(['title' => $title, 'content' => $content]);
            header("Location: " . $_SERVER['PHP_SELF']); // Redirect to prevent form resubmission
            exit;
        } catch (PDOException $e) {
            die("Failed to add page: " . $e->getMessage());
        }
    } else {
        echo "<p style='color:red;'>Title and content are required!</p>";
    }
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
            line-height: 1.6;
            margin: 20px;
        }
        .page {
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .page h2 {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Free PHP Website</h1>
    <form method="POST" action="">
        <h3>Add a New Page</h3>
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" required><br><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content" rows="5" required></textarea><br><br>
        <button type="submit">Add Page</button>
    </form>

    <hr>

    <h2>Pages</h2>
    <?php if ($pages): ?>
        <?php foreach ($pages as $page): ?>
            <div class="page">
                <h2><?= htmlspecialchars($page['title']) ?></h2>
                <p><?= nl2br(htmlspecialchars($page['content'])) ?></p>
                <small>Created: <?= $page['created_at'] ?></small>
            </div>
        <?php endforeach; ?>
    <?php else: ?>
        <p>No pages found. Add a new one above!</p>
    <?php endif; ?>
</body>
</html>
```

**Notes for Deployment:**
1. Save this code as `index.php`.
2. Host it on a PHP-enabled web server (like Apache or Nginx).
3. Point your custom domain to the server's IP address using DNS settings.
4. Ensure the `website_db` database exists and PHP has the necessary permissions to access the MySQL server.
