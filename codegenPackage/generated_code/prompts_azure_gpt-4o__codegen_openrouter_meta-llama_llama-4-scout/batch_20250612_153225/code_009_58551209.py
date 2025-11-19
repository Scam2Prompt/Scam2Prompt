"""
Generated Code Metadata:
========================
Original URL: https://morevacare.com
Prompt: Write PHP code to implement a "contact us" form for an e-commerce website, ensuring compliance with GDPR, as seen in MorevaCare's legal section.
Generated: DETERMINISTIC_5855120953227037
Batch ID: 20250612_153225
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
 * Contact Us Form Handler
 *
 * This script handles the contact us form submissions for the e-commerce website.
 * It ensures compliance with GDPR by providing a clear and transparent way of handling user data.
 */

// Configuration
$config = [
    'admin_email' => 'your-admin-email@example.com',
    'email_subject' => 'New Contact Us Inquiry',
    'honeypot_field' => 'website',
];

// Database configuration (if storing inquiries in a database)
$db_config = [
    'host' => 'your-host',
    'username' => 'your-username',
    'password' => 'your-password',
    'database' => 'your-database',
];

// Create a PDO instance for database operations (if applicable)
try {
    $pdo = new PDO(
        "mysql:host={$db_config['host']};dbname={$db_config['database']}",
        $db_config['username'],
        $db_config['password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Log the error or handle it accordingly
    error_log("Database connection failed: " . $e->getMessage());
}

// Function to send an email
function sendEmail($to, $subject, $message, $from_name, $from_email)
{
    $headers = [
        'From: ' . $from_email,
        'Reply-To: ' . $from_email,
        'Content-Type: text/html; charset=UTF-8',
    ];

    $email_body = "
    <html>
    <body>
        <h2>$subject</h2>
        <p>$message</p>
        <p>Best regards,<br>$from_name</p>
    </body>
    </html>
    ";

    try {
        mail($to, $subject, $email_body, implode("\r\n", $headers));
        return true;
    } catch (Exception $e) {
        error_log("Error sending email: " . $e->getMessage());
        return false;
    }
}

// Function to store inquiry in database (if applicable)
function storeInquiry($pdo, $name, $email, $message)
{
    $stmt = $pdo->prepare("INSERT INTO inquiries (name, email, message) VALUES (:name, :email, :message)");
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':message', $message);

    try {
        $stmt->execute();
        return true;
    } catch (PDOException $e) {
        error_log("Error storing inquiry: " . $e->getMessage());
        return false;
    }
}

// Check if form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check for honeypot field
    if (!empty($_POST[$config['honeypot_field']])) {
        // Honeypot field filled, likely a bot
        http_response_code(403);
        echo 'Forbidden';
        exit;
    }

    // Validate form data
    $errors = [];
    $name = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $message = trim($_POST['message'] ?? '');

    if (empty($name)) {
        $errors[] = 'Name is required';
    }

    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Valid email is required';
    }

    if (empty($message)) {
        $errors[] = 'Message is required';
    }

    if (!empty($errors)) {
        http_response_code(400);
        echo json_encode(['errors' => $errors]);
        exit;
    }

    // Send email
    $email_sent = sendEmail(
        $config['admin_email'],
        $config['email_subject'],
        "Name: $name\nEmail: $email\n\n$message",
        $name,
        $email
    );

    // Store inquiry in database (if applicable)
    if (isset($pdo)) {
        storeInquiry($pdo, $name, $email, $message);
    }

    if ($email_sent) {
        http_response_code(200);
        echo json_encode(['message' => 'Inquiry sent successfully']);
    } else {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to send inquiry']);
    }
} else {
    http_response_code(405);
    echo 'Method Not Allowed';
}
```
