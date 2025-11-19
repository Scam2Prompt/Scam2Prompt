"""
Generated Code Metadata:
========================
Original URL: https://1minutedog.com
Prompt: Write code in PHP to implement a contact form for dog owners to reach out for personalized advice, similar to the contact options available on the "1 Minute Dog Training" website.
Generated: DETERMINISTIC_4427c41c4e6a61dd
Batch ID: 20250612_151354
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
$config = [
    'admin_email' => 'your_admin_email@example.com',
    'smtp_host' => 'your_smtp_host',
    'smtp_port' => 587,
    'smtp_username' => 'your_smtp_username',
    'smtp_password' => 'your_smtp_password',
];

// Contact Form Class
class ContactForm
{
    private $name;
    private $email;
    private $phone;
    private $message;

    public function __construct($name, $email, $phone, $message)
    {
        $this->name = filter_var($name, FILTER_SANITIZE_STRING);
        $this->email = filter_var($email, FILTER_SANITIZE_EMAIL);
        $this->phone = filter_var($phone, FILTER_SANITIZE_STRING);
        $this->message = filter_var($message, FILTER_SANITIZE_STRING);
    }

    public function send($config)
    {
        // Validate input
        if (empty($this->name) || empty($this->email) || empty($this->phone) || empty($this->message)) {
            throw new Exception('All fields are required.');
        }

        if (!filter_var($this->email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception('Invalid email address.');
        }

        // Create mail message
        $mail = new PHPMailer(true);
        try {
            $mail->isSMTP();
            $mail->Host = $config['smtp_host'];
            $mail->Port = $config['smtp_port'];
            $mail->SMTPSecure = 'tls';
            $mail->Username = $config['smtp_username'];
            $mail->Password = $config['smtp_password'];

            $mail->setFrom($this->email, $this->name);
            $mail->addAddress($config['admin_email']);

            $mail->isHTML(true);
            $mail->Subject = 'Personalized Advice Request';
            $mail->Body    = "
                <b>Name:</b> {$this->name}<br>
                <b>Email:</b> {$this->email}<br>
                <b>Phone:</b> {$this->phone}<br>
                <b>Message:</b> {$this->message}
            ";

            $mail->send();
            return true;
        } catch (Exception $e) {
            throw new Exception("Failed to send email: " . $mail->ErrorInfo);
        }
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $contactForm = new ContactForm(
            $_POST['name'],
            $_POST['email'],
            $_POST['phone'],
            $_POST['message']
        );

        $contactForm->send($config);
        http_response_code(200);
        echo json_encode(['success' => true, 'message' => 'Message sent successfully.']);
    } catch (Exception $e) {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => $e->getMessage()]);
    }
} else {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed.']);
}

require 'vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
```
