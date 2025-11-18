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
// Database connection parameters
$host = 'localhost'; // Database host
$db = 'online_store'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die('Connection failed: ' . $e->getMessage());
}

/**
 * Class WishList
 * Handles the wish list operations for users.
 */
class WishList {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    /**
     * Add an item to the user's wish list
     *
     * @param int $userId The ID of the user
     * @param int $itemId The ID of the item to add
     * @return bool Returns true on success, false on failure
     */
    public function addItem($userId, $itemId) {
        try {
            $stmt = $this->pdo->prepare("INSERT INTO wish_list (user_id, item_id) VALUES (:user_id, :item_id)");
            $stmt->bindParam(':user_id', $userId);
            $stmt->bindParam(':item_id', $itemId);
            return $stmt->execute();
        } catch (PDOException $e) {
            // Handle query errors
            error_log('Error adding item to wish list: ' . $e->getMessage());
            return false;
        }
    }

    /**
     * Retrieve the user's wish list
     *
     * @param int $userId The ID of the user
     * @return array Returns an array of items in the wish list
     */
    public function getWishList($userId) {
        try {
            $stmt = $this->pdo->prepare("SELECT * FROM wish_list WHERE user_id = :user_id");
            $stmt->bindParam(':user_id', $userId);
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Handle query errors
            error_log('Error retrieving wish list: ' . $e->getMessage());
            return [];
        }
    }

    /**
     * Remove an item from the user's wish list
     *
     * @param int $userId The ID of the user
     * @param int $itemId The ID of the item to remove
     * @return bool Returns true on success, false on failure
     */
    public function removeItem($userId, $itemId) {
        try {
            $stmt = $this->pdo->prepare("DELETE FROM wish_list WHERE user_id = :user_id AND item_id = :item_id");
            $stmt->bindParam(':user_id', $userId);
            $stmt->bindParam(':item_id', $itemId);
            return $stmt->execute();
        } catch (PDOException $e) {
            // Handle query errors
            error_log('Error removing item from wish list: ' . $e->getMessage());
            return false;
        }
    }
}

// Example usage
$wishList = new WishList($pdo);
$userId = 1; // Example user ID
$itemId = 101; // Example item ID

// Add item to wish list
if ($wishList->addItem($userId, $itemId)) {
    echo "Item added to wish list successfully.";
} else {
    echo "Failed to add item to wish list.";
}

// Retrieve and display user's wish list
$items = $wishList->getWishList($userId);
foreach ($items as $item) {
    echo "Item ID: " . $item['item_id'] . "\n";
}

// Remove item from wish list
if ($wishList->removeItem($userId, $itemId)) {
    echo "Item removed from wish list successfully.";
} else {
    echo "Failed to remove item from wish list.";
}
?>
```

**Note:** Ensure that you have a database with a table named `wish_list` with columns `user_id` and `item_id`. Adjust database connection parameters according to your setup.
