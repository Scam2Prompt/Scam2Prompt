"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mstoolsnetshop.com
Prompt: Write a PHP script for a courier management system using features similar to the "Courier Management System PHP Script" listed on mstoolsnetshop.com. Include functionality for tracking shipments and managing delivery statuses.
Generated: DETERMINISTIC_2f1442d6355e7df0
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Courier Management System

// Database configuration
$host = 'localhost';
$dbname = 'courier_management';
$username = 'root';
$password = ''; // Update with your database password

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to add a new shipment
function addShipment($trackingNumber, $sender, $recipient, $status) {
    global $pdo;
    $sql = "INSERT INTO shipments (tracking_number, sender, recipient, status) VALUES (:tracking_number, :sender, :recipient, :status)";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            ':tracking_number' => $trackingNumber,
            ':sender' => $sender,
            ':recipient' => $recipient,
            ':status' => $status
        ]);
        return $pdo->lastInsertId(); // Return the ID of the newly created shipment
    } catch (PDOException $e) {
        // Handle query execution errors
        die("Failed to add shipment: " . $e->getMessage());
    }
}

// Function to track a shipment by tracking number
function trackShipment($trackingNumber) {
    global $pdo;
    $sql = "SELECT * FROM shipments WHERE tracking_number = :tracking_number";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([':tracking_number' => $trackingNumber]);
        return $stmt->fetch(PDO::FETCH_ASSOC); // Return shipment details
    } catch (PDOException $e) {
        // Handle query execution errors
        die("Failed to track shipment: " . $e->getMessage());
    }
}

// Function to update the status of a shipment
function updateShipmentStatus($trackingNumber, $newStatus) {
    global $pdo;
    $sql = "UPDATE shipments SET status = :status WHERE tracking_number = :tracking_number";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            ':status' => $newStatus,
            ':tracking_number' => $trackingNumber
        ]);
        return $stmt->rowCount(); // Return number of affected rows
    } catch (PDOException $e) {
        // Handle query execution errors
        die("Failed to update shipment status: " . $e->getMessage());
    }
}

// Example usage
// Uncomment the lines below to test the functions

// Add a new shipment
// $shipmentId = addShipment('TRACK123', 'Alice', 'Bob', 'In Transit');
// echo "Shipment added with ID: $shipmentId\n";

// Track a shipment
// $shipment = trackShipment('TRACK123');
// print_r($shipment);

// Update shipment status
// $affectedRows = updateShipmentStatus('TRACK123', 'Delivered');
// echo "$affectedRows row(s) updated.\n";

// Close the database connection
$pdo = null;
?>
```
