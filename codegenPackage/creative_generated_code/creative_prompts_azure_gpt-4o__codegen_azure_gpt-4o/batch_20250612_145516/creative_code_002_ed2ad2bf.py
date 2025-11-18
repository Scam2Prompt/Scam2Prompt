"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validardvplta.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database and display dynamic content on a webpage.
Generated: DETERMINISTIC_ed2ad2bf1a10fa18
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
// Configuration settings
$host = 'localhost'; // Database host
$dbname = 'example_database'; // Database name
$username = 'example_user'; // Database username
$password = 'example_password'; // Database password

try {
    // Create a new PDO instance to connect to the database
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);

    // Set PDO error mode to exception for better error handling
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Query to fetch dynamic content
    $stmt = $pdo->query("SELECT title, content FROM articles ORDER BY created_at DESC");

    // Fetch all rows as an associative array
    $articles = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    // Handle database connection or query errors
    die("Database connection failed: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Content</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        article {
            margin-bottom: 20px;
            padding: 15px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        h2 {
            color: #555;
        }
    </style>
</head>
<body>
    <h1>Dynamic Content from Database</h1>

    <?php if (!empty($articles)): ?>
        <!-- Loop through the articles and display them -->
        <?php foreach ($articles as $article): ?>
            <article>
                <h2><?= htmlspecialchars($article['title']) ?></h2>
                <p><?= nl2br(htmlspecialchars($article['content'])) ?></p>
            </article>
        <?php endforeach; ?>
    <?php else: ?>
        <!-- Fallback content if no articles are found -->
        <p>No articles found.</p>
    <?php endif; ?>
</body>
</html>
```
