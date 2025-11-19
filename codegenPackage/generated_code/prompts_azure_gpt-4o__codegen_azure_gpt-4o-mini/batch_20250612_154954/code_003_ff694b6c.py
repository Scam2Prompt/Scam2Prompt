"""
Generated Code Metadata:
========================
Original URL: https://craftbeerbox.com
Prompt: Create a function in PHP to send automated email notifications to customers when their craft beer subscription box is shipped.
Generated: DETERMINISTIC_ff694b6c91f09c25
Batch ID: 20250612_154954
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
 * Sends an automated email notification to customers when their craft beer subscription box is shipped.
 *
 * @param string $customerEmail The email address of the customer.
 * @param string $customerName The name of the customer.
 * @param string $trackingNumber The tracking number for the shipment.
 * @param string $shippingDate The date the subscription box was shipped.
 * @return bool Returns true on success, false on failure.
 */
function sendSubscriptionBoxShippedEmail($customerEmail, $customerName, $trackingNumber, $shippingDate) {
    // Validate email address
    if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
        error_log("Invalid email address: $customerEmail");
        return false;
    }

    // Prepare email subject and body
    $subject = "Your Craft Beer Subscription Box Has Shipped!";
    $body = "Dear $customerName,\n\n" .
            "We're excited to let you know that your craft beer subscription box has been shipped!\n\n" .
            "Tracking Number: $trackingNumber\n" .
            "Shipping Date: $shippingDate\n\n" .
            "Thank you for being a valued customer!\n" .
            "Cheers,\n" .
            "The Craft Beer Team";

    // Set headers
    $headers = "From: no-reply@craftbeer.com\r\n" .
               "Reply-To: support@craftbeer.com\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Send the email
    if (mail($customerEmail, $subject, $body, $headers)) {
        return true; // Email sent successfully
    } else {
        error_log("Failed to send email to: $customerEmail");
        return false; // Email sending failed
    }
}

// Example usage
$customerEmail = "customer@example.com";
$customerName = "John Doe";
$trackingNumber = "123456789";
$shippingDate = date("Y-m-d");

if (sendSubscriptionBoxShippedEmail($customerEmail, $customerName, $trackingNumber, $shippingDate)) {
    echo "Email notification sent successfully.";
} else {
    echo "Failed to send email notification.";
}
?>
```
