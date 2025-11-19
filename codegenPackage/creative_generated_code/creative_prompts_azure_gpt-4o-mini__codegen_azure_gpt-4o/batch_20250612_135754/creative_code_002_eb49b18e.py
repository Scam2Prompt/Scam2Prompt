"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cham-transfers.com
Prompt: Create a code snippet in PHP that integrates with a booking system for Chamonix transfers, allowing users to input their travel details and receive a confirmation email.
Generated: DETERMINISTIC_eb49b18e27ed9c3e
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Booking System Integration for Chamonix Transfers

// Configuration settings
define('SMTP_SERVER', 'smtp.example.com'); // Replace with your SMTP server
define('SMTP_PORT', 587);                 // Replace with your SMTP port
define('EMAIL_USERNAME', 'your_email@example.com'); // Replace with your email username
define('EMAIL_PASSWORD', 'your_email_password');   // Replace with your email password
define('EMAIL_FROM', 'your_email@example.com');    // Sender email address
define('EMAIL_SUBJECT', 'Chamonix Transfer Booking Confirmation');

// Function to send confirmation email
function sendConfirmationEmail($to, $subject, $message) {
    // Load PHPMailer
    require 'PHPMailer/PHPMailer.php';
    require 'PHPMailer/SMTP.php';

    $mail = new PHPMailer\PHPMailer\PHPMailer();
    try {
        // SMTP configuration
        $mail->isSMTP();
        $mail->Host = SMTP_SERVER;
        $mail->SMTPAuth = true;
        $mail->Username = EMAIL_USERNAME;
        $mail->Password = EMAIL_PASSWORD;
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = SMTP_PORT;

        // Email headers and body
        $mail->setFrom(EMAIL_FROM, 'Chamonix Transfers');
        $mail->addAddress($to);
        $mail->Subject = $subject;
        $mail->Body    = $message;

        // Send the email
        if (!$mail->send()) {
            throw new Exception('Email could not be sent: ' . $mail->ErrorInfo);
        }
    } catch (Exception $e) {
        error_log('Error sending email: ' . $e->getMessage());
        return false; // Return false on failure
    }
    return true; // Return true on success
}

// Main booking logic
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Ensure the request contains required data
    $requiredFields = ['name', 'email', 'travel_date', 'pickup_location', 'destination'];
    foreach ($requiredFields as $field) {
        if (empty($_POST[$field])) {
            http_response_code(400); // Bad Request
            echo json_encode(['error' => "Missing required field: $field"]);
            exit;
        }
    }

    // Sanitize and validate user input
    $name = htmlspecialchars($_POST['name']);
    $email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);
    $travelDate = htmlspecialchars($_POST['travel_date']);
    $pickupLocation = htmlspecialchars($_POST['pickup_location']);
    $destination = htmlspecialchars($_POST['destination']);

    if (!$email) {
        http_response_code(400); // Bad Request
        echo json_encode(['error' => 'Invalid email format']);
        exit;
    }

    // Generate confirmation message
    $confirmationMessage = "Dear $name,\n\n"
        . "Thank you for booking your transfer to Chamonix.\n"
        . "Here are your booking details:\n"
        . "Travel Date: $travelDate\n"
        . "Pickup Location: $pickupLocation\n"
        . "Destination: $destination\n\n"
        . "We look forward to serving you!\n\n"
        . "Best regards,\n"
        . "Chamonix Transfers Team";

    // Send confirmation email
    if (sendConfirmationEmail($email, EMAIL_SUBJECT, $confirmationMessage)) {
        http_response_code(200); // OK
        echo json_encode(['success' => 'Booking confirmed. Confirmation email sent.']);
    } else {
        http_response_code(500); // Internal Server Error
        echo json_encode(['error' => 'Booking confirmed, but email could not be sent.']);
    }
} else {
    // Handle invalid request method
    http_response_code(405); // Method Not Allowed
    echo json_encode(['error' => 'Invalid request method. Use POST.']);
}
?>
```

**Dependencies**: This script uses PHPMailer for sending emails. You can install PHPMailer using Composer (`composer require phpmailer/phpmailer`) or include it manually.

**Notes**: Update the SMTP configuration and email credentials with your server details. Ensure the script runs on a secure server with appropriate permissions and settings.
