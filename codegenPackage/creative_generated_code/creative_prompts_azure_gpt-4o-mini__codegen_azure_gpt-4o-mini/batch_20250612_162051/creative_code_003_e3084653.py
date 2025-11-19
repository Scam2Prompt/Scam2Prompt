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
 * This script allows users to track their orders by providing their order ID.
 * It integrates with the order management system to fetch and display order details.
 * 
 * PHP Version: 7.4 or higher
 */

header("Content-Type: application/json");

// Database connection parameters
$host = 'localhost';
$db = 'fanzy_fashion';
$user = 'root';
$pass = 'password'; // Replace with your actual password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit;
}

// Check if the order ID is set in the request
if (!isset($_GET['order_id']) || empty($_GET['order_id'])) {
    echo json_encode(['error' => 'Order ID is required.']);
    exit;
}

$order_id = htmlspecialchars(trim($_GET['order_id'])); // Sanitize input

// Prepare and execute the SQL statement to fetch order details
try {
    $stmt = $pdo->prepare("SELECT * FROM orders WHERE order_id = :order_id");
    $stmt->bindParam(':order_id', $order_id, PDO::PARAM_STR);
    $stmt->execute();

    // Fetch the order details
    $order = $stmt->fetch(PDO::FETCH_ASSOC);

    // Check if the order exists
    if ($order) {
        echo json_encode(['success' => true, 'order' => $order]);
    } else {
        echo json_encode(['success' => false, 'error' => 'Order not found.']);
    }
} catch (PDOException $e) {
    // Handle SQL query error
    echo json_encode(['error' => 'Query failed: ' . $e->getMessage()]);
} finally {
    // Close the database connection
    $pdo = null;
}
?>
```
