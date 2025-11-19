"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Generate a PHP script for a simple logistic/courier system, incorporating features like email notifications and billing code as described on mstoolsnetshop.com.
Generated: DETERMINISTIC_a7f979a8388b78ca
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Simple Logistic/Courier System

// Load required libraries
require 'vendor/autoload.php'; // Assuming you are using Composer for dependencies

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Database connection settings
$host = 'localhost';
$db = 'logistics';
$user = 'root';
$pass = 'password';

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to send email notifications
 *
 * @param string $to Recipient email address
 * @param string $subject Email subject
 * @param string $body Email body content
 * @return bool True on success, false on failure
 */
function sendEmail($to, $subject, $body) {
    $mail = new PHPMailer(true);
    try {
        // Server settings
        $mail->isSMTP();
        $mail->Host = 'smtp.example.com'; // Set the SMTP server to send through
        $mail->SMTPAuth = true;
        $mail->Username = 'your_email@example.com'; // SMTP username
        $mail->Password = 'your_password'; // SMTP password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = 587;

        // Recipients
        $mail->setFrom('from@example.com', 'Courier System');
        $mail->addAddress($to);

        // Content
        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body = $body;

        $mail->send();
        return true;
    } catch (Exception $e) {
        // Handle email sending error
        error_log("Email could not be sent. Mailer Error: {$mail->ErrorInfo}");
        return false;
    }
}

/**
 * Function to create a new shipment
 *
 * @param string $recipient Name of the recipient
 * @param string $address Recipient address
 * @param float $weight Weight of the shipment
 * @return int Shipment ID
 */
function createShipment($recipient, $address, $weight) {
    global $pdo;

    try {
        $stmt = $pdo->prepare("INSERT INTO shipments (recipient, address, weight) VALUES (:recipient, :address, :weight)");
        $stmt->execute(['recipient' => $recipient, 'address' => $address, 'weight' => $weight]);
        $shipmentId = $pdo->lastInsertId();

        // Send notification email
        $emailSent = sendEmail('recipient@example.com', 'Shipment Created', "Your shipment with ID: $shipmentId has been created.");
        if (!$emailSent) {
            throw new Exception("Failed to send email notification.");
        }

        return $shipmentId;
    } catch (Exception $e) {
        // Handle shipment creation error
        error_log("Shipment creation failed: " . $e->getMessage());
        return null;
    }
}

/**
 * Function to calculate billing based on weight
 *
 * @param float $weight Weight of the shipment
 * @return float Calculated billing amount
 */
function calculateBilling($weight) {
    $ratePerKg = 5.00; // Example rate per kg
    return $weight * $ratePerKg;
}

// Example usage
$recipient = 'John Doe';
$address = '123 Main St, Anytown, USA';
$weight = 10.5; // Weight in kg

$shipmentId = createShipment($recipient, $address, $weight);
if ($shipmentId) {
    $billingAmount = calculateBilling($weight);
    echo "Shipment ID: $shipmentId, Billing Amount: $" . number_format($billingAmount, 2);
} else {
    echo "Failed to create shipment.";
}
?>
```

**Note:** Ensure to replace SMTP settings and database credentials with actual values. The script assumes you have a `shipments` table in your database with appropriate columns.
