"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Develop a code snippet in PHP that sends an email notification to a service provider when a maintenance request for a refrigerator is submitted.
Generated: DETERMINISTIC_89fde0fd388ef6fa
Batch ID: 20250612_163540
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
 * Sends an email notification to a service provider when a maintenance request
 * for a refrigerator is submitted.
 *
 * @param string $serviceProviderEmail The email address of the service provider.
 * @param string $customerName The name of the customer submitting the request.
 * @param string $issueDescription A brief description of the issue.
 * @return bool True if the email was sent successfully, false otherwise.
 */
function sendMaintenanceRequestEmail($serviceProviderEmail, $customerName, $issueDescription) {
    // Validate email format
    if (!filter_var($serviceProviderEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email format for service provider.');
    }

    // Prepare email subject and body
    $subject = 'New Maintenance Request for Refrigerator';
    $body = "Hello,\n\n"
          . "You have received a new maintenance request.\n\n"
          . "Customer Name: $customerName\n"
          . "Issue Description: $issueDescription\n\n"
          . "Please address this request at your earliest convenience.\n\n"
          . "Thank you.";

    // Set headers for the email
    $headers = "From: noreply@example.com\r\n" .
               "Reply-To: noreply@example.com\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Send the email using the mail function
    if (!mail($serviceProviderEmail, $subject, $body, $headers)) {
        // Log error if mail sending fails
        error_log("Failed to send maintenance request email to $serviceProviderEmail");
        return false;
    }

    return true;
}

// Example usage
try {
    $serviceProviderEmail = 'provider@example.com';
    $customerName = 'John Doe';
    $issueDescription = 'Refrigerator not cooling properly.';
    
    if (sendMaintenanceRequestEmail($serviceProviderEmail, $customerName, $issueDescription)) {
        echo 'Email notification sent successfully.';
    } else {
        echo 'Failed to send email notification.';
    }
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo 'Error: ' . $e->getMessage();
}
?>
```
