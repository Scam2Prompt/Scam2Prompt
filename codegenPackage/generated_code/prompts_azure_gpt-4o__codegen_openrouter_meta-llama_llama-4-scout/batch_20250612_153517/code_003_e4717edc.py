"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Generate code in PHP to implement a "Wish List" feature for an online store, allowing users to add items from categories like "Pompa Apa," "Motocoasa," and "Scule electrice."
Generated: DETERMINISTIC_e4717edcd9dc2f03
Batch ID: 20250612_153517
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
 * Wish List class for managing user wish lists.
 */
class WishList {
    private $db;
    private $userId;

    /**
     * Constructor for WishList class.
     * 
     * @param PDO $db     Database connection.
     * @param int  $userId User ID.
     */
    public function __construct(PDO $db, int $userId) {
        $this->db = $db;
        $this->userId = $userId;
    }

    /**
     * Add item to wish list.
     * 
     * @param int $productId Product ID.
     * 
     * @return bool True if added, false otherwise.
     */
    public function addItem(int $productId): bool {
        try {
            $stmt = $this->db->prepare("INSERT INTO wish_list (user_id, product_id) VALUES (:userId, :productId)");
            $stmt->bindParam(':userId', $this->userId);
            $stmt->bindParam(':productId', $productId);
            return $stmt->execute() > 0;
        } catch (PDOException $e) {
            // Log error
            error_log("Error adding item to wish list: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Remove item from wish list.
     * 
     * @param int $productId Product ID.
     * 
     * @return bool True if removed, false otherwise.
     */
    public function removeItem(int $productId): bool {
        try {
            $stmt = $this->db->prepare("DELETE FROM wish_list WHERE user_id = :userId AND product_id = :productId");
            $stmt->bindParam(':userId', $this->userId);
            $stmt->bindParam(':productId', $productId);
            return $stmt->execute() > 0;
        } catch (PDOException $e) {
            // Log error
            error_log("Error removing item from wish list: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get all items in wish list.
     * 
     * @return array List of products.
     */
    public function getItems(): array {
        try {
            $stmt = $this->db->prepare("SELECT p.* FROM wish_list wl JOIN products p ON wl.product_id = p.id WHERE wl.user_id = :userId");
            $stmt->bindParam(':userId', $this->userId);
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Log error
            error_log("Error getting wish list items: " . $e->getMessage());
            return [];
        }
    }
}

/**
 * Product class for managing products.
 */
class Product {
    private $db;

    /**
     * Constructor for Product class.
     * 
     * @param PDO $db Database connection.
     */
    public function __construct(PDO $db) {
        $this->db = $db;
    }

    /**
     * Get all products by category.
     * 
     * @param string $category Category name.
     * 
     * @return array List of products.
     */
    public function getProductsByCategory(string $category): array {
        try {
            $stmt = $this->db->prepare("SELECT * FROM products WHERE category = :category");
            $stmt->bindParam(':category', $category);
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Log error
            error_log("Error getting products by category: " . $e->getMessage());
            return [];
        }
    }
}

// Database connection settings
$host = 'localhost';
$dbname = 'online_store';
$username = 'root';
$password = 'password';

// Create database connection
try {
    $db = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Log error
    error_log("Error connecting to database: " . $e->getMessage());
    exit();
}

// Example usage
$userId = 1;
$wishList = new WishList($db, $userId);
$product = new Product($db);

// Get products by category
$category = "Pompa Apa";
$products = $product->getProductsByCategory($category);

// Add item to wish list
$productId = 1;
$wishList->addItem($productId);

// Get wish list items
$wishListItems = $wishList->getItems();

// Print wish list items
print_r($wishListItems);
```

```sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE wish_list (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO products (name, category, description) VALUES
('Pompa Apa 1', 'Pompa Apa', 'Pompa apa pentru irigatii'),
('Pompa Apa 2', 'Pompa Apa', 'Pompa apa pentru alimentare cu apa'),
('Motocoasa 1', 'Motocoasa', 'Motocoasa pentru taiat iarba'),
('Scule electrice 1', 'Scule electrice', 'Scule electrice pentru lucrari de constructii');
```
