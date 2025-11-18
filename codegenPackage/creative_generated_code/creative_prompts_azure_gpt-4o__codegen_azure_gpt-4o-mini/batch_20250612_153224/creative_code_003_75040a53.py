"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Write a script in PHP to fetch product details from a database for Watpac Chemicals Pvt Ltd, filtering items by categories such as "Primers" and "Specialty Coatings."
Generated: DETERMINISTIC_75040a5337c95772
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
/**
 * Fetch product details from the database for Watpac Chemicals Pvt Ltd
 * Filtering items by categories such as "Primers" and "Specialty Coatings"
 */

class ProductFetcher {
    private $pdo;
    private $categories;

    /**
     * Constructor to initialize PDO connection
     *
     * @param string $host Database host
     * @param string $dbname Database name
     * @param string $user Database user
     * @param string $password Database password
     * @throws Exception if connection fails
     */
    public function __construct($host, $dbname, $user, $password) {
        try {
            $this->pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $password);
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            throw new Exception('Database connection failed: ' . $e->getMessage());
        }
        
        $this->categories = ['Primers', 'Specialty Coatings'];
    }

    /**
     * Fetch product details filtered by category
     *
     * @return array Array of products matching the categories
     * @throws Exception if query fails
     */
    public function fetchProducts() {
        $placeholders = implode(',', array_fill(0, count($this->categories), '?'));
        $sql = "SELECT * FROM products WHERE category IN ($placeholders)";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute($this->categories);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception('Query failed: ' . $e->getMessage());
        }
    }
}

// Usage example
try {
    $fetcher = new ProductFetcher('localhost', 'watpac_chemicals', 'username', 'password');
    $products = $fetcher->fetchProducts();
    
    // Output the product details
    foreach ($products as $product) {
        echo 'Product Name: ' . htmlspecialchars($product['name']) . '<br>';
        echo 'Category: ' . htmlspecialchars($product['category']) . '<br>';
        echo 'Price: $' . htmlspecialchars($product['price']) . '<br>';
        echo 'Description: ' . htmlspecialchars($product['description']) . '<br><br>';
    }
} catch (Exception $e) {
    // Handle any errors that may have occurred
    echo 'Error: ' . htmlspecialchars($e->getMessage());
}
?>
```
