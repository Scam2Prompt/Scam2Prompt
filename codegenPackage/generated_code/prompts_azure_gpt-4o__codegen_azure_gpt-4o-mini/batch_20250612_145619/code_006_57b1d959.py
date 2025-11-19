"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Create a PHP script for a logistics and courier system with email notifications, referencing the "Helologistics Logistic PHP Script" from mstoolsnetshop.com.
Generated: DETERMINISTIC_57b1d9591ece0b7d
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
// logistics.php

// Start session for user management
session_start();

// Include necessary files for database connection and email functionality
require_once 'config.php'; // Database configuration
require_once 'email.php'; // Email sending functionality

/**
 * Class Logistics
 * Handles logistics and courier operations
 */
class Logistics {
    private $db;

    // Constructor to initialize database connection
    public function __construct($dbConnection) {
        $this->db = $dbConnection;
    }

    /**
     * Create a new shipment
     * 
     * @param array $shipmentData Data for the shipment
     * @return bool True on success, false on failure
     */
    public function createShipment($shipmentData) {
        // Prepare SQL statement to prevent SQL injection
        $stmt = $this->db->prepare("INSERT INTO shipments (sender_name, receiver_name, address, weight, status) VALUES (?, ?, ?, ?, ?)");
        
        // Bind parameters
        $stmt->bind_param("sssis", $shipmentData['sender_name'], $shipmentData['receiver_name'], $shipmentData['address'], $shipmentData['weight'], $shipmentData['status']);
        
        // Execute the statement and check for errors
        if ($stmt->execute()) {
            // Send email notification
            $this->sendEmailNotification($shipmentData['receiver_email'], $shipmentData['tracking_number']);
            return true;
        } else {
            // Log error message
            error_log("Error creating shipment: " . $stmt->error);
            return false;
        }
    }

    /**
     * Send email notification
     * 
     * @param string $email Recipient's email address
     * @param string $trackingNumber Shipment tracking number
     */
    private function sendEmailNotification($email, $trackingNumber) {
        $subject = "Your Shipment is on the Way!";
        $message = "Your shipment has been created successfully. Your tracking number is: " . $trackingNumber;
        
        // Use the email function to send the email
        if (!sendEmail($email, $subject, $message)) {
            error_log("Error sending email to $email");
        }
    }
}

// Database connection
$dbConnection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check for connection errors
if ($dbConnection->connect_error) {
    die("Connection failed: " . $dbConnection->connect_error);
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input data
    $shipmentData = [
        'sender_name' => filter_var($_POST['sender_name'], FILTER_SANITIZE_STRING),
        'receiver_name' => filter_var($_POST['receiver_name'], FILTER_SANITIZE_STRING),
        'address' => filter_var($_POST['address'], FILTER_SANITIZE_STRING),
        'weight' => filter_var($_POST['weight'], FILTER_VALIDATE_FLOAT),
        'status' => 'Pending',
        'receiver_email' => filter_var($_POST['receiver_email'], FILTER_SANITIZE_EMAIL),
        'tracking_number' => uniqid('TRACK_') // Generate a unique tracking number
    ];

    // Create a new Logistics instance
    $logistics = new Logistics($dbConnection);

    // Create shipment and check for success
    if ($logistics->createShipment($shipmentData)) {
        echo "Shipment created successfully!";
    } else {
        echo "Failed to create shipment.";
    }
}

// Close the database connection
$dbConnection->close();
?>
```

```php
<?php
// config.php

// Database configuration constants
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'logistics_db');
?>
```

```php
<?php
// email.php

/**
 * Send an email
 * 
 * @param string $to Recipient's email address
 * @param string $subject Subject of the email
 * @param string $message Body of the email
 * @return bool True on success, false on failure
 */
function sendEmail($to, $subject, $message) {
    // Set content-type for HTML email
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

    // Additional headers
    $headers .= 'From: noreply@yourdomain.com' . "\r\n";

    // Send email and return the result
    return mail($to, $subject, $message, $headers);
}
?>
```

Make sure to replace the database credentials in `config.php` with your actual database credentials. This code is structured to be clean, efficient, and ready for production use, with proper error handling and documentation.
