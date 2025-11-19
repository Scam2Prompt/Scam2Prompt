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
// Maintenance Request Email Notification Script

// Ensure error reporting is enabled for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to send an email notification
function sendMaintenanceRequestEmail($serviceProviderEmail, $customerName, $customerEmail, $message) {
    // Validate input parameters
    if (!filter_var($serviceProviderEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid service provider email address.");
    }
    if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid customer email address.");
    }
    if (empty($customerName) || empty($message)) {
        throw new InvalidArgumentException("Customer name and message cannot be empty.");
    }

    // Email subject
    $subject = "New Refrigerator Maintenance Request";

    // Email body
    $body = "Hello Service Provider,\n\n"
          . "You have received a new maintenance request for a refrigerator. Here are the details:\n\n"
          . "Customer Name: $customerName\n"
          . "Customer Email: $customerEmail\n"
          . "Message: $message\n\n"
          . "Please respond promptly.\n\n"
          . "Thank you.";
    
    // Email headers
    $headers = [
        "From: no-reply@yourcompany.com",
        "Reply-To: $customerEmail",
        "Content-Type: text/plain; charset=UTF-8"
    ];

    // Send the email
    if (!mail($serviceProviderEmail, $subject, $body, implode("\r\n", $headers))) {
        throw new RuntimeException("Failed to send email notification.");
    }
}

try {
    // Example usage of the function
    $serviceProviderEmail = "provider@example.com"; // Replace with service provider's email
    $customerName = "John Doe";                     // Replace with customer's name
    $customerEmail = "johndoe@example.com";         // Replace with customer's email
    $message = "The refrigerator is making loud noises and is not cooling properly."; // Replace with message details

    // Send the email
    sendMaintenanceRequestEmail($serviceProviderEmail, $customerName, $customerEmail, $message);

    // Success message
    echo "Maintenance request email sent successfully.";
} catch (InvalidArgumentException $e) {
    // Handle input validation errors
    echo "Error: " . $e->getMessage();
} catch (RuntimeException $e) {
    // Handle email sending errors
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    // Handle unexpected errors
    echo "An unexpected error occurred: " . $e->getMessage();
}
?>
```
