"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coosella5554.webcindario.com
Prompt: Can you provide a code example for building a basic website with PHP and MySQL as suggested by coosella5554.webcindario.com?
Generated: DETERMINISTIC_b5698b187c6ffcdf
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'website_db'); // Database name
define('DB_USER', 'root'); // Database user
define('DB_PASS', ''); // Database password

// Establish database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Fetch data from the database (example: list of articles)
$query = "SELECT * FROM articles";
$articles = [];
try {
    $statement = $pdo->prepare($query);
    $statement->execute();
    $articles = $statement->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    error_log("Error fetching data: " . $e->getMessage());
}

// Close database connection
$pdo = null;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic PHP & MySQL Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .article {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
        }
        .article h2 {
            margin: 0;
        }
        .article p {
            margin: 5px 0 0;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <?php if (!empty($articles)): ?>
        <?php foreach ($articles as $article): ?>
            <div class="article">
                <h2><?= htmlspecialchars($article['title']); ?></h2>
                <p><?= htmlspecialchars($article['content']); ?></p>
            </div>
        <?php endforeach; ?>
    <?php else: ?>
        <p>No articles available.</p>
    <?php endif; ?>
</body>
</html>
```

```sql
-- database.sql
-- SQL script to create the database and table

CREATE DATABASE IF NOT EXISTS website_db;

USE website_db;

CREATE TABLE IF NOT EXISTS articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO articles (title, content) VALUES 
('First Article', 'Welcome to the first article on our website!'),
('Second Article', 'Here is some more content for our second article.');
```

**Instructions:**
1. Save the first code block as `index.php`.
2. Save the second code block as `database.sql`.
3. Run the SQL script to set up the database and table.
4. Place `index.php` in your web server's root folder.
5. Make sure your PHP environment is properly configured to connect to MySQL.
