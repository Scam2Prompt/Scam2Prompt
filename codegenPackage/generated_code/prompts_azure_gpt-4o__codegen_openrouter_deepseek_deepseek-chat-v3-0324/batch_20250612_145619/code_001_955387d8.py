"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Generate a PHP script for a logistics platform with integrated map functionality, inspired by the "Sprint Logistic PHP Script With Map" available on mstoolsnetshop.com.
Generated: DETERMINISTIC_955387d85cfa48a7
Batch ID: 20250612_145619
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://maps.googleapis.com/maps/api/directions/json?": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://maps.googleapis.com/maps/api/distancematrix/json?": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Sprint Logistic PHP Script With Map Integration
 * 
 * This script provides logistics management with integrated map functionality
 * for tracking shipments and optimizing routes.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'logistics_db');

// Google Maps API Key
define('GMAPS_API_KEY', 'YOUR_GOOGLE_MAPS_API_KEY');

// Error reporting
error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', __DIR__ . '/error.log');

// Start session
session_start();

// Autoload classes
spl_autoload_register(function ($class_name) {
    include 'classes/' . $class_name . '.php';
});

// Database connection
try {
    $db = new PDO(
        "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME,
        DB_USER,
        DB_PASS,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]
    );
} catch (PDOException $e) {
    error_log("Database connection failed: " . $e->getMessage());
    die("Database connection error. Please try again later.");
}

// Main application class
class LogisticsApp {
    private $db;
    
    public function __construct($db) {
        $this->db = $db;
    }
    
    /**
     * Get all shipments
     */
    public function getShipments() {
        try {
            $stmt = $this->db->query("SELECT * FROM shipments ORDER BY created_at DESC");
            return $stmt->fetchAll();
        } catch (PDOException $e) {
            error_log("Error fetching shipments: " . $e->getMessage());
            return [];
        }
    }
    
    /**
     * Get shipment by ID
     */
    public function getShipment($id) {
        try {
            $stmt = $this->db->prepare("SELECT * FROM shipments WHERE id = ?");
            $stmt->execute([$id]);
            return $stmt->fetch();
        } catch (PDOException $e) {
            error_log("Error fetching shipment: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Create new shipment
     */
    public function createShipment($data) {
        try {
            $stmt = $this->db->prepare(
                "INSERT INTO shipments 
                (origin, destination, weight, dimensions, status, customer_name, customer_phone) 
                VALUES (?, ?, ?, ?, ?, ?, ?)"
            );
            
            $stmt->execute([
                $data['origin'],
                $data['destination'],
                $data['weight'],
                $data['dimensions'],
                'pending',
                $data['customer_name'],
                $data['customer_phone']
            ]);
            
            return $this->db->lastInsertId();
        } catch (PDOException $e) {
            error_log("Error creating shipment: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Update shipment status
     */
    public function updateShipmentStatus($id, $status) {
        try {
            $stmt = $this->db->prepare(
                "UPDATE shipments SET status = ? WHERE id = ?"
            );
            return $stmt->execute([$status, $id]);
        } catch (PDOException $e) {
            error_log("Error updating shipment status: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Get optimized route between two points
     */
    public function getRoute($origin, $destination) {
        $url = "https://maps.googleapis.com/maps/api/directions/json?" . 
               "origin=" . urlencode($origin) . 
               "&destination=" . urlencode($destination) . 
               "&key=" . GMAPS_API_KEY;
        
        try {
            $response = file_get_contents($url);
            $data = json_decode($response, true);
            
            if ($data['status'] !== 'OK') {
                throw new Exception("Google Maps API error: " . $data['status']);
            }
            
            return $data;
        } catch (Exception $e) {
            error_log("Error getting route: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Get distance matrix between multiple points
     */
    public function getDistanceMatrix($origins, $destinations) {
        $url = "https://maps.googleapis.com/maps/api/distancematrix/json?" . 
               "origins=" . urlencode(implode('|', $origins)) . 
               "&destinations=" . urlencode(implode('|', $destinations)) . 
               "&key=" . GMAPS_API_KEY;
        
        try {
            $response = file_get_contents($url);
            $data = json_decode($response, true);
            
            if ($data['status'] !== 'OK') {
                throw new Exception("Google Maps API error: " . $data['status']);
            }
            
            return $data;
        } catch (Exception $e) {
            error_log("Error getting distance matrix: " . $e->getMessage());
            return false;
        }
    }
}

// Initialize application
$app = new LogisticsApp($db);

// Handle API requests
if (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] === 'POST') {
    header('Content-Type: application/json');
    
    try {
        $input = json_decode(file_get_contents('php://input'), true);
        
        if (isset($input['action'])) {
            switch ($input['action']) {
                case 'create_shipment':
                    $id = $app->createShipment($input['data']);
                    echo json_encode(['success' => $id !== false, 'id' => $id]);
                    break;
                    
                case 'get_route':
                    $route = $app->getRoute($input['origin'], $input['destination']);
                    echo json_encode(['success' => $route !== false, 'route' => $route]);
                    break;
                    
                case 'update_status':
                    $success = $app->updateShipmentStatus($input['id'], $input['status']);
                    echo json_encode(['success' => $success]);
                    break;
                    
                default:
                    echo json_encode(['success' => false, 'error' => 'Invalid action']);
            }
        } else {
            echo json_encode(['success' => false, 'error' => 'No action specified']);
        }
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
    }
    
    exit;
}

// HTML Template
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sprint Logistics</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        #map {
            height: 500px;
            width: 100%;
        }
        .shipment-card {
            cursor: pointer;
            transition: all 0.3s;
        }
        .shipment-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container-fluid">
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
            <div class="container">
                <a class="navbar-brand" href="#">Sprint Logistics</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" href="#">Dashboard</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Shipments</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Drivers</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Reports</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        
        <div class="row">
            <div class="col-md-4">
                <div class="card mb-4">
                    <div class="card-header bg-primary text-white">
                        <h5 class="mb-0">New Shipment</h5>
                    </div>
