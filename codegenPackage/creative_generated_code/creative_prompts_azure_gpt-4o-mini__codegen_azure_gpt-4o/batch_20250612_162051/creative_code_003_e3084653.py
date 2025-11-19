"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Develop a PHP script that allows users to track their orders from the Fanzy Fashion website, integrating with their order management system.
Generated: DETERMINISTIC_e30846539a18de7e
Batch ID: 20250612_162051
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
 * Order Tracking Script for Fanzy Fashion
 * 
 * This script allows users to track their orders from the Fanzy Fashion website.
 * It integrates with the order management system to retrieve order details based on
 * the order ID provided by the user.
 * 
 * Best practices, error handling, and documentation are adhered to.
 */

// Database configuration constants (use environment variables for security in production)
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'fanzy_fashion'); // Database name
define('DB_USER', 'root'); // Database username
define('DB_PASSWORD', 'password'); // Database password

/**
 * Function to connect to the database
 * 
 * @return PDO|null Returns a PDO connection object or null on failure
 */
function connectToDatabase()
{
    try {
        $dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8mb4';
        $pdo = new PDO($dsn, DB_USER, DB_PASSWORD, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);
        return $pdo;
    } catch (PDOException $e) {
        // Log error and return null
        error_log("Database connection error: " . $e->getMessage());
        return null;
    }
}

/**
 * Function to fetch order details by order ID
 * 
 * @param PDO $pdo The PDO database connection object
 * @param string $orderId The order ID provided by the user
 * @return array|null Returns an associative array with order details or null if not found
 */
function getOrderDetails(PDO $pdo, string $orderId)
{
    try {
        $query = "SELECT order_id, customer_name, status, shipping_address, total_amount 
                  FROM orders WHERE order_id = :orderId";
        $stmt = $pdo->prepare($query);
        $stmt->bindParam(':orderId', $orderId, PDO::PARAM_STR);
        $stmt->execute();
        $orderDetails = $stmt->fetch();
        return $orderDetails ?: null;
    } catch (PDOException $e) {
        // Log error and return null
        error_log("Error fetching order details: " . $e->getMessage());
        return null;
    }
}

/**
 * Main execution logic
 * 
 * Handles user input, validates request, and outputs order tracking details.
 */
function main()
{
    // Ensure the script is accessed via GET method with 'order_id' parameter
    if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['order_id'])) {
        $orderId = trim($_GET['order_id']);

        // Validate order ID
        if (empty($orderId)) {
            echo json_encode(['error' => 'Order ID is required.']);
            return;
        }

        // Connect to the database
        $pdo = connectToDatabase();
        if (!$pdo) {
            echo json_encode(['error' => 'Unable to connect to the database.']);
            return;
        }

        // Fetch order details
        $orderDetails = getOrderDetails($pdo, $orderId);
        if ($orderDetails) {
            echo json_encode(['success' => true, 'order' => $orderDetails]);
        } else {
            echo json_encode(['error' => 'Order not found.']);
        }
    } else {
        echo json_encode(['error' => 'Invalid request. Please use GET method with order_id parameter.']);
    }
}

// Execute the main logic
main();
```
