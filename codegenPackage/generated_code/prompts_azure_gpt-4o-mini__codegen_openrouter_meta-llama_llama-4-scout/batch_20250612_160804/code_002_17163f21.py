"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Create a PHP script to handle customer inquiries about personalized flip-flops, similar to the services offered by Surff Ojotas.
Generated: DETERMINISTIC_17163f2144e0c379
Batch ID: 20250612_160804
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
 * Customer Inquiry Handler for Personalized Flip-Flops
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Database connection failed: ' . $e->getMessage());
}

/**
 * Handle customer inquiry
 *
 * @param array $inquiry
 * @return bool
 */
function handleInquiry(array $inquiry): bool
{
    global $pdo;

    // Validate input
    if (!isset($inquiry['name'], $inquiry['email'], $inquiry['message'], $inquiry['flip_flop_design'])) {
        throw new Exception('Invalid inquiry data');
    }

    // Sanitize input
    $name = htmlspecialchars($inquiry['name']);
    $email = htmlspecialchars($inquiry['email']);
    $message = htmlspecialchars($inquiry['message']);
    $flipFlopDesign = htmlspecialchars($inquiry['flip_flop_design']);

    // Save inquiry to database
    $stmt = $pdo->prepare('
        INSERT INTO inquiries (name, email, message, flip_flop_design, created_at)
        VALUES (:name, :email, :message, :flip_flop_design, NOW())
    ');
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':message', $message);
    $stmt->bindParam(':flip_flop_design', $flipFlopDesign);

    try {
        $stmt->execute();
        return true;
    } catch (PDOException $e) {
        throw new Exception('Failed to save inquiry: ' . $e->getMessage());
    }
}

/**
 * Send confirmation email to customer
 *
 * @param string $email
 * @param string $message
 * @return bool
 */
function sendConfirmationEmail(string $email, string $message): bool
{
    // Email configuration
    $subject = 'Inquiry Confirmation - Personalized Flip-Flops';
    $fromEmail = 'your_email@example.com';

    // Email content
    $body = "
        Dear Customer,<br>
        Thank you for your inquiry about personalized flip-flops. We will get back to you soon.<br>
        Your message: $message<br>
        Best regards,
        [Your Name]
    ";

    // Send email using PHPMailer or your preferred email library
    // For simplicity, this example uses mail()
    try {
        $headers = 'From: ' . $fromEmail . "\r\n";
        mail($email, $subject, $body, $headers);
        return true;
    } catch (Exception $e) {
        throw new Exception('Failed to send confirmation email: ' . $e->getMessage());
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $inquiry = [
            'name' => $_POST['name'],
            'email' => $_POST['email'],
            'message' => $_POST['message'],
            'flip_flop_design' => $_POST['flip_flop_design'],
        ];

        if (handleInquiry($inquiry)) {
            sendConfirmationEmail($inquiry['email'], $inquiry['message']);
            http_response_code(201);
            echo 'Inquiry submitted successfully';
        } else {
            http_response_code(500);
            echo 'Failed to submit inquiry';
        }
    } catch (Exception $e) {
        http_response_code(400);
        echo 'Error: ' . $e->getMessage();
    }
}

// Close database connection
$pdo = null;

?>
```
