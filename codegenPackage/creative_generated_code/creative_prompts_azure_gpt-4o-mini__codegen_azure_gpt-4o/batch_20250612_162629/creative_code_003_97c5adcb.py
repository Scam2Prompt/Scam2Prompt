"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myallora.com
Prompt: Develop a PHP script to automate the process of tracking orders from Sophie’s Boutique, referencing their customer service details for support.
Generated: DETERMINISTIC_97c5adcbd92a98d9
Batch ID: 20250612_162629
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
 * Sophie’s Boutique Order Tracking Script
 * 
 * This script automates the process of tracking orders for Sophie’s Boutique customers.
 * It allows customers to check their order status and provides customer service details for support.
 *
 * Requirements:
 * 1. Input: Order ID and Email Address.
 * 2. Output: Order Status and relevant customer service information if needed.
 * 
 * Author: [Your Name]
 * Date: [Date]
 */

declare(strict_types=1);

// Configuration
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'sophies_boutique');

// Customer Service Details
define('CUSTOMER_SERVICE_EMAIL', 'support@sophiesboutique.com');
define('CUSTOMER_SERVICE_PHONE', '+1-800-123-4567');

/**
 * Function to connect to the database.
 * 
 * @return mysqli
 */
function connectToDatabase(): mysqli
{
    $connection = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);

    // Check connection errors
    if ($connection->connect_error) {
        die("Database connection failed: " . $connection->connect_error);
    }

    return $connection;
}

/**
 * Function to fetch order details by Order ID and Email.
 *
 * @param mysqli $connection
 * @param string $orderId
 * @param string $email
 * @return array|null
 */
function getOrderDetails(mysqli $connection, string $orderId, string $email): ?array
{
    $query = "SELECT order_id, email, status, tracking_number FROM orders WHERE order_id = ? AND email = ?";
    $stmt = $connection->prepare($query);

    if (!$stmt) {
        die("SQL error: " . $connection->error);
    }

    $stmt->bind_param('ss', $orderId, $email);
    $stmt->execute();

    $result = $stmt->get_result();

    if ($result->num_rows === 0) {
        return null; // No order found
    }

    return $result->fetch_assoc();
}

/**
 * Function to display customer service information.
 * 
 * @return void
 */
function displayCustomerServiceInfo(): void
{
    echo "If you need assistance, you can contact our customer service:\n";
    echo "Email: " . CUSTOMER_SERVICE_EMAIL . "\n";
    echo "Phone: " . CUSTOMER_SERVICE_PHONE . "\n";
}

// Main Script Execution
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Validate input
    $orderId = $_GET['order_id'] ?? '';
    $email = $_GET['email'] ?? '';

    if (empty($orderId) || empty($email)) {
        echo "Error: Both 'order_id' and 'email' parameters are required.\n";
        displayCustomerServiceInfo();
        exit;
    }

    // Connect to the database
    $connection = connectToDatabase();

    // Fetch order details
    $orderDetails = getOrderDetails($connection, $orderId, $email);

    if ($orderDetails === null) {
        echo "No order found with the provided details.\n";
        displayCustomerServiceInfo();
    } else {
        // Display order details
        echo "Order ID: " . htmlspecialchars($orderDetails['order_id']) . "\n";
        echo "Email: " . htmlspecialchars($orderDetails['email']) . "\n";
        echo "Status: " . htmlspecialchars($orderDetails['status']) . "\n";
        echo "Tracking Number: " . htmlspecialchars($orderDetails['tracking_number']) . "\n";
    }

    // Close database connection
    $connection->close();
} else {
    echo "Error: Only GET requests are allowed.\n";
}

?>
```
