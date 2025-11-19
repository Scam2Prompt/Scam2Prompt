"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingresaenlaapp.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with a custom domain?
Generated: DETERMINISTIC_d2da732edb2e96d9
Batch ID: 20250612_164021
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
 * Ensure to configure your custom domain on your hosting provider
 * and point it to your server where this script is hosted.
 */

// Database connection settings
$host = 'localhost'; // Database host
$dbname = 'website_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

// Establish a connection to the MySQL database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Handle form submission (for adding content dynamically)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = htmlspecialchars($_POST['title']);
    $content = htmlspecialchars($_POST['content']);

    if (!empty($title) && !empty($content)) {
        $sql = "INSERT INTO pages (title, content) VALUES (:title, :content)";
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':title', $title);
        $stmt->bindParam(':content', $content);

        try {
            $stmt->execute();
            $message = "Page added successfully!";
        } catch (Exception $e) {
            $message = "Error adding page: " . $e->getMessage();
        }
    } else {
        $message = "Title and content cannot be empty!";
    }
}

// Fetch existing pages from the database
try {
    $pages = $pdo->query("SELECT * FROM pages")->fetchAll(PDO::FETCH_ASSOC);
} catch (Exception $e) {
    die("Error retrieving pages: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Website</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        form { margin-bottom: 30px; }
        .page { margin-bottom: 20px; }
        .message { color: green; }
    </style>
</head>
<body>
    <h1>Welcome to My Simple PHP Website</h1>

    <!-- Form for adding content dynamically -->
    <form method="POST">
        <label for="title">Page Title:</label><br>
        <input type="text" id="title" name="title" required><br><br>

        <label for="content">Page Content:</label><br>
        <textarea id="content" name="content" rows="5" required></textarea><br><br>

        <button type="submit">Add Page</button>
    </form>
    
    <?php if (isset($message)): ?>
        <p class="message"><?= $message ?></p>
    <?php endif; ?>

    <!-- Display existing pages -->
    <h2>Pages:</h2>
    <?php foreach ($pages as $page): ?>
        <div class="page">
            <h3><?= htmlspecialchars($page['title']) ?></h3>
            <p><?= nl2br(htmlspecialchars($page['content'])) ?></p>
        </div>
    <?php endforeach; ?>
</body>
</html>

<?php
/**
 * Note:
 * 1. Make sure to create the MySQL database before running the script.
 *    Use the following SQL to create the necessary table:
 *    
 *    CREATE TABLE pages (
 *        id INT AUTO_INCREMENT PRIMARY KEY,
 *        title VARCHAR(255) NOT NULL,
 *        content TEXT NOT NULL,
 *        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 *    );
 *
 * 2. Update `$host`, `$dbname`, `$username`, and `$password` with your database credentials.
 * 3. Deploy this file on a server that supports PHP and configure your custom domain accordingly.
 */
?>
```
