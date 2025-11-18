"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paperland.com.ar
Prompt: Write a PHP script to handle customer inquiries and orders for personalized paper products, similar to the contact form functionality on Paperland's website.
Generated: DETERMINISTIC_5be5cbc0bea48f58
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Customer Inquiry and Order Handler for Personalized Paper Products
 *
 * This script handles customer inquiries and orders submitted via a contact form.
 * It validates form input, sends confirmation emails, and logs inquiries for further processing.
 */

// Enable error reporting for debugging during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define constants for email configuration
define('ADMIN_EMAIL', 'admin@paperland.com'); // Replace with the actual admin email
define('FROM_EMAIL', 'no-reply@paperland.com');
define('EMAIL_SUBJECT', 'Customer Inquiry/Order Confirmation');
define('LOG_FILE', __DIR__ . '/inquiries.log');

/**
 * Function to validate form input
 *
 * @param string $data The input data to validate
 * @return string The sanitized input data
 */
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate form input
    $name        = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
    $email       = isset($_POST['email']) ? sanitizeInput($_POST['email']) : '';
    $productType = isset($_POST['product_type']) ? sanitizeInput($_POST['product_type']) : '';
    $message     = isset($_POST['message']) ? sanitizeInput($_POST['message']) : '';
    
    // Error handling: Ensure all required fields are provided
    $errors = [];
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'A valid email address is required.';
    }
    if (empty($productType)) {
        $errors[] = 'Product type is required.';
    }
    if (empty($message)) {
        $errors[] = 'Message is required.';
    }

    // If there are errors, display them and exit
    if (!empty($errors)) {
        header('Content-Type: application/json');
        echo json_encode(['success' => false, 'errors' => $errors]);
        exit;
    }

    // Prepare email content
    $emailContent = "
        Dear $name,\n
        Thank you for your inquiry/order regarding personalized paper products.\n
        Here are the details you provided:
        - Product Type: $productType
        - Message: $message\n
        We will review your request and get back to you shortly.\n
        - Paperland Team
    ";

    // Send confirmation email to the customer
    $headers = "From: " . FROM_EMAIL . "\r\n" .
               "Reply-To: " . ADMIN_EMAIL . "\r\n" .
               "Content-Type: text/plain; charset=UTF-8";

    if (!mail($email, EMAIL_SUBJECT, $emailContent, $headers)) {
        header('Content-Type: application/json');
        echo json_encode(['success' => false, 'errors' => ['Failed to send confirmation email.']]);
        exit;
    }

    // Log the inquiry for admin review
    $logEntry = date('Y-m-d H:i:s') . " | Name: $name | Email: $email | Product Type: $productType | Message: $message\n";
    file_put_contents(LOG_FILE, $logEntry, FILE_APPEND);

    // Respond with success status
    header('Content-Type: application/json');
    echo json_encode(['success' => true, 'message' => 'Inquiry submitted successfully.']);
    exit;
}

// If accessed without form submission, respond with an error
header('Content-Type: application/json');
echo json_encode(['success' => false, 'errors' => ['Invalid request method.']]);
exit;
?>
```
