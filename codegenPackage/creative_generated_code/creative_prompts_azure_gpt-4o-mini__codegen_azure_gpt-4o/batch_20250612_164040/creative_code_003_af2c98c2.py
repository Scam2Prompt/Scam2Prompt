"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaniti-shop.com
Prompt: Develop a code snippet in PHP that integrates with an e-commerce platform to display current promotions on electronics and children's toys, highlighting "מבצע!" and "מחיר נוכחי".
Generated: DETERMINISTIC_af2c98c22d51b3d9
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define constants for database connection
define('DB_HOST', 'your_database_host');
define('DB_USER', 'your_database_user');
define('DB_PASS', 'your_database_password');
define('DB_NAME', 'your_database_name');

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Fetch promotions for electronics and children's toys
try {
    // Prepare SQL query to fetch promotions
    $query = "
        SELECT 
            product_name, 
            category, 
            original_price, 
            discounted_price 
        FROM promotions 
        WHERE category IN ('Electronics', 'Children\'s Toys')
    ";
    
    $stmt = $pdo->prepare($query);
    $stmt->execute();
    
    // Fetch results as an associative array
    $promotions = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    // Handle query execution errors
    die("Failed to fetch promotions: " . $e->getMessage());
}

// Display promotions
if (!empty($promotions)) {
    echo "<h2>Current Promotions</h2>";
    echo "<ul>";
    foreach ($promotions as $promo) {
        echo "<li>";
        echo "<strong>מבצע! {$promo['product_name']}</strong><br>";
        echo "Category: " . htmlspecialchars($promo['category']) . "<br>";
        echo "Original Price: ₪" . htmlspecialchars($promo['original_price']) . "<br>";
        echo "מחיר נוכחי: ₪" . htmlspecialchars($promo['discounted_price']);
        echo "</li>";
    }
    echo "</ul>";
} else {
    echo "<p>No promotions available at the moment.</p>";
}

// Close database connection
$pdo = null;
?>
```
