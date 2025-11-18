"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftbeerbox.com
Prompt: Create a function in PHP to send automated email notifications to customers when their craft beer subscription box is shipped.
Generated: DETERMINISTIC_ff694b6c91f09c25
Batch ID: 20250612_154954
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
 * Sends an automated email notification to customers when their craft beer subscription box is shipped.
 *
 * @param string $customerEmail The email address of the customer.
 * @param string $customerName The name of the customer.
 * @param string $trackingNumber The tracking number for the shipment.
 * @return bool Returns true if the email was sent successfully, false otherwise.
 */
function sendSubscriptionShipmentNotification($customerEmail, $customerName, $trackingNumber) {
    // Validate the email address
    if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email address: $customerEmail");
    }

    // Prepare the email subject and body
    $subject = "Your Craft Beer Subscription Box is on its way!";
    $message = "
    Hi $customerName,

    We are excited to let you know that your craft beer subscription box has been shipped!

    Tracking Number: $trackingNumber

    Thank you for being a valued customer. We hope you enjoy your selection!

    Cheers,
    The Craft Beer Team
    ";

    // Set email headers
    $headers = "From: no-reply@craftbeercompany.com\r\n";
    $headers .= "Reply-To: support@craftbeercompany.com\r\n";
    $headers .= "Content-Type: text/plain; charset=utf-8\r\n";

    // Attempt to send the email and handle potential errors
    try {
        if (!mail($customerEmail, $subject, $message, $headers)) {
            throw new Exception("Failed to send email to $customerEmail");
        }
        return true; // Email sent successfully
    } catch (Exception $e) {
        // Log the error (error logging implementation can vary)
        error_log($e->getMessage());
        return false; // Email not sent
    }
}

// Example usage
try {
    $emailSent = sendSubscriptionShipmentNotification('customer@example.com', 'John Doe', 'TRACK123456');
    if ($emailSent) {
        echo "Email notification sent successfully.";
    } else {
        echo "Failed to send email notification.";
    }
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    echo "An unexpected error occurred: " . $e->getMessage();
}

?>
```
