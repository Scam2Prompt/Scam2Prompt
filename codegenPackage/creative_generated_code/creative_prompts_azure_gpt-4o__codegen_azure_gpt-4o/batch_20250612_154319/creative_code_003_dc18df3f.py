"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Write a PHP script to send a contact form submission to the email address provided on the Samba Plastic Industries website, including fields for name, email, phone number, title, and description.
Generated: DETERMINISTIC_dc18df3f8543fff3
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form.php

// Ensure error reporting is enabled for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// SMTP configuration (adjust based on your server configuration)
$SMTP_HOST = 'smtp.example.com'; // Replace with your SMTP host
$SMTP_PORT = 587;               // Replace with your SMTP port
$SMTP_USERNAME = 'your_username@example.com'; // Replace with your SMTP username
$SMTP_PASSWORD = 'your_password';             // Replace with your SMTP password

// Email recipient (Samba Plastic Industries' contact email)
$recipientEmail = 'contact@sambaplastic.com'; // Replace with the actual email address

// Function to send email
function sendContactEmail($name, $email, $phone, $title, $description, $recipientEmail) {
    // Import PHPMailer classes (Make sure you include PHPMailer via Composer or manually)
    require 'vendor/autoload.php'; // Ensure PHPMailer is installed via Composer

    $mail = new PHPMailer\PHPMailer\PHPMailer();

    try {
        // SMTP server settings
        $mail->isSMTP();
        $mail->Host = $GLOBALS['SMTP_HOST'];
        $mail->SMTPAuth = true;
        $mail->Username = $GLOBALS['SMTP_USERNAME'];
        $mail->Password = $GLOBALS['SMTP_PASSWORD'];
        $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = $GLOBALS['SMTP_PORT'];

        // Email settings
        $mail->setFrom($email, $name); // Sender's email and name
        $mail->addAddress($recipientEmail); // Recipient's email
        $mail->Subject = $title;
        $mail->Body = "Name: $name\nEmail: $email\nPhone: $phone\n\nDescription:\n$description";

        // Send the email
        if ($mail->send()) {
            return ['success' => true, 'message' => 'Email sent successfully.'];
        } else {
            return ['success' => false, 'message' => 'Failed to send email: ' . $mail->ErrorInfo];
        }
    } catch (Exception $e) {
        return ['success' => false, 'message' => 'Error occurred: ' . $e->getMessage()];
    }
}

// Validate and process form data
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $title = filter_input(INPUT_POST, 'title', FILTER_SANITIZE_STRING);
    $description = filter_input(INPUT_POST, 'description', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (!$name || !$email || !$phone || !$title || !$description) {
        echo json_encode(['success' => false, 'message' => 'All fields are required.']);
        exit;
    }

    // Send the email
    $result = sendContactEmail($name, $email, $phone, $title, $description, $recipientEmail);

    // Return JSON response
    header('Content-Type: application/json');
    echo json_encode($result);
} else {
    // Handle non-POST requests
    http_response_code(405); // Method Not Allowed
    echo json_encode(['success' => false, 'message' => 'Invalid request method.']);
}
?>
```

**Note:** 
- Ensure you have PHPMailer installed via Composer (`composer require phpmailer/phpmailer`).
- Replace relevant placeholders like SMTP credentials and recipient email with actual values.
- Save this code in a `.php` file (e.g., `contact_form.php`) on your server, and create a corresponding HTML form for user input.
