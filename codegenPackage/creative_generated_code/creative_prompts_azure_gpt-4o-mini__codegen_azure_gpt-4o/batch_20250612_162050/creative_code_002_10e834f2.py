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
// Configuration for database connection
$host = 'localhost';         // Database host
$dbname = 'news_varta_india'; // Database name
$username = 'root';           // Database username
$password = '';               // Database password

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Error connecting to the database: " . $e->getMessage());
}

// Function to fetch the most popular articles for a given category
function getPopularArticles(PDO $pdo, string $category, int $limit = 10): array {
    try {
        // Prepare the SQL query to retrieve articles based on category and popularity
        $stmt = $pdo->prepare("
            SELECT title, content, author, published_date, views 
            FROM articles 
            WHERE category = :category 
            ORDER BY views DESC 
            LIMIT :limit
        ");
        
        // Bind parameters to prevent SQL injection
        $stmt->bindParam(':category', $category, PDO::PARAM_STR);
        $stmt->bindParam(':limit', $limit, PDO::PARAM_INT);
        
        // Execute the query
        $stmt->execute();
        
        // Fetch all matching articles
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Log and rethrow the error for handling by the caller
        error_log("Error fetching articles: " . $e->getMessage());
        throw new Exception("Failed to fetch articles for category: $category");
    }
}

// Fetch and display the most popular articles for sports and business
try {
    $sportsArticles = getPopularArticles($pdo, 'sports');
    $businessArticles = getPopularArticles($pdo, 'business');

    echo "<h1>Most Popular Sports Articles</h1>";
    foreach ($sportsArticles as $article) {
        echo "<h2>" . htmlspecialchars($article['title']) . "</h2>";
        echo "<p>" . htmlspecialchars($article['content']) . "</p>";
        echo "<p><strong>Author:</strong> " . htmlspecialchars($article['author']) . "</p>";
        echo "<p><strong>Published Date:</strong> " . htmlspecialchars($article['published_date']) . "</p>";
        echo "<p><strong>Views:</strong> " . htmlspecialchars($article['views']) . "</p>";
        echo "<hr>";
    }

    echo "<h1>Most Popular Business Articles</h1>";
    foreach ($businessArticles as $article) {
        echo "<h2>" . htmlspecialchars($article['title']) . "</h2>";
        echo "<p>" . htmlspecialchars($article['content']) . "</p>";
        echo "<p><strong>Author:</strong> " . htmlspecialchars($article['author']) . "</p>";
        echo "<p><strong>Published Date:</strong> " . htmlspecialchars($article['published_date']) . "</p>";
        echo "<p><strong>Views:</strong> " . htmlspecialchars($article['views']) . "</p>";
        echo "<hr>";
    }
} catch (Exception $e) {
    // Handle errors during article retrieval or display
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
