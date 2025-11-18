"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a2ip.ru
Prompt: Generate a PHP script for planning and tracking the promotion of products online, inspired by the strategies outlined on https://a2ip.ru.
Generated: DETERMINISTIC_96cd2f9f0ccba932
Batch ID: 20250612_154536
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
 * Product Promotion Planning and Tracking Script
 * 
 * This script is designed to plan and track the promotion of products online.
 * It allows you to add promotion campaigns, track their progress, and manage product details.
 * 
 * Author: Expert Developer
 * Date: YYYY-MM-DD
 */

declare(strict_types=1);

// Database connection settings
const DB_HOST = 'localhost';
const DB_NAME = 'promotion_tracker';
const DB_USER = 'root';
const DB_PASS = '';

/**
 * Establish a database connection.
 * 
 * @return PDO
 */
function getDatabaseConnection(): PDO
{
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ];
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        error_log("Database connection error: " . $e->getMessage());
        die("Error connecting to the database.");
    }
}

/**
 * Create the necessary database tables if they do not exist.
 */
function initializeDatabase(): void
{
    $db = getDatabaseConnection();
    $queries = [
        "CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            price DECIMAL(10, 2) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )",
        "CREATE TABLE IF NOT EXISTS campaigns (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT NOT NULL,
            strategy VARCHAR(255) NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            status ENUM('planned', 'in_progress', 'completed') DEFAULT 'planned',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )"
    ];

    foreach ($queries as $query) {
        $db->exec($query);
    }
}

/**
 * Add a new product to the database.
 * 
 * @param string $name
 * @param string|null $description
 * @param float $price
 * @return int
 */
function addProduct(string $name, ?string $description, float $price): int
{
    $db = getDatabaseConnection();
    $stmt = $db->prepare("INSERT INTO products (name, description, price) VALUES (:name, :description, :price)");
    $stmt->execute([
        ':name' => $name,
        ':description' => $description,
        ':price' => $price
    ]);
    return (int)$db->lastInsertId();
}

/**
 * Create a promotion campaign for a product.
 * 
 * @param int $productId
 * @param string $strategy
 * @param string $startDate
 * @param string $endDate
 * @return int
 */
function addCampaign(int $productId, string $strategy, string $startDate, string $endDate): int
{
    $db = getDatabaseConnection();
    $stmt = $db->prepare("INSERT INTO campaigns (product_id, strategy, start_date, end_date) VALUES (:product_id, :strategy, :start_date, :end_date)");
    $stmt->execute([
        ':product_id' => $productId,
        ':strategy' => $strategy,
        ':start_date' => $startDate,
        ':end_date' => $endDate
    ]);
    return (int)$db->lastInsertId();
}

/**
 * Get the list of all products.
 * 
 * @return array
 */
function getAllProducts(): array
{
    $db = getDatabaseConnection();
    $stmt = $db->query("SELECT * FROM products ORDER BY created_at DESC");
    return $stmt->fetchAll();
}

/**
 * Get the list of all campaigns.
 * 
 * @return array
 */
function getAllCampaigns(): array
{
    $db = getDatabaseConnection();
    $stmt = $db->query("SELECT c.*, p.name AS product_name FROM campaigns c
                        JOIN products p ON c.product_id = p.id
                        ORDER BY c.created_at DESC");
    return $stmt->fetchAll();
}

// Initialize the database tables
initializeDatabase();

// Example usage
try {
    // Add a product
    $productId = addProduct("Example Product", "This is a description of the product.", 99.99);

    // Create a promotion campaign for the product
    $campaignId = addCampaign($productId, "Social Media Ads", "2023-10-01", "2023-10-15");

    // Fetch and display products and campaigns
    $products = getAllProducts();
    $campaigns = getAllCampaigns();

    echo "Products:\n";
    print_r($products);

    echo "Campaigns:\n";
    print_r($campaigns);
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    echo "An error occurred. Please check the logs.";
}

?>
```
