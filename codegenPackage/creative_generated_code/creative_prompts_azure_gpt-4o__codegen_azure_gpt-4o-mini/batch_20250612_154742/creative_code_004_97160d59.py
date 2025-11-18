"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Write a PHP script to send email confirmations to customers after they book a tour package or taxi service through the "Best Holidays All India" website.
Generated: DETERMINISTIC_97160d59dd05f29b
Batch ID: 20250612_154742
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
 * Email Confirmation Script for Tour Package or Taxi Service Booking
 * Best Holidays All India
 * 
 * This script sends a confirmation email to customers after they book a tour package 
 * or taxi service. It uses PHP's mail function and includes error handling.
 */

// Configuration settings
define('SMTP_HOST', 'smtp.example.com'); // SMTP server address
define('SMTP_PORT', 587); // SMTP port
define('SMTP_USER', 'your_email@example.com'); // SMTP username
define('SMTP_PASS', 'your_password'); // SMTP password
define('FROM_EMAIL', 'no-reply@bestholidaysallindia.com'); // From email address
define('FROM_NAME', 'Best Holidays All India'); // From name
define('SUBJECT', 'Your Booking Confirmation'); // Email subject

/**
 * Send confirmation email to customer
 *
 * @param string $to Email address of the customer
 * @param string $customerName Name of the customer
 * @param string $bookingDetails Details of the booking
 * @return bool True on success, False on failure
 */
function sendConfirmationEmail($to, $customerName, $bookingDetails) {
    // Validate email format
    if (!filter_var($to, FILTER_VALIDATE_EMAIL)) {
        error_log("Invalid email format: $to");
        return false;
    }

    // Prepare email headers
    $headers = "From: " . FROM_NAME . " <" . FROM_EMAIL . ">\r\n";
    $headers .= "Reply-To: " . FROM_EMAIL . "\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";

    // Prepare email body
    $body = "<h1>Booking Confirmation</h1>";
    $body .= "<p>Dear " . htmlspecialchars($customerName) . ",</p>";
    $body .= "<p>Thank you for booking with us! Here are your booking details:</p>";
    $body .= "<p>" . nl2br(htmlspecialchars($bookingDetails)) . "</p>";
    $body .= "<p>We look forward to serving you!</p>";
    $body .= "<p>Best Regards,<br>" . FROM_NAME . "</p>";

    // Attempt to send the email
    if (mail($to, SUBJECT, $body, $headers)) {
        return true;
    } else {
        error_log("Failed to send email to: $to");
        return false;
    }
}

// Example usage
$customerEmail = 'customer@example.com'; // Customer's email
$customerName = 'John Doe'; // Customer's name
$bookingDetails = 'Tour Package: Golden Triangle<br>Date: 2023-10-01<br>Price: $500'; // Booking details

// Sending confirmation email
if (sendConfirmationEmail($customerEmail, $customerName, $bookingDetails)) {
    echo "Confirmation email sent successfully to $customerEmail.";
} else {
    echo "Failed to send confirmation email.";
}
?>
```
