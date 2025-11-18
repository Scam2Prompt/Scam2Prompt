"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Write a PHP script to send an email inquiry to "turismo@marchigue.cl" using the contact information provided on the Turismo Marchigüe website.
Generated: DETERMINISTIC_fd1d8f7bcfaca437
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
 * Sends an email inquiry to Turismo Marchigüe.
 *
 * This script gathers contact information from the user and
 * sends an email to the specified address. Ensure that the
 * server is configured to send emails using the mail() function.
 *
 * @throws Exception If the email fails to send or input validation fails.
 */

// Set the recipient email address
$recipient = "turismo@marchigue.cl";

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Validate and sanitize input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);
    
    // Check for validation errors
    if (empty($name) || empty($email) || empty($message)) {
        throw new Exception("Please fill in all fields.");
    }

    if (!$email) {
        throw new Exception("Invalid email format.");
    }

    // Prepare the email headers
    $headers = "From: $name <$email>\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=utf-8\r\n";

    // Compose the email body
    $emailBody = "Name: $name\n";
    $emailBody .= "Email: $email\n\n";
    $emailBody .= "Message:\n$message\n";

    // Send the email
    if (mail($recipient, "New Inquiry from Website", $emailBody, $headers)) {
        echo "Email sent successfully!";
    } else {
        throw new Exception("Email sending failed. Please try again later.");
    }
}

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Contact Inquiry</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        
        <button type="submit">Send Inquiry</button>
    </form>
</body>
</html>
```
