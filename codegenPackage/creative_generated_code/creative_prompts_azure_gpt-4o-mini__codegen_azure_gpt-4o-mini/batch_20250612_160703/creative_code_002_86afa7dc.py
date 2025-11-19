"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Create a PHP code snippet that sends an inquiry email to Sekolah Quran Indonesia's contact address for more information about their Ma'had Aly program.
Generated: DETERMINISTIC_86afa7dc9f1aa65e
Batch ID: 20250612_160703
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
        throw new InvalidArgumentException('Name, email, and message are required.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email format.');
    }

    // Set the recipient email address
    $to = 'contact@sekolahquranindonesia.com'; // Replace with the actual contact email
    $subject = 'Inquiry about Ma\'had Aly Program';
    
    // Create the email headers
    $headers = "From: $name <$email>\r\n" .
               "Reply-To: $email\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Prepare the email body
    $body = "You have received a new inquiry regarding the Ma'had Aly program:\n\n" .
            "Name: $name\n" .
            "Email: $email\n\n" .
            "Message:\n$message";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        return true; // Email sent successfully
    } else {
        throw new RuntimeException('Failed to send email.');
    }
}

// Example usage
try {
    $name = 'John Doe'; // Replace with user input
    $email = 'johndoe@example.com'; // Replace with user input
    $message = 'I would like to know more about the Ma\'had Aly program.'; // Replace with user input

    sendInquiryEmail($name, $email, $message);
    echo "Inquiry sent successfully!";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
