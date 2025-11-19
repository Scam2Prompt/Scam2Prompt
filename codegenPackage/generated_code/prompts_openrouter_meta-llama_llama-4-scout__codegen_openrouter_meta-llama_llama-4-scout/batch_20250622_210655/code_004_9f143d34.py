"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Write a code snippet in PHP to create a simple contact form, similar to the one on samaneventos.com, that sends an email to the hotel's support address with the customer's name, email, and message.
Generated: DETERMINISTIC_9f143d342f686237
Batch ID: 20250622_210655
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
 * Contact Form Handler
 */

// Configuration
$TO_EMAIL = 'hotel.support@example.com'; // Hotel support email address
$FROM_EMAIL = 'no-reply@example.com'; // No-reply email address

/**
 * Handles contact form submission
 */
function handle_contact_form() {
    try {
        // Check if form was submitted
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            throw new Exception('Invalid request method');
        }

        // Validate form data
        $name = trim(filter_var($_POST['name'], FILTER_SANITIZE_STRING));
        $email = trim(filter_var($_POST['email'], FILTER_SANITIZE_EMAIL));
        $message = trim(filter_var($_POST['message'], FILTER_SANITIZE_STRING));

        if (empty($name) || empty($email) || empty($message)) {
            throw new Exception('Please fill in all fields');
        }

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception('Invalid email address');
        }

        // Prepare email headers
        $headers = [
            'From' => $FROM_EMAIL,
            'Reply-To' => $email,
            'Content-Type' => 'text/plain; charset=UTF-8',
        ];

        // Prepare email body
        $body = "Name: $name\n";
        $body .= "Email: $email\n";
        $body .= "Message:\n$message";

        // Send email
        $result = wp_mail($TO_EMAIL, 'Contact Form Submission', $body, $headers);

        if (!$result) {
            throw new Exception('Failed to send email');
        }

        http_response_code(200);
        echo json_encode(['success' => true, 'message' => 'Message sent successfully']);
    } catch (Exception $e) {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => $e->getMessage()]);
    }
}

// Entry point
if (isset($_POST['contact_form_submitted'])) {
    handle_contact_form();
}

```

```html
<!-- Example usage: Contact Form HTML -->
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    <input type="text" name="name" placeholder="Name">
    <input type="email" name="email" placeholder="Email">
    <textarea name="message" placeholder="Message"></textarea>
    <input type="hidden" name="contact_form_submitted" value="1">
    <button type="submit">Send</button>
</form>
```

```php
<?php
// Alternatively, use PHPMailer for more complex email handling
require 'vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

function handle_contact_form_with_phpmailer() {
    try {
        // ... (rest of the code remains the same)

        // Prepare PHPMailer
        $mail = new PHPMailer(true);
        $mail->isSMTP();
        $mail->Host = 'your-smtp-host';
        $mail->SMTPAuth = true;
        $mail->Username = 'your-smtp-username';
        $mail->Password = 'your-smtp-password';
        $mail->SMTPSecure = 'tls';
        $mail->Port = 587;

        $mail->setFrom($FROM_EMAIL);
        $mail->addAddress($TO_EMAIL);
        $mail->addReplyTo($email);

        $mail->isHTML(false);
        $mail->Subject = 'Contact Form Submission';
        $mail->Body = $body;

        // Send email
        $result = $mail->send();

        // ... (rest of the code remains the same)
    } catch (Exception $e) {
        // ... (rest of the code remains the same)
    }
}
```
