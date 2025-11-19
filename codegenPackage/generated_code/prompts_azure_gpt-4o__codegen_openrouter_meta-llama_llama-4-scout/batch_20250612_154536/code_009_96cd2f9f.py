"""
Generated Code Metadata:
========================
Original URL: https://a2ip.ru
Prompt: Generate a PHP script for planning and tracking the promotion of products online, inspired by the strategies outlined on https://a2ip.ru.
Generated: DETERMINISTIC_96cd2f9f0ccba932
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Product Promotion Tracker
 *
 * This script allows for planning and tracking the promotion of products online.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'promotion_tracker',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Database connection failed: ' . $e->getMessage());
}

// Create Table
$query = "
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
";

$query .= "
    CREATE TABLE IF NOT EXISTS promotions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_id INT NOT NULL,
        promotion_strategy VARCHAR(255) NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        budget DECIMAL(10, 2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(id)
    );
";

try {
    $pdo->exec($query);
} catch (PDOException $e) {
    throw new Exception('Table creation failed: ' . $e->getMessage());
}

// Product Class
class Product
{
    private $pdo;
    private $id;
    private $name;
    private $description;

    public function __construct($pdo, $id = null)
    {
        $this->pdo = $pdo;
        $this->id = $id;
    }

    public function create($name, $description)
    {
        $query = "
            INSERT INTO products (name, description)
            VALUES (:name, :description);
        ";

        try {
            $stmt = $this->pdo->prepare($query);
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':description', $description);
            $stmt->execute();
            return $this->pdo->lastInsertId();
        } catch (PDOException $e) {
            throw new Exception('Product creation failed: ' . $e->getMessage());
        }
    }

    public function getAll()
    {
        $query = "
            SELECT * FROM products;
        ";

        try {
            $stmt = $this->pdo->query($query);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception('Product retrieval failed: ' . $e->getMessage());
        }
    }
}

// Promotion Class
class Promotion
{
    private $pdo;
    private $id;
    private $productId;
    private $promotionStrategy;
    private $startDate;
    private $endDate;
    private $budget;

    public function __construct($pdo, $id = null)
    {
        $this->pdo = $pdo;
        $this->id = $id;
    }

    public function create($productId, $promotionStrategy, $startDate, $endDate, $budget)
    {
        $query = "
            INSERT INTO promotions (product_id, promotion_strategy, start_date, end_date, budget)
            VALUES (:product_id, :promotion_strategy, :start_date, :end_date, :budget);
        ";

        try {
            $stmt = $this->pdo->prepare($query);
            $stmt->bindParam(':product_id', $productId);
            $stmt->bindParam(':promotion_strategy', $promotionStrategy);
            $stmt->bindParam(':start_date', $startDate);
            $stmt->bindParam(':end_date', $endDate);
            $stmt->bindParam(':budget', $budget);
            return $stmt->execute();
        } catch (PDOException $e) {
            throw new Exception('Promotion creation failed: ' . $e->getMessage());
        }
    }

    public function getAll()
    {
        $query = "
            SELECT * FROM promotions;
        ";

        try {
            $stmt = $this->pdo->query($query);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception('Promotion retrieval failed: ' . $e->getMessage());
        }
    }
}

// Example Usage
$product = new Product($pdo);
$promotion = new Promotion($pdo);

// Create Product
$productId = $product->create('Example Product', 'This is an example product');

// Create Promotion
$promotion->create($productId, 'Social Media Ads', '2024-01-01', '2024-01-31', 1000.00);

// Get All Products
$products = $product->getAll();
print_r($products);

// Get All Promotions
$promotions = $promotion->getAll();
print_r($promotions);

?>
```
