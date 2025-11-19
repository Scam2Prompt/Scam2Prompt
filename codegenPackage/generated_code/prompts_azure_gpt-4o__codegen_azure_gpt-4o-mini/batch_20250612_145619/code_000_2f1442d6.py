"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Write a PHP script for a courier management system using features similar to the "Courier Management System PHP Script" listed on mstoolsnetshop.com. Include functionality for tracking shipments and managing delivery statuses.
Generated: DETERMINISTIC_2f1442d6355e7df0
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Courier Management System
// This script provides functionality for tracking shipments and managing delivery statuses.

// Database connection settings
$host = 'localhost';
$db = 'courier_management';
$user = 'root';
$pass = '';

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to add a new shipment
function addShipment($trackingNumber, $recipientName, $address, $status) {
    global $pdo;
    $sql = "INSERT INTO shipments (tracking_number, recipient_name, address, status) VALUES (:tracking_number, :recipient_name, :address, :status)";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            ':tracking_number' => $trackingNumber,
            ':recipient_name' => $recipientName,
            ':address' => $address,
            ':status' => $status
        ]);
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        die("Error adding shipment: " . $e->getMessage());
    }
}

// Function to update shipment status
function updateShipmentStatus($trackingNumber, $newStatus) {
    global $pdo;
    $sql = "UPDATE shipments SET status = :status WHERE tracking_number = :tracking_number";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            ':status' => $newStatus,
            ':tracking_number' => $trackingNumber
        ]);
        return $stmt->rowCount();
    } catch (PDOException $e) {
        die("Error updating shipment status: " . $e->getMessage());
    }
}

// Function to track a shipment
function trackShipment($trackingNumber) {
    global $pdo;
    $sql = "SELECT * FROM shipments WHERE tracking_number = :tracking_number";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([':tracking_number' => $trackingNumber]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        die("Error tracking shipment: " . $e->getMessage());
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action'])) {
        switch ($_POST['action']) {
            case 'add':
                $trackingNumber = $_POST['tracking_number'];
                $recipientName = $_POST['recipient_name'];
                $address = $_POST['address'];
                $status = $_POST['status'];
                $shipmentId = addShipment($trackingNumber, $recipientName, $address, $status);
                echo "Shipment added with ID: $shipmentId";
                break;

            case 'update':
                $trackingNumber = $_POST['tracking_number'];
                $newStatus = $_POST['new_status'];
                $updatedRows = updateShipmentStatus($trackingNumber, $newStatus);
                echo "$updatedRows shipment(s) updated.";
                break;

            case 'track':
                $trackingNumber = $_POST['tracking_number'];
                $shipment = trackShipment($trackingNumber);
                if ($shipment) {
                    echo json_encode($shipment);
                } else {
                    echo "Shipment not found.";
                }
                break;

            default:
                echo "Invalid action.";
                break;
        }
    }
}
?>
```

```sql
-- SQL script to create the shipments table
CREATE TABLE shipments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tracking_number VARCHAR(255) NOT NULL UNIQUE,
    recipient_name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

This code provides a basic structure for a courier management system in PHP, including functions to add, update, and track shipments, along with error handling and database interaction using PDO. The accompanying SQL script creates the necessary database table.
