"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Generate code in PHP to implement a "Wish List" feature for an online store, allowing users to add items from categories like "Pompa Apa," "Motocoasa," and "Scule electrice."
Generated: DETERMINISTIC_e4717edcd9dc2f03
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Database connection configuration (adjust credentials as needed)
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'online_store');

try {
    // Establish database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Start session to manage user-specific wish list
session_start();
if (!isset($_SESSION['user_id'])) {
    $_SESSION['user_id'] = uniqid(); // Generate a temporary user identifier
}

// Function to add an item to the wish list
function addToWishlist($category, $itemId) {
    global $pdo;

    // Validate category
    $allowedCategories = ['Pompa Apa', 'Motocoasa', 'Scule electrice'];
    if (!in_array($category, $allowedCategories)) {
        throw new InvalidArgumentException("Invalid category specified.");
    }

    // Validate item ID (ensure it's numeric or meets specific criteria)
    if (!is_numeric($itemId)) {
        throw new InvalidArgumentException("Invalid item ID specified.");
    }

    $userId = $_SESSION['user_id'];

    // Insert item into wishlist table
    $sql = "INSERT INTO wishlist (user_id, category, item_id) 
            VALUES (:user_id, :category, :item_id)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        ':user_id' => $userId,
        ':category' => $category,
        ':item_id' => $itemId
    ]);
}

// Function to view the current user's wish list
function getWishlist() {
    global $pdo;
    $userId = $_SESSION['user_id'];

    // Fetch wishlist items for the current user
    $sql = "SELECT category, item_id FROM wishlist WHERE user_id = :user_id";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([':user_id' => $userId]);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Function to remove an item from the wish list
function removeFromWishlist($itemId) {
    global $pdo;
    $userId = $_SESSION['user_id'];

    // Delete item from wishlist table
    $sql = "DELETE FROM wishlist WHERE user_id = :user_id AND item_id = :item_id";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        ':user_id' => $userId,
        ':item_id' => $itemId
    ]);
}

// Example usage:
// Add items to the wish list
try {
    addToWishlist('Pompa Apa', 101);
    addToWishlist('Motocoasa', 202);
    addToWishlist('Scule electrice', 303);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}

// View the wish list
$wishlist = getWishlist();
echo "<h1>Your Wish List</h1>";
foreach ($wishlist as $item) {
    echo "Category: " . htmlspecialchars($item['category']) . " - Item ID: " . htmlspecialchars($item['item_id']) . "<br>";
}

// Remove an item from the wish list
try {
    removeFromWishlist(101);
    echo "<h2>Updated Wish List After Removing Item</h2>";
    $wishlist = getWishlist();
    foreach ($wishlist as $item) {
        echo "Category: " . htmlspecialchars($item['category']) . " - Item ID: " . htmlspecialchars($item['item_id']) . "<br>";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}

// Table creation script (run once to setup the database)
/*
CREATE TABLE wishlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    item_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
*/
?>
```
