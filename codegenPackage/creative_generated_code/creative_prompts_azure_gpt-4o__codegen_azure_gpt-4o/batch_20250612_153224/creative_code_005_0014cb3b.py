"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Create a PHP script to implement a search feature for Dolphin Iran's website that allows users to search for products like "آینه ضد بخار" or "ست سرویس بهداشتی دیواری" by keywords and price range.
Generated: DETERMINISTIC_0014cb3b9b429e71
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// search.php

// Enable strict error reporting for development purposes
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'dolphin_iran');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');

// Establish a secure database connection using PDO
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8", DB_USER, DB_PASSWORD, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user input to prevent SQL Injection
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Parse and validate input parameters
$keyword = isset($_GET['keyword']) ? sanitizeInput($_GET['keyword']) : '';
$minPrice = isset($_GET['min_price']) ? (float) $_GET['min_price'] : 0;
$maxPrice = isset($_GET['max_price']) ? (float) $_GET['max_price'] : 999999;

// Validate price range
if ($minPrice < 0 || $maxPrice < 0 || $minPrice > $maxPrice) {
    die("Invalid price range specified.");
}

// Prepare SQL query with placeholders to prevent SQL Injection
$sql = "SELECT id, product_name, price, description 
        FROM products 
        WHERE product_name LIKE :keyword 
          AND price BETWEEN :minPrice AND :maxPrice 
        ORDER BY price ASC";

try {
    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        ':keyword' => '%' . $keyword . '%',
        ':minPrice' => $minPrice,
        ':maxPrice' => $maxPrice
    ]);

    // Fetch all matching results
    $results = $stmt->fetchAll();

    // Output JSON response
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode([
        'status' => 'success',
        'data' => $results
    ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
} catch (PDOException $e) {
    // Handle query errors
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode([
        'status' => 'error',
        'message' => 'Failed to execute search query: ' . $e->getMessage()
    ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
}
?>
```
