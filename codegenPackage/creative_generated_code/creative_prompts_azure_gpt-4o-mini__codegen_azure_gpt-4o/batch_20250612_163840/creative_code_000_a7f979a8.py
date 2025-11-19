"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mstoolsnetshop.com
Prompt: Generate a PHP script for a simple logistic/courier system, incorporating features like email notifications and billing code as described on mstoolsnetshop.com.
Generated: DETERMINISTIC_a7f979a8388b78ca
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// logistics_system.php

// Ensure errors are displayed during development but suppressed in production
error_reporting(E_ALL); // Use error_reporting(0) in production
ini_set('display_errors', '1');

// Configuration for database connection and email settings
define('DB_HOST', 'your_database_host');
define('DB_NAME', 'your_database_name');
define('DB_USER', 'your_database_user');
define('DB_PASSWORD', 'your_database_password');

define('SMTP_HOST', 'your_smtp_host');
define('SMTP_PORT', 587); // Adjust if using a different port
define('SMTP_USER', 'your_email_user');
define('SMTP_PASS', 'your_email_password');
define('FROM_EMAIL', 'your_email@example.com');
define('FROM_NAME', 'Your Logistic System');

// Establish database connection using PDO
function getDatabaseConnection(): PDO {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8";
        $pdo = new PDO($dsn, DB_USER, DB_PASSWORD);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Send email notification function
function sendEmailNotification(string $toEmail, string $subject, string $message): bool {
    try {
        // PHPMailer library can be used for robust email handling
        require 'path_to/PHPMailer.php'; 
        require 'path_to/SMTP.php'; 
        
        $mail = new PHPMailer\PHPMailer\PHPMailer();
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USER;
        $mail->Password = SMTP_PASS;
        $mail->Port = SMTP_PORT;

        $mail->setFrom(FROM_EMAIL, FROM_NAME);
        $mail->addAddress($toEmail);
        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body = $message;

        return $mail->send();
    } catch (Exception $e) {
        error_log("Email failed: " . $e->getMessage());
        return false;
    }
}

// Create a new shipment function
function createShipment(array $shipmentDetails): bool {
    try {
        $pdo = getDatabaseConnection();

        $statement = $pdo->prepare(
            "INSERT INTO shipments 
            (tracking_number, sender_name, recipient_name, recipient_address, package_weight, status, created_at) 
            VALUES (:tracking_number, :sender_name, :recipient_name, :recipient_address, :package_weight, :status, NOW())"
        );

        $shipmentDetails['tracking_number'] = generateTrackingNumber();
        $shipmentDetails['status'] = 'Pending';

        if ($statement->execute($shipmentDetails)) {
            // Send email notification to the recipient
            $emailSent = sendEmailNotification(
                $shipmentDetails['recipient_email'],
                'Your Shipment has been created!',
                'Your shipment with tracking number: ' . $shipmentDetails['tracking_number'] . ' has been created.'
            );

            return $emailSent;
        }

        return false;

    } catch (Exception $e) {
        error_log("Error creating shipment: " . $e->getMessage());
        return false;
    }
}

// Generate a unique tracking number
function generateTrackingNumber(): string {
    return strtoupper(uniqid('TRK'));
}

// Update shipment status function
function updateShipmentStatus(string $trackingNumber, string $newStatus): bool {
    try {
        $pdo = getDatabaseConnection();

        $statement = $pdo->prepare(
            "UPDATE shipments 
            SET status = :status, updated_at = NOW() 
            WHERE tracking_number = :tracking_number"
        );

        return $statement->execute([
            ':status' => $newStatus,
            ':tracking_number' => $trackingNumber
        ]);

    } catch (Exception $e) {
        error_log("Error updating shipment status: " . $e->getMessage());
        return false;
    }
}

// Calculate billing function
function calculateBilling(float $weight): float {
    $baseRate = 5.00; // Base rate in USD
    $ratePerKg = 2.00; // Rate per kg in USD

    return $baseRate + ($ratePerKg * $weight);
}

// Example usage (should be replaced with API endpoints in a production system)

// Create a shipment
$shipmentDetails = [
    'sender_name' => 'John Doe',
    'recipient_name' => 'Jane Smith',
    'recipient_address' => '123 Street, City, Country',
    'recipient_email' => 'jane.smith@example.com',
    'package_weight' => 10.5
];

if (createShipment($shipmentDetails)) {
    echo "Shipment created successfully!";
} else {
    echo "Failed to create shipment.";
}

// Update shipment status
if (updateShipmentStatus('TRK12345ABCDE', 'Delivered')) {
    echo "Shipment status updated!";
} else {
    echo "Failed to update shipment status.";
}

// Calculate billing
$weight = 10.5; // Example weight
echo "The billing cost is: $" . calculateBilling($weight);

?>
```
