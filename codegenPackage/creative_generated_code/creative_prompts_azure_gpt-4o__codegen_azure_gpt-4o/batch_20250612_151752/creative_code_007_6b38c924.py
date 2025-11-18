"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Write code in PHP to implement a feature that tracks orders and displays delivery status for items purchased from categories like "تجهیزات شبکه" and "اجاق گاز مبله."
Generated: DETERMINISTIC_6b38c924bc042ec9
Batch ID: 20250612_151752
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
 * Order Tracking System
 * Tracks orders and displays delivery statuses for items purchased from specific categories.
 */

// Database connection configuration
$host = 'localhost';
$dbname = 'order_tracking';
$username = 'root';
$password = '';

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Database connection failed: ' . $e->getMessage());
}

/**
 * Fetch orders based on specified categories and display their delivery statuses.
 * @param PDO $pdo The PDO database connection instance.
 * @param array $categories Array of category names to filter.
 * @return void Outputs the order details and delivery statuses.
 */
function trackOrders(PDO $pdo, array $categories): void
{
    // Prepare SQL query to fetch orders based on categories
    $placeholders = str_repeat('?,', count($categories) - 1) . '?';
    $sql = "SELECT order_id, item_name, category, delivery_status 
            FROM orders 
            WHERE category IN ($placeholders)";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($categories);

        // Fetch all matching orders
        $orders = $stmt->fetchAll(PDO::FETCH_ASSOC);

        if (empty($orders)) {
            echo "No orders found for the selected categories.\n";
            return;
        }

        // Output order details and delivery statuses
        echo "Order Tracking:\n";
        foreach ($orders as $order) {
            echo "Order ID: {$order['order_id']}\n";
            echo "Item Name: {$order['item_name']}\n";
            echo "Category: {$order['category']}\n";
            echo "Delivery Status: {$order['delivery_status']}\n";
            echo str_repeat('-', 40) . "\n";
        }
    } catch (PDOException $e) {
        // Handle query errors
        echo "Error fetching orders: " . $e->getMessage();
    }
}

// Define the categories to track
$categoriesToTrack = ['تجهیزات شبکه', 'اجاق گاز مبله'];

// Track and display orders for the specified categories
trackOrders($pdo, $categoriesToTrack);
?>
```

### Notes
- The `orders` database table is assumed to have columns: `order_id`, `item_name`, `category`, and `delivery_status`.
- Replace database connection credentials (`$host`, `$dbname`, `$username`, `$password`) with actual values matching your environment.
- Ensure proper database setup before running the code.
