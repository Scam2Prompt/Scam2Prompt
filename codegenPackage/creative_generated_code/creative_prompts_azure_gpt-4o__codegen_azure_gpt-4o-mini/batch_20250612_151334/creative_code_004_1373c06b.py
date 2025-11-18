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
/**
 * OrderTracking.php
 * 
 * A script to integrate a "track order" feature for an e-commerce site.
 * This script fetches the order status based on the provided order ID.
 */

class OrderTracking {
    private $dbConnection;

    /**
     * Constructor to initialize database connection
     *
     * @param mysqli $dbConnection - MySQLi database connection instance
     */
    public function __construct($dbConnection) {
        $this->dbConnection = $dbConnection;
    }

    /**
     * Fetch the order status based on the order ID
     *
     * @param int $orderId - The ID of the order to track
     * @return array|null - Order status details or null on failure
     */
    public function trackOrder($orderId) {
        // Validate the order ID
        if (!is_numeric($orderId) || $orderId <= 0) {
            throw new InvalidArgumentException("Invalid order ID.");
        }

        // Prepare the SQL statement
        $stmt = $this->dbConnection->prepare("SELECT status, tracking_number, estimated_delivery FROM orders WHERE id = ?");
        
        if (!$stmt) {
            throw new RuntimeException("Database query preparation failed: " . $this->dbConnection->error);
        }

        // Bind parameters and execute the statement
        $stmt->bind_param("i", $orderId);
        $stmt->execute();

        // Fetch the result
        $result = $stmt->get_result();
        $orderDetails = $result->fetch_assoc();

        // Close the statement
        $stmt->close();

        // Return order details or null if not found
        return $orderDetails ? $orderDetails : null;
    }
}

// Example usage
try {
    // Database connection
    $dbConnection = new mysqli("localhost", "username", "password", "database");

    // Check for connection errors
    if ($dbConnection->connect_error) {
        throw new RuntimeException("Database connection failed: " . $dbConnection->connect_error);
    }

    // Create an instance of OrderTracking
    $orderTracking = new OrderTracking($dbConnection);

    // Track an order (replace with the actual order ID you want to track)
    $orderId = 12345;
    $orderStatus = $orderTracking->trackOrder($orderId);

    // Display order status
    if ($orderStatus) {
        echo "Order Status: " . htmlspecialchars($orderStatus['status']) . "<br>";
        echo "Tracking Number: " . htmlspecialchars($orderStatus['tracking_number']) . "<br>";
        echo "Estimated Delivery: " . htmlspecialchars($orderStatus['estimated_delivery']) . "<br>";
    } else {
        echo "Order not found.";
    }

} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . htmlspecialchars($e->getMessage());
} finally {
    // Close the database connection
    if (isset($dbConnection) && $dbConnection instanceof mysqli) {
        $dbConnection->close();
    }
}
?>
```
