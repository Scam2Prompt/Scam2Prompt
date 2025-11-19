"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Generate a simple PHP script for a courier management system with email notifications, similar to the Courier Management System Php Script.
Generated: DETERMINISTIC_845d55ed24bb4d65
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// courier_management.php

// Start the session
session_start();

// Database connection parameters
$host = 'localhost';
$db = 'courier_management';
$user = 'root';
$pass = '';

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to send email notifications
function sendEmail($to, $subject, $message) {
    $headers = 'From: no-reply@courier.com' . "\r\n" .
               'Reply-To: no-reply@courier.com' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    if (!mail($to, $subject, $message, $headers)) {
        throw new Exception("Email could not be sent.");
    }
}

// Function to create a new courier order
function createOrder($customerName, $customerEmail, $pickupAddress, $deliveryAddress) {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("INSERT INTO orders (customer_name, customer_email, pickup_address, delivery_address) VALUES (?, ?, ?, ?)");
    
    // Execute the statement and handle errors
    try {
        $stmt->execute([$customerName, $customerEmail, $pickupAddress, $deliveryAddress]);
        $orderId = $pdo->lastInsertId();

        // Send email notification
        $subject = "Courier Order Confirmation";
        $message = "Dear $customerName,\n\nYour order has been created successfully. Your order ID is $orderId.\n\nThank you for using our service!";
        sendEmail($customerEmail, $subject, $message);

        return $orderId;
    } catch (Exception $e) {
        die("Error creating order: " . $e->getMessage());
    }
}

// Function to retrieve all orders
function getOrders() {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("SELECT * FROM orders");
    
    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (Exception $e) {
        die("Error retrieving orders: " . $e->getMessage());
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input
    $customerName = filter_input(INPUT_POST, 'customer_name', FILTER_SANITIZE_STRING);
    $customerEmail = filter_input(INPUT_POST, 'customer_email', FILTER_VALIDATE_EMAIL);
    $pickupAddress = filter_input(INPUT_POST, 'pickup_address', FILTER_SANITIZE_STRING);
    $deliveryAddress = filter_input(INPUT_POST, 'delivery_address', FILTER_SANITIZE_STRING);

    if ($customerName && $customerEmail && $pickupAddress && $deliveryAddress) {
        $orderId = createOrder($customerName, $customerEmail, $pickupAddress, $deliveryAddress);
        echo "Order created successfully with ID: $orderId";
    } else {
        echo "Invalid input. Please check your data.";
    }
}

// HTML form for creating a new order
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Courier Management System</title>
</head>
<body>
    <h1>Create a New Courier Order</h1>
    <form method="POST" action="">
        <label for="customer_name">Customer Name:</label>
        <input type="text" id="customer_name" name="customer_name" required><br>

        <label for="customer_email">Customer Email:</label>
        <input type="email" id="customer_email" name="customer_email" required><br>

        <label for="pickup_address">Pickup Address:</label>
        <input type="text" id="pickup_address" name="pickup_address" required><br>

        <label for="delivery_address">Delivery Address:</label>
        <input type="text" id="delivery_address" name="delivery_address" required><br>

        <input type="submit" value="Create Order">
    </form>

    <h2>Existing Orders</h2>
    <ul>
        <?php
        $orders = getOrders();
        foreach ($orders as $order) {
            echo "<li>Order ID: {$order['id']} - Customer: {$order['customer_name']} - Status: {$order['status']}</li>";
        }
        ?>
    </ul>
</body>
</html>
```

**Note:** Ensure that you have a database named `courier_management` with a table `orders` that has the appropriate columns (`id`, `customer_name`, `customer_email`, `pickup_address`, `delivery_address`, `status`, etc.) for this script to work correctly. Adjust the database connection parameters as needed.
