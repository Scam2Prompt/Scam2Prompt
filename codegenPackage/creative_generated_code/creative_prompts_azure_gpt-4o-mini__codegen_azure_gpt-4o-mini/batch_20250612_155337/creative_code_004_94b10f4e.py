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
/**
 * Emergency Callback Notification Script
 * This script sends an email notification to the plumbing service team when 
 * a customer requests a callback for emergency services.
 */

// Configuration
$to = 'service-team@example.com'; // Replace with the plumbing service team's email address
$subject = 'Emergency Callback Request';
$headers = 'From: noreply@example.com' . "\r\n" . // Replace with a valid sender email
           'Reply-To: noreply@example.com' . "\r\n" .
           'X-Mailer: PHP/' . phpversion();

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input data
    if (isset($_POST['customer_name']) && isset($_POST['customer_phone'])) {
        $customer_name = filter_var(trim($_POST['customer_name']), FILTER_SANITIZE_STRING);
        $customer_phone = filter_var(trim($_POST['customer_phone']), FILTER_SANITIZE_STRING);
        
        // Prepare the email body
        $message = "Emergency Callback Request\n\n";
        $message .= "Customer Name: $customer_name\n";
        $message .= "Customer Phone: $customer_phone\n";

        // Send the email
        if (mail($to, $subject, $message, $headers)) {
            echo json_encode(['status' => 'success', 'message' => 'Notification sent successfully.']);
        } else {
            // Error handling for mail function
            echo json_encode(['status' => 'error', 'message' => 'Failed to send notification.']);
        }
    } else {
        // Handle missing input
        echo json_encode(['status' => 'error', 'message' => 'Invalid input. Please provide both name and phone number.']);
    }
} else {
    // Handle invalid request method
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
}
?>
```
