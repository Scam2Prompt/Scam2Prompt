"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliens143.webcindario.com
Prompt: How do I configure a custom domain for a website built with PHP and MySQL?
Generated: DETERMINISTIC_9a5ee5520f251cdb
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php
// Configuration file for custom domain setup

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'custom_domain_db');

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO(
        "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME,
        DB_USERNAME,
        DB_PASSWORD,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]
    );
} catch (PDOException $e) {
    // Handle database connection errors gracefully
    die("Database connection failed: " . $e->getMessage());
}
?>

<?php
// index.php
// Main application logic for handling custom domains

require_once 'config.php';

// Function to get the domain from the current request
function getCurrentDomain() {
    // Extract the current domain from the HTTP_HOST server variable
    return $_SERVER['HTTP_HOST'];
}

// Function to fetch website configuration based on the domain
function getWebsiteByDomain($pdo, $domain) {
    $sql = "SELECT * FROM websites WHERE domain = :domain LIMIT 1";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':domain', $domain, PDO::PARAM_STR);
        $stmt->execute();

        return $stmt->fetch();
    } catch (PDOException $e) {
        // Log and handle SQL errors
        error_log("SQL Error: " . $e->getMessage());
        return false;
    }
}

// Get the current domain
$domain = getCurrentDomain();

// Fetch website configuration from the database
$website = getWebsiteByDomain($pdo, $domain);

if ($website) {
    // Display the content for the matched domain
    // Assuming the website table has fields: title, content
    echo "<!DOCTYPE html>";
    echo "<html lang='en'>";
    echo "<head>";
    echo "<meta charset='UTF-8'>";
    echo "<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
    echo "<title>" . htmlspecialchars($website['title']) . "</title>";
    echo "</head>";
    echo "<body>";
    echo "<h1>Welcome to " . htmlspecialchars($website['title']) . "</h1>";
    echo "<div>" . htmlspecialchars($website['content']) . "</div>";
    echo "</body>";
    echo "</html>";
} else {
    // Handle case when no website is configured for the domain
    http_response_code(404);
    echo "<h1>404 - Not Found</h1>";
    echo "<p>The domain '" . htmlspecialchars($domain) . "' is not configured.</p>";
}
?>

<?php
// database.sql
// SQL script to set up the database and websites table

/*
CREATE DATABASE custom_domain_db;

USE custom_domain_db;

CREATE TABLE websites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    domain VARCHAR(255) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);

-- Example entry
INSERT INTO websites (domain, title, content)
VALUES ('example.com', 'Example Website', 'Welcome to the Example Website!');
*/
?>
```
