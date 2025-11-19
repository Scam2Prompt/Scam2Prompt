"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepbook.online
Prompt: Construct a PHP script that sends an email notification to a plumbing service team when a customer requests a callback for emergency services.
Generated: DETERMINISTIC_94b10f4e77633c9b
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Callback request email sender for plumbing service

/**
 * Sends an email notification to the plumbing service team when a customer requests a callback.
 *
 * @param string $customerName The name of the customer.
 * @param string $customerPhone The phone number of the customer.
 * @param string $customerEmail The email address of the customer (optional).
 * @return bool Returns true if the email was sent successfully, false otherwise.
 */
function sendCallbackRequestEmail($customerName, $customerPhone, $customerEmail = null)
{
    // Validate input
    if (empty($customerName) || empty($customerPhone)) {
        throw new InvalidArgumentException("Customer name and phone number are required.");
    }

    // Plumbing service team's email address
    $serviceTeamEmail = "service@plumbingcompany.com";

    // Email subject
    $subject = "Emergency Callback Request";

    // Email message body
    $message = "Dear Plumbing Service Team,\n\n";
    $message .= "A customer has requested an emergency callback. Please find the details below:\n\n";
    $message .= "Name: " . htmlspecialchars($customerName) . "\n";
    $message .= "Phone: " . htmlspecialchars($customerPhone) . "\n";
    if ($customerEmail) {
        $message .= "Email: " . htmlspecialchars($customerEmail) . "\n";
    }
    $message .= "\nPlease contact the customer as soon as possible.\n\n";
    $message .= "Thank you,\nCallback Notification System";

    // Email headers
    $headers = "From: no-reply@plumbingcompany.com\r\n";
    $headers .= "Reply-To: no-reply@plumbingcompany.com\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();

    // Send the email
    $emailSent = mail($serviceTeamEmail, $subject, $message, $headers);

    // Return whether the email was successfully sent
    return $emailSent;
}

// Example usage
try {
    $customerName = "John Doe";
    $customerPhone = "123-456-7890";
    $customerEmail = "johndoe@example.com";

    $result = sendCallbackRequestEmail($customerName, $customerPhone, $customerEmail);

    if ($result) {
        echo "Email sent successfully.";
    } else {
        echo "Failed to send email.";
    }
} catch (Exception $e) {
    // Handle errors (log them or display them)
    error_log("Error sending email: " . $e->getMessage());
    echo "An error occurred while sending the email. Please try again later.";
}

?>
```
