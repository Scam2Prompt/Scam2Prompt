"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Write a PHP script to send promotional emails about new arrivals and sales, such as "Save 50% on Ralph Lauren Shirts," to subscribers, as seen on brandsoutlet.qa.
Generated: DETERMINISTIC_f969d29831f38971
Batch ID: 20250612_151858
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
 * Sends promotional emails to subscribers about new arrivals and sales.
 *
 * @param array $subscribers An array of email addresses to send promotions to.
 * @param string $subject The subject line of the email.
 * @param string $message The body of the email.
 * @return void
 */
function sendPromotionalEmails(array $subscribers, string $subject, string $message): void {
    // Validate the subject and message
    if (empty($subject) || empty($message)) {
        throw new InvalidArgumentException('Subject and message cannot be empty.');
    }
    
    foreach ($subscribers as $email) {
        // Validate email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            error_log("Invalid email address: $email");
            continue; // Skip to the next email if the current one is invalid
        }

        // Send email
        $headers = 'From: promotions@brandsoutlet.qa' . "\r\n" .
                   'Reply-To: promotions@brandsoutlet.qa' . "\r\n" .
                   'X-Mailer: PHP/' . phpversion();

        // Use mail() function to send email
        if (mail($email, $subject, $message, $headers)) {
            echo "Email sent to: $email\n";
        } else {
            error_log("Failed to send email to: $email");
        }
    }
}

// Example usage
try {
    // List of subscribers (in a production environment, retrieve this from a database)
    $subscribers = [
        'user1@example.com',
        'user2@example.com',
        'invalid-email', // This is to demonstrate error handling
        'user3@example.com'
    ];

    // Subject and message of the promotional email
    $subject = "Save 50% on Ralph Lauren Shirts";
    $message = "Don't miss out on our latest arrivals! Enjoy 50% off Ralph Lauren shirts while stocks last.";

    // Send promotional emails
    sendPromotionalEmails($subscribers, $subject, $message);
} catch (Exception $e) {
    // Log any exceptions that occur
    error_log('Error sending promotional emails: ' . $e->getMessage());
}
?>
```
