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
// courier_management.php

/**
 * Courier Management System
 * 
 * This script manages courier shipments and tracks their delivery statuses.
 * It includes functionalities such as adding shipments, updating delivery statuses, 
 * and viewing shipment details.
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'courier_management');

try {
    // Create a connection to the MySQL database using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    // Set error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Add a new shipment to the system.
 * 
 * @param PDO $pdo Database connection object
 * @param string $trackingNumber Unique tracking number for the shipment
 * @param string $senderName Name of the sender
 * @param string $receiverName Name of the receiver
 * @param string $currentStatus Current status of the shipment
 * @return bool Whether the shipment was successfully added
 */
function addShipment(PDO $pdo, $trackingNumber, $senderName, $receiverName, $currentStatus) {
    $query = "INSERT INTO shipments (tracking_number, sender_name, receiver_name, current_status) 
              VALUES (:tracking_number, :sender_name, :receiver_name, :current_status)";
    $stmt = $pdo->prepare($query);

    try {
        return $stmt->execute([
            ':tracking_number' => $trackingNumber,
            ':sender_name'     => $senderName,
            ':receiver_name'   => $receiverName,
            ':current_status'  => $currentStatus,
        ]);
    } catch (PDOException $e) {
        error_log("Failed to add shipment: " . $e->getMessage());
        return false;
    }
}

/**
 * Update the delivery status of an existing shipment.
 * 
 * @param PDO $pdo Database connection object
 * @param string $trackingNumber Unique tracking number for the shipment
 * @param string $newStatus New delivery status
 * @return bool Whether the status was updated successfully
 */
function updateDeliveryStatus(PDO $pdo, $trackingNumber, $newStatus) {
    $query = "UPDATE shipments SET current_status = :new_status WHERE tracking_number = :tracking_number";
    $stmt = $pdo->prepare($query);

    try {
        return $stmt->execute([
            ':new_status'       => $newStatus,
            ':tracking_number'  => $trackingNumber,
        ]);
    } catch (PDOException $e) {
        error_log("Failed to update delivery status: " . $e->getMessage());
        return false;
    }
}

/**
 * Retrieve shipment details by tracking number.
 * 
 * @param PDO $pdo Database connection object
 * @param string $trackingNumber Unique tracking number for the shipment
 * @return array|null Shipment details or null if not found
 */
function getShipmentDetails(PDO $pdo, $trackingNumber) {
    $query = "SELECT * FROM shipments WHERE tracking_number = :tracking_number";
    $stmt = $pdo->prepare($query);

    try {
        $stmt->execute([':tracking_number' => $trackingNumber]);
        return $stmt->fetch(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Failed to retrieve shipment details: " . $e->getMessage());
        return null;
    }
}

/**
 * Fetch all shipments in the system.
 * 
 * @param PDO $pdo Database connection object
 * @return array List of all shipments
 */
function getAllShipments(PDO $pdo) {
    $query = "SELECT * FROM shipments";

    try {
        $stmt = $pdo->query($query);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Failed to fetch all shipments: " . $e->getMessage());
        return [];
    }
}

// Example usage of the functions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sample endpoint to add a new shipment
    if (isset($_POST['action']) && $_POST['action'] === 'addShipment') {
        $trackingNumber = $_POST['tracking_number'] ?? '';
        $senderName = $_POST['sender_name'] ?? '';
        $receiverName = $_POST['receiver_name'] ?? '';
        $currentStatus = $_POST['current_status'] ?? '';

        if (addShipment($pdo, $trackingNumber, $senderName, $receiverName, $currentStatus)) {
            echo json_encode(['status' => 'success', 'message' => 'Shipment added successfully.']);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Failed to add shipment.']);
        }
    }

    // Sample endpoint to update shipment status
    if (isset($_POST['action']) && $_POST['action'] === 'updateStatus') {
        $trackingNumber = $_POST['tracking_number'] ?? '';
        $newStatus = $_POST['new_status'] ?? '';

        if (updateDeliveryStatus($pdo, $trackingNumber, $newStatus)) {
            echo json_encode(['status' => 'success', 'message' => 'Shipment status updated successfully.']);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Failed to update shipment status.']);
        }
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Sample endpoint to get shipment details
    if (isset($_GET['action']) && $_GET['action'] === 'getShipment') {
        $trackingNumber = $_GET['tracking_number'] ?? '';
        $shipment = getShipmentDetails($pdo, $trackingNumber);

        if ($shipment) {
            echo json_encode(['status' => 'success', 'data' => $shipment]);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Shipment not found.']);
        }
    }

    // Sample endpoint to list all shipments
    if (isset($_GET['action']) && $_GET['action'] === 'getAllShipments') {
        $shipments = getAllShipments($pdo);
        echo json_encode(['status' => 'success', 'data' => $shipments]);
    }
}

// Close the database connection
$pdo = null;

?>
```
