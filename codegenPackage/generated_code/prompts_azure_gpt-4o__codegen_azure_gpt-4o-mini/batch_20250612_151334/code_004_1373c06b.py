"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a script in PHP to integrate a "track order" feature for an e-commerce site, similar to the "RASTREAR PEDIDO" functionality on the "Dal Cortivo Pneus" platform.
Generated: DETERMINISTIC_1373c06b5cca9331
Batch ID: 20250612_151334
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
 * Order Tracking Script for E-commerce Platform
 * This script allows users to track their orders using a unique order ID.
 */

// Database connection parameters
$host = 'localhost'; // Database host
$db = 'ecommerce'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to track an order by its ID
 *
 * @param string $orderId The unique order ID to track
 * @return array|null The order details or null if not found
 */
function trackOrder($orderId) {
    global $pdo;

    // Prepare the SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT * FROM orders WHERE order_id = :orderId");
    $stmt->bindParam(':orderId', $orderId);

    // Execute the statement
    $stmt->execute();

    // Fetch the order details
    return $stmt->fetch(PDO::FETCH_ASSOC);
}

// Check if the order ID is provided via GET request
if (isset($_GET['order_id'])) {
    $orderId = trim($_GET['order_id']);

    // Validate the order ID
    if (empty($orderId)) {
        echo json_encode(['error' => 'Order ID cannot be empty.']);
        exit;
    }

    // Track the order
    $orderDetails = trackOrder($orderId);

    // Check if the order was found
    if ($orderDetails) {
        // Return order details as JSON
        echo json_encode(['success' => true, 'order' => $orderDetails]);
    } else {
        // Return error if order not found
        echo json_encode(['success' => false, 'error' => 'Order not found.']);
    }
} else {
    // Return error if order ID is not provided
    echo json_encode(['error' => 'No order ID provided.']);
}
?>
```
