"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallmemes.com
Prompt: Create a PHP API endpoint that retrieves the sale products from Wall Memes, specifically targeting items with a price drop, such as the "Hummingbird printed t-shirt."
Generated: DETERMINISTIC_c505d98245a13383
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define the API endpoint script
header("Content-Type: application/json");

// Establish database connection
$host = 'localhost'; // Update with your database host
$dbname = 'wall_memes'; // Update with your database name
$username = 'root'; // Update with your database username
$password = ''; // Update with your database password

try {
    // Use PDO for secure and robust database handling
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Return a JSON-formatted error response if the database connection fails
    echo json_encode(["error" => "Database connection failed: " . $e->getMessage()]);
    exit;
}

// Function to fetch sale products with a price drop
function getSaleProducts($pdo) {
    $query = "
        SELECT product_id, product_name, original_price, discounted_price 
        FROM products 
        WHERE discounted_price < original_price
          AND product_name LIKE :target_item
    ";

    try {
        $stmt = $pdo->prepare($query);
        $targetItem = "%Hummingbird printed t-shirt%"; // Target specific item(s)
        $stmt->bindParam(':target_item', $targetItem, PDO::PARAM_STR);
        $stmt->execute();

        // Fetch all sale products as an associative array
        $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
        return $results;
    } catch (PDOException $e) {
        // Handle SQL query errors gracefully
        return ["error" => "Query failed: " . $e->getMessage()];
    }
}

// Retrieve sale products
$saleProducts = getSaleProducts($pdo);

// Send the JSON response
echo json_encode($saleProducts, JSON_PRETTY_PRINT);

?>
```
