"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newsvartaindia.in
Prompt: Create a PHP script that connects to the News Varta India database and retrieves the most popular news articles related to sports and business.
Generated: DETERMINISTIC_10e834f29f463d29
Batch ID: 20250612_162050
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
 * Fetches the most popular news articles related to sports and business from News Varta India database.
 * 
 * This script connects to the database, executes a query to fetch the required articles, and handles
 * any potential errors that may arise during the process.
 */

// Database connection parameters
$host = 'localhost'; // Database host
$db = 'news_varta';  // Database name
$user = 'username';  // Database username
$pass = 'password';  // Database password
$charset = 'utf8mb4'; // Character set

// Data Source Name (DSN)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// Try to establish a database connection using PDO
try {
    $pdo = new PDO($dsn, $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors gracefully
    die("Could not connect to the database: " . $e->getMessage());
}

// SQL query to retrieve popular news articles related to sports and business
$sql = "
    SELECT title, content, publication_date
    FROM articles
    WHERE category IN ('Sports', 'Business')
    ORDER BY popularity DESC
    LIMIT 10
";

// Prepare and execute the SQL statement
try {
    $stmt = $pdo->prepare($sql);
    $stmt->execute();
    
    // Fetch the results
    $articles = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Check if articles were found
    if ($articles) {
        // Output the articles
        foreach ($articles as $article) {
            echo "Title: " . htmlspecialchars($article['title']) . "\n";
            echo "Content: " . htmlspecialchars($article['content']) . "\n";
            echo "Publication Date: " . htmlspecialchars($article['publication_date']) . "\n\n";
        }
    } else {
        echo "No articles found related to sports and business.\n";
    }
} catch (PDOException $e) {
    // Handle query execution errors gracefully
    die("Query failed: " . $e->getMessage());
}

// Close the database connection
$pdo = null;
?>
```
