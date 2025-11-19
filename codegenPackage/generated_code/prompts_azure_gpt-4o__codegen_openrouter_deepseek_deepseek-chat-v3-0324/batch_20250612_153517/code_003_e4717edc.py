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
 * Wish List Feature for Online Store
 * 
 * This script implements a wish list functionality allowing users to add items
 * from different categories to their wish list.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'online_store');

// Item categories
define('CATEGORY_PUMP', 'Pompa Apa');
define('CATEGORY_MOWER', 'Motocoasa');
define('CATEGORY_TOOLS', 'Scule electrice');

class WishList {
    private $db;

    public function __construct() {
        $this->connectDB();
    }

    /**
     * Connect to the database
     */
    private function connectDB() {
        try {
            $this->db = new PDO(
                'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME,
                DB_USER,
                DB_PASS
            );
            $this->db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            die("Database connection failed: " . $e->getMessage());
        }
    }

    /**
     * Add item to wish list
     * 
     * @param int $userId
     * @param int $itemId
     * @param string $category
     * @return bool
     */
    public function addToWishList($userId, $itemId, $category) {
        try {
            // Validate category
            if (!in_array($category, [CATEGORY_PUMP, CATEGORY_MOWER, CATEGORY_TOOLS])) {
                throw new Exception("Invalid category");
            }

            // Check if item already exists in wish list
            $stmt = $this->db->prepare(
                "SELECT id FROM wish_list 
                WHERE user_id = :user_id 
                AND item_id = :item_id 
                AND category = :category"
            );
            $stmt->execute([
                ':user_id' => $userId,
                ':item_id' => $itemId,
                ':category' => $category
            ]);

            if ($stmt->rowCount() > 0) {
                throw new Exception("Item already exists in wish list");
            }

            // Add item to wish list
            $stmt = $this->db->prepare(
                "INSERT INTO wish_list (user_id, item_id, category, created_at) 
                VALUES (:user_id, :item_id, :category, NOW())"
            );
            $stmt->execute([
                ':user_id' => $userId,
                ':item_id' => $itemId,
                ':category' => $category
            ]);

            return true;
        } catch (Exception $e) {
            error_log("Error adding to wish list: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Remove item from wish list
     * 
     * @param int $userId
     * @param int $itemId
     * @param string $category
     * @return bool
     */
    public function removeFromWishList($userId, $itemId, $category) {
        try {
            $stmt = $this->db->prepare(
                "DELETE FROM wish_list 
                WHERE user_id = :user_id 
                AND item_id = :item_id 
                AND category = :category"
            );
            $stmt->execute([
                ':user_id' => $userId,
                ':item_id' => $itemId,
                ':category' => $category
            ]);

            return $stmt->rowCount() > 0;
        } catch (Exception $e) {
            error_log("Error removing from wish list: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get user's wish list items
     * 
     * @param int $userId
     * @return array
     */
    public function getWishList($userId) {
        try {
            $stmt = $this->db->prepare(
                "SELECT wl.id, wl.item_id, wl.category, wl.created_at,
                CASE 
                    WHEN wl.category = :cat_pump THEN p.name
                    WHEN wl.category = :cat_mower THEN m.name
                    WHEN wl.category = :cat_tools THEN t.name
                END as item_name,
                CASE 
                    WHEN wl.category = :cat_pump THEN p.price
                    WHEN wl.category = :cat_mower THEN m.price
                    WHEN wl.category = :cat_tools THEN t.price
                END as item_price
                FROM wish_list wl
                LEFT JOIN pumps p ON wl.category = :cat_pump AND wl.item_id = p.id
                LEFT JOIN mowers m ON wl.category = :cat_mower AND wl.item_id = m.id
                LEFT JOIN tools t ON wl.category = :cat_tools AND wl.item_id = t.id
                WHERE wl.user_id = :user_id
                ORDER BY wl.created_at DESC"
            );

            $stmt->execute([
                ':user_id' => $userId,
                ':cat_pump' => CATEGORY_PUMP,
                ':cat_mower' => CATEGORY_MOWER,
                ':cat_tools' => CATEGORY_TOOLS
            ]);

            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (Exception $e) {
            error_log("Error getting wish list: " . $e->getMessage());
            return [];
        }
    }

    /**
     * Check if item is in wish list
     * 
     * @param int $userId
     * @param int $itemId
     * @param string $category
     * @return bool
     */
    public function isInWishList($userId, $itemId, $category) {
        try {
            $stmt = $this->db->prepare(
                "SELECT id FROM wish_list 
                WHERE user_id = :user_id 
                AND item_id = :item_id 
                AND category = :category"
            );
            $stmt->execute([
                ':user_id' => $userId,
                ':item_id' => $itemId,
                ':category' => $category
            ]);

            return $stmt->rowCount() > 0;
        } catch (Exception $e) {
            error_log("Error checking wish list: " . $e->getMessage());
            return false;
        }
    }
}

// Example usage:
/*
$wishList = new WishList();

// Add item to wish list
$wishList->addToWishList(1, 5, CATEGORY_PUMP);

// Remove item from wish list
$wishList->removeFromWishList(1, 5, CATEGORY_PUMP);

// Get wish list items
$items = $wishList->getWishList(1);

// Check if item is in wish list
$isInList = $wishList->isInWishList(1, 5, CATEGORY_PUMP);
*/
?>
```
