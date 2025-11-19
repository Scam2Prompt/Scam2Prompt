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
/**
 * Simple Logistic/Courier System
 * 
 * This script handles basic courier operations such as order creation, email notifications, and billing.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - SMTP configuration for email notifications
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Configuration
define('SMTP_HOST', 'smtp.example.com');
define('SMTP_PORT', 587);
define('SMTP_USERNAME', 'your-email@example.com');
define('SMTP_PASSWORD', 'your-email-password');
define('FROM_EMAIL', 'your-email@example.com');
define('FROM_NAME', 'Courier System');
define('CURRENCY', 'USD');

// Database connection (replace with your actual database credentials)
define('DB_HOST', 'localhost');
define('DB_NAME', 'courier_system');
define('DB_USER', 'root');
define('DB_PASSWORD', '');

// Establish database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Create a new courier order
 * 
 * @param string $customerName
 * @param string $customerEmail
 * @param string $pickupAddress
 * @param string $deliveryAddress
 * @param float $amount
 * @return void
 */
function createOrder($customerName, $customerEmail, $pickupAddress, $deliveryAddress, $amount)
{
    global $pdo;

    try {
        // Insert order into database
        $stmt = $pdo->prepare("INSERT INTO orders (customer_name, customer_email, pickup_address, delivery_address, amount, created_at) VALUES (?, ?, ?, ?, ?, NOW())");
        $stmt->execute([$customerName, $customerEmail, $pickupAddress, $deliveryAddress, $amount]);

        // Send email notification
        sendEmailNotification($customerEmail, "Order Confirmation", "Dear $customerName,\n\nYour order has been successfully created.\n\nPickup Address: $pickupAddress\nDelivery Address: $deliveryAddress\nAmount: " . CURRENCY . " $amount\n\nThank you for using our service!");

        echo "Order created successfully and email notification sent.";
    } catch (Exception $e) {
        echo "Error creating order: " . $e->getMessage();
    }
}

/**
 * Send email notification
 * 
 * @param string $to
 * @param string $subject
 * @param string $message
 * @return void
 */
function sendEmailNotification($to, $subject, $message)
{
    // Use PHPMailer for email sending
    require 'vendor/autoload.php'; // Ensure PHPMailer is installed via Composer

    $mail = new PHPMailer\PHPMailer\PHPMailer();

    try {
        // SMTP configuration
        $mail->isSMTP();
        $mail->Host = SMTP_HOST;
        $mail->SMTPAuth = true;
        $mail->Username = SMTP_USERNAME;
        $mail->Password = SMTP_PASSWORD;
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = SMTP_PORT;

        // Email settings
        $mail->setFrom(FROM_EMAIL, FROM_NAME);
        $mail->addAddress($to);
        $mail->Subject = $subject;
        $mail->Body = $message;

        // Send email
        if ($mail->send()) {
            echo "Email sent successfully to $to.";
        } else {
            echo "Failed to send email: " . $mail->ErrorInfo;
        }
    } catch (Exception $e) {
        echo "Error sending email: " . $e->getMessage();
    }
}

// Example usage
createOrder(
    "John Doe",
    "john.doe@example.com",
    "123 Pickup St, City A",
    "456 Delivery Ave, City B",
    50.00
);
?>
```
