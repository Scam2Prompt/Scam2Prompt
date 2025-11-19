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
/**
 * Courier Management System
 * 
 * This script provides functionality for managing courier shipments,
 * tracking deliveries, and updating delivery statuses.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'courier_management');

// Establish database connection
try {
    $conn = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

/**
 * Class CourierManagement
 * Handles all courier management operations
 */
class CourierManagement {
    private $conn;

    public function __construct($conn) {
        $this->conn = $conn;
    }

    /**
     * Add new shipment to the system
     * 
     * @param array $shipmentData
     * @return bool|string
     */
    public function addShipment($shipmentData) {
        try {
            $stmt = $this->conn->prepare("INSERT INTO shipments 
                (tracking_number, sender_name, sender_address, sender_phone, 
                receiver_name, receiver_address, receiver_phone, 
                package_description, weight, shipping_date, expected_delivery_date, 
                shipping_cost, status) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
            
            $status = $shipmentData['status'] ?? 'Processing';
            
            $stmt->execute([
                $this->generateTrackingNumber(),
                $shipmentData['sender_name'],
                $shipmentData['sender_address'],
                $shipmentData['sender_phone'],
                $shipmentData['receiver_name'],
                $shipmentData['receiver_address'],
                $shipmentData['receiver_phone'],
                $shipmentData['package_description'],
                $shipmentData['weight'],
                $shipmentData['shipping_date'],
                $shipmentData['expected_delivery_date'],
                $shipmentData['shipping_cost'],
                $status
            ]);
            
            return $this->conn->lastInsertId();
        } catch(PDOException $e) {
            error_log("Error adding shipment: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Generate unique tracking number
     * 
     * @return string
     */
    private function generateTrackingNumber() {
        return 'CMS' . date('Ymd') . strtoupper(substr(uniqid(), -6));
    }

    /**
     * Update shipment status
     * 
     * @param string $trackingNumber
     * @param string $newStatus
     * @return bool
     */
    public function updateStatus($trackingNumber, $newStatus) {
        try {
            $stmt = $this->conn->prepare("UPDATE shipments SET status = ? WHERE tracking_number = ?");
            return $stmt->execute([$newStatus, $trackingNumber]);
        } catch(PDOException $e) {
            error_log("Error updating status: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get shipment details by tracking number
     * 
     * @param string $trackingNumber
     * @return array|bool
     */
    public function trackShipment($trackingNumber) {
        try {
            $stmt = $this->conn->prepare("SELECT * FROM shipments WHERE tracking_number = ?");
            $stmt->execute([$trackingNumber]);
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch(PDOException $e) {
            error_log("Error tracking shipment: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get all shipments with optional filters
     * 
     * @param array $filters
     * @return array|bool
     */
    public function getAllShipments($filters = []) {
        try {
            $query = "SELECT * FROM shipments WHERE 1=1";
            $params = [];
            
            if (!empty($filters['status'])) {
                $query .= " AND status = ?";
                $params[] = $filters['status'];
            }
            
            if (!empty($filters['date_from'])) {
                $query .= " AND shipping_date >= ?";
                $params[] = $filters['date_from'];
            }
            
            if (!empty($filters['date_to'])) {
                $query .= " AND shipping_date <= ?";
                $params[] = $filters['date_to'];
            }
            
            $stmt = $this->conn->prepare($query);
            $stmt->execute($params);
            
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch(PDOException $e) {
            error_log("Error getting shipments: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Add status history for a shipment
     * 
     * @param string $trackingNumber
     * @param string $status
     * @param string $notes
     * @return bool
     */
    public function addStatusHistory($trackingNumber, $status, $notes = '') {
        try {
            $stmt = $this->conn->prepare("INSERT INTO status_history 
                (tracking_number, status, status_date, notes) 
                VALUES (?, ?, NOW(), ?)");
            return $stmt->execute([$trackingNumber, $status, $notes]);
        } catch(PDOException $e) {
            error_log("Error adding status history: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get status history for a shipment
     * 
     * @param string $trackingNumber
     * @return array|bool
     */
    public function getStatusHistory($trackingNumber) {
        try {
            $stmt = $this->conn->prepare("SELECT * FROM status_history 
                WHERE tracking_number = ? ORDER BY status_date DESC");
            $stmt->execute([$trackingNumber]);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch(PDOException $e) {
            error_log("Error getting status history: " . $e->getMessage());
            return false;
        }
    }
}

// Example usage
$courierSystem = new CourierManagement($conn);

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action'])) {
        try {
            switch ($_POST['action']) {
                case 'add_shipment':
                    $shipmentId = $courierSystem->addShipment($_POST);
                    if ($shipmentId) {
                        $courierSystem->addStatusHistory(
                            $courierSystem->generateTrackingNumber(), 
                            'Processing',
                            'Shipment created'
                        );
                        echo json_encode(['success' => true, 'tracking_number' => $shipmentId]);
                    } else {
                        echo json_encode(['success' => false, 'error' => 'Failed to add shipment']);
                    }
                    break;
                    
                case 'update_status':
                    if ($courierSystem->updateStatus($_POST['tracking_number'], $_POST['new_status'])) {
                        $courierSystem->addStatusHistory(
                            $_POST['tracking_number'], 
                            $_POST['new_status'],
                            $_POST['notes'] ?? ''
                        );
                        echo json_encode(['success' => true]);
                    } else {
                        echo json_encode(['success' => false, 'error' => 'Failed to update status']);
                    }
                    break;
                    
                case 'track_shipment':
                    $shipment = $courierSystem->trackShipment($_POST['tracking_number']);
                    if ($shipment) {
                        $history = $courierSystem->getStatusHistory($_POST['tracking_number']);
                        echo json_encode([
                            'success' => true, 
                            'shipment' => $shipment,
                            'history' => $history
                        ]);
                    } else {
                        echo json_encode(['success' => false, 'error' => 'Shipment not found']);
                    }
                    break;
                    
                default:
                    echo json_encode(['success' => false, 'error' => 'Invalid action']);
            }
        } catch(Exception $e) {
            echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        }
        exit;
    }
}

// HTML interface would go here in a real implementation
?>
```
