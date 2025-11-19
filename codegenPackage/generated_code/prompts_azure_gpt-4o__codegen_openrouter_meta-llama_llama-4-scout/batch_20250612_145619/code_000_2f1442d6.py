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

// Configuration
$db_host = 'localhost';
$db_username = 'root';
$db_password = '';
$db_name = 'courier_management';

// Create connection
$conn = new mysqli($db_host, $db_username, $db_password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Create table for shipments
$sql = "
CREATE TABLE IF NOT EXISTS shipments (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    tracking_number VARCHAR(255) NOT NULL,
    sender_name VARCHAR(255) NOT NULL,
    sender_address VARCHAR(255) NOT NULL,
    receiver_name VARCHAR(255) NOT NULL,
    receiver_address VARCHAR(255) NOT NULL,
    package_description VARCHAR(255) NOT NULL,
    delivery_status VARCHAR(50) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";

// Execute table creation
if (!$conn->query($sql)) {
    die("Error creating table: " . $conn->error);
}

// Create table for delivery updates
$sql = "
CREATE TABLE IF NOT EXISTS delivery_updates (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    shipment_id INT(6) UNSIGNED NOT NULL,
    update_status VARCHAR(50) NOT NULL,
    update_description VARCHAR(255) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shipment_id) REFERENCES shipments(id)
)";

// Execute table creation
if (!$conn->query($sql)) {
    die("Error creating table: " . $conn->error);
}

// Close connection
$conn->close();

// Courier Management System Class
class CourierManagementSystem {
    private $conn;

    public function __construct($db_host, $db_username, $db_password, $db_name) {
        $this->conn = new mysqli($db_host, $db_username, $db_password, $db_name);

        if ($this->conn->connect_error) {
            die("Connection failed: " . $this->conn->connect_error);
        }
    }

    // Add new shipment
    public function addShipment($tracking_number, $sender_name, $sender_address, $receiver_name, $receiver_address, $package_description) {
        $sql = "
            INSERT INTO shipments (tracking_number, sender_name, sender_address, receiver_name, receiver_address, package_description)
            VALUES (?, ?, ?, ?, ?, ?)
        ";

        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("ssssss", $tracking_number, $sender_name, $sender_address, $receiver_name, $receiver_address, $package_description);

        if (!$stmt->execute()) {
            die("Error adding shipment: " . $stmt->error);
        }

        $stmt->close();
    }

    // Update delivery status
    public function updateDeliveryStatus($shipment_id, $update_status, $update_description) {
        $sql = "
            UPDATE shipments
            SET delivery_status = ?
            WHERE id = ?
        ";

        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("si", $update_status, $shipment_id);

        if (!$stmt->execute()) {
            die("Error updating delivery status: " . $stmt->error);
        }

        $sql = "
            INSERT INTO delivery_updates (shipment_id, update_status, update_description)
            VALUES (?, ?, ?)
        ";

        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("iss", $shipment_id, $update_status, $update_description);

        if (!$stmt->execute()) {
            die("Error adding delivery update: " . $stmt->error);
        }

        $stmt->close();
    }

    // Get shipment details
    public function getShipmentDetails($shipment_id) {
        $sql = "
            SELECT * FROM shipments
            WHERE id = ?
        ";

        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("i", $shipment_id);

        if (!$stmt->execute()) {
            die("Error retrieving shipment details: " . $stmt->error);
        }

        $result = $stmt->get_result();
        $shipment_details = $result->fetch_assoc();

        $stmt->close();

        return $shipment_details;
    }

    // Get delivery updates
    public function getDeliveryUpdates($shipment_id) {
        $sql = "
            SELECT * FROM delivery_updates
            WHERE shipment_id = ?
            ORDER BY updated_at DESC
        ";

        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("i", $shipment_id);

        if (!$stmt->execute()) {
            die("Error retrieving delivery updates: " . $stmt->error);
        }

        $result = $stmt->get_result();
        $delivery_updates = $result->fetch_all(MYSQLI_ASSOC);

        $stmt->close();

        return $delivery_updates;
    }

    // Close connection
    public function closeConnection() {
        $this->conn->close();
    }
}

// Example usage
$courier_management_system = new CourierManagementSystem($db_host, $db_username, $db_password, $db_name);

// Add new shipment
$courier_management_system->addShipment(
    'TRK12345',
    'John Doe',
    '123 Main St',
    'Jane Doe',
    '456 Elm St',
    'Package contents'
);

// Update delivery status
$courier_management_system->updateDeliveryStatus(1, 'in_transit', 'Shipment is in transit');

// Get shipment details
$shipment_details = $courier_management_system->getShipmentDetails(1);
print_r($shipment_details);

// Get delivery updates
$delivery_updates = $courier_management_system->getDeliveryUpdates(1);
print_r($delivery_updates);

// Close connection
$courier_management_system->closeConnection();
```
