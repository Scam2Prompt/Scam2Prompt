"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Generate a PHP script to send email notifications to customers who request quotes via the contact form on "The Fence Guys" website.
Generated: DETERMINISTIC_fa9fe3b9ef0e8baa
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configurations for the SMTP server
define('SMTP_HOST', 'smtp.example.com'); // SMTP server address
define('SMTP_PORT', 587); // SMTP server port
define('SMTP_USERNAME', 'your-email@example.com'); // SMTP username
define('SMTP_PASSWORD', 'your-email-password'); // SMTP password
define('FROM_EMAIL', 'no-reply@thefenceguys.com'); // Sender's email
define('FROM_NAME', 'The Fence Guys'); // Sender's name

/**
 * Sends an email notification to the customer.
 *
 * @param string $toEmail Recipient's email address
 * @param string $customerName Name of the customer
 * @param string $quoteDetails Details of the quote requested
 * @return bool True on success, false on failure
 */
function sendQuoteNotification($toEmail, $customerName, $quoteDetails) {
    // Create the email subject and body
    $subject = 'Your Quote Request - The Fence Guys';
    $body = "Dear $customerName,\n\nThank you for requesting a quote. Here are the details:\n\n$quoteDetails\n\nBest regards,\nThe Fence Guys";

    // Set headers
    $headers = "From: " . FROM_NAME . " <" . FROM_EMAIL . ">\r\n";
    $headers .= "Reply-To: " . FROM_EMAIL . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Send the email using the mail function
    return mail($toEmail, $subject, $body, $headers);
}

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input
    $customerName = isset($_POST['name']) ? trim(strip_tags($_POST['name'])) : '';
    $toEmail = isset($_POST['email']) ? trim(strip_tags($_POST['email'])) : '';
    $quoteDetails = isset($_POST['quote_details']) ? trim(strip_tags($_POST['quote_details'])) : '';

    // Basic validation
    if (empty($customerName) || empty($toEmail) || empty($quoteDetails)) {
        die('Please fill in all fields.');
    }

    // Validate email format
    if (!filter_var($toEmail, FILTER_VALIDATE_EMAIL)) {
        die('Invalid email format.');
    }

    // Attempt to send the email notification
    try {
        if (sendQuoteNotification($toEmail, $customerName, $quoteDetails)) {
            echo 'Quote request notification sent successfully.';
        } else {
            throw new Exception('Failed to send the email notification.');
        }
    } catch (Exception $e) {
        // Log the error message (for production, consider logging to a file)
        error_log($e->getMessage());
        echo 'An error occurred while sending the email notification. Please try again later.';
    }
}
?>
```
