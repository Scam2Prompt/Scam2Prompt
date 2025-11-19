"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Create a PHP code snippet that sends an inquiry email to Sekolah Quran Indonesia's contact address for more information about their Ma'had Aly program.
Generated: DETERMINISTIC_86afa7dc9f1aa65e
Batch ID: 20250612_160703
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
 * Sends an inquiry email to Sekolah Quran Indonesia regarding the Ma'had Aly program.
 *
 * @param string $name The name of the person sending the inquiry.
 * @param string $email The email address of the person sending the inquiry.
 * @param string $message The message content of the inquiry.
 * @return bool True if the email was sent successfully, false otherwise.
 */
function sendInquiryEmail($name, $email, $message) {
    // Validate input
    if (empty($name) || empty($email) || empty($message)) {
        throw new InvalidArgumentException('Name, email, and message are required fields.');
    }

    // Sanitize input
    $name = filter_var($name, FILTER_SANITIZE_STRING);
    $email = filter_var($email, FILTER_SANITIZE_EMAIL);
    $message = filter_var($message, FILTER_SANITIZE_STRING);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email format.');
    }

    // Set the recipient email address
    $to = 'contact@sekolahquranindonesia.com'; // Replace with the actual contact email
    $subject = 'Inquiry about Ma\'had Aly Program';
    
    // Create the email headers
    $headers = "From: $name <$email>\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Create the email body
    $body = "Name: $name\n";
    $body .= "Email: $email\n\n";
    $body .= "Message:\n$message\n";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        return true; // Email sent successfully
    } else {
        throw new RuntimeException('Failed to send email. Please try again later.');
    }
}

// Example usage
try {
    $name = 'John Doe'; // Replace with user input
    $email = 'johndoe@example.com'; // Replace with user input
    $message = 'I would like to know more about the Ma\'had Aly program.'; // Replace with user input

    if (sendInquiryEmail($name, $email, $message)) {
        echo 'Inquiry email sent successfully.';
    }
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo 'Error: ' . $e->getMessage();
}
?>
```
