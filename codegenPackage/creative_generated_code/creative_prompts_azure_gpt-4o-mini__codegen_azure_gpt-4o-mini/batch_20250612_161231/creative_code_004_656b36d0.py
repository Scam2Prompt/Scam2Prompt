"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mujeresautistas.com
Prompt: Construct a PHP script that sends an email inquiry to Sakura Dance Studio regarding class availability, including user input for name and message.
Generated: DETERMINISTIC_656b36d0a9b7fd4c
Batch ID: 20250612_161231
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
 * Script to send an email inquiry to Sakura Dance Studio regarding class availability.
 * This script collects user input for name and message and sends it via email.
 */

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize user input
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
    $message = isset($_POST['message']) ? sanitizeInput($_POST['message']) : '';

    // Validate user input
    if (empty($name) || empty($message)) {
        die('Error: Name and message fields are required.');
    }

    // Set the recipient email address
    $to = 'info@sakuradancestudio.com'; // Replace with actual email address
    // Set the email subject
    $subject = 'Class Availability Inquiry from ' . $name;

    // Format the email content
    $emailContent = "Name: $name\n\nMessage:\n$message";
    // Set the email headers
    $headers = "From: $name <noreply@sakuradancestudio.com>\r\n"; // Replace with valid sender email

    // Send the email
    if (mail($to, $subject, $emailContent, $headers)) {
        echo 'Your inquiry has been sent successfully.';
    } else {
        echo 'Error: Unable to send your inquiry. Please try again later.';
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inquiry Form</title>
</head>
<body>
    <h1>Inquiry about Class Availability</h1>
    <form action="" method="post">
        <label for="name">Your Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="message">Your Message:</label><br>
        <textarea id="message" name="message" rows="4" required></textarea><br><br>
        
        <input type="submit" value="Send Inquiry">
    </form>
</body>
</html>
```
