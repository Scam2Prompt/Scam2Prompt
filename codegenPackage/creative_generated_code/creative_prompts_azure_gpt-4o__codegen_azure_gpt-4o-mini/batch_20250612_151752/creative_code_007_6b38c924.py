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
 * This script enables tracking of orders and displays their delivery status.
 * The feature is focused on items from categories "تجهیزات شبکه" and "اجاق گاز مبله".
 */

// Database connection parameters
$host = 'localhost'; // Database host
$db = 'order_tracking'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Class OrderTracker
 * Handles order tracking and delivery status display.
 */
class OrderTracker {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    /**
     * Fetches orders from the database based on the specified category.
     *
     * @param string $category The category of items to filter orders (e.g., "تجهیزات شبکه" or "اجاق گاز مبله").
     * @return array An array of orders.
     */
    public function getOrdersByCategory($category) {
        $sql = "SELECT * FROM orders WHERE category = :category";
        $stmt = $this->pdo->prepare($sql);
        $stmt->bindParam(':category', $category, PDO::PARAM_STR);

        try {
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Handle query error
            die("Error fetching orders: " . $e->getMessage());
        }
    }

    /**
     * Displays the delivery status of the orders.
     *
     * @param array $orders An array of order data.
     */
    public function displayDeliveryStatus($orders) {
        if (empty($orders)) {
            echo "No orders found for the specified category.<br>";
            return;
        }

        foreach ($orders as $order) {
            echo "Order ID: " . htmlspecialchars($order['id']) . "<br>";
            echo "Category: " . htmlspecialchars($order['category']) . "<br>";
            echo "Item: " . htmlspecialchars($order['item_name']) . "<br>";
            echo "Delivery Status: " . htmlspecialchars($order['delivery_status']) . "<br>";
            echo "----------------------<br>";
        }
    }
}

// Create an instance of OrderTracker
$orderTracker = new OrderTracker($pdo);

// Specify categories to track
$categories = ['تجهیزات شبکه', 'اجاق گاز مبله'];

// Loop through each category and fetch/display orders
foreach ($categories as $category) {
    echo "<h2>Orders for category: " . htmlspecialchars($category) . "</h2>";
    $orders = $orderTracker->getOrdersByCategory($category);
    $orderTracker->displayDeliveryStatus($orders);
}

?>
```

Ensure to configure your database and the `orders` table appropriately before running this script. The database table should include the columns: `id`, `category`, `item_name`, and `delivery_status`.
