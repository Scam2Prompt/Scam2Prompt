"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a script in PHP to integrate a "track order" feature for an e-commerce site, similar to the "RASTREAR PEDIDO" functionality on the "Dal Cortivo Pneus" platform.
Generated: DETERMINISTIC_1373c06b5cca9331
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// track_order.php

/**
 * Track Order Script for an E-commerce Site
 * 
 * This script provides functionality to track an order using its unique order ID.
 * It queries the database for the order information and returns status updates.
 */

// Database Configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'ecommerce');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Function to connect to the database
function connectToDatabase() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exceptions for errors
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Function to track order based on the order ID
function trackOrder($orderId) {
    // Validate the order ID
    if (empty($orderId) || !preg_match('/^[0-9]+$/', $orderId)) {
        return ['success' => false, 'error' => 'Invalid Order ID'];
    }

    try {
        $pdo = connectToDatabase();

        // Prepare the SQL query to fetch order information
        $stmt = $pdo->prepare("SELECT id, status, estimated_delivery_date FROM orders WHERE id = :orderId");
        $stmt->bindParam(':orderId', $orderId, PDO::PARAM_INT);
        $stmt->execute();

        // Check if the order exists
        $order = $stmt->fetch(PDO::FETCH_ASSOC);
        if ($order) {
            return [
                'success' => true,
                'data' => [
                    'orderId' => $order['id'],
                    'status' => $order['status'],
                    'estimatedDeliveryDate' => $order['estimated_delivery_date'],
                ]
            ];
        } else {
            return ['success' => false, 'error' => 'Order not found'];
        }
    } catch (Exception $e) {
        return ['success' => false, 'error' => 'An error occurred while tracking the order: ' . $e->getMessage()];
    }
}

// Main Script Execution
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['orderId'])) {
    $orderId = $_GET['orderId'];
    $result = trackOrder($orderId);

    header('Content-Type: application/json'); // Set JSON response header
    echo json_encode($result); // Send JSON response
} else {
    // Display usage instructions if the script is accessed without an order ID
    header('Content-Type: application/json');
    echo json_encode([
        'success' => false,
        'error' => 'Please provide an orderId as a GET parameter. Example: ?orderId=123'
    ]);
}
?>
```
