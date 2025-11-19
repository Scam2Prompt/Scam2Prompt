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
// Define the recipient email address for Sekolah Quran Indonesia's contact
$recipientEmail = "contact@sekolahquranindonesia.com"; 

// Subject of the inquiry email
$emailSubject = "Inquiry About Ma'had Aly Program";

// Content of the email message
$emailMessage = "
Dear Sekolah Quran Indonesia Team,

I am writing to inquire about the Ma'had Aly program offered by your institution. 
I would like to know more details about the program structure, admission requirements, and any other relevant information.

Thank you for your time and assistance. I look forward to your reply.

Best regards,
[Your Name]
[Your Contact Information]
";

// Additional headers
$headers = "From: your-email@example.com" . "\r\n" .
           "Reply-To: your-email@example.com" . "\r\n" .
           "X-Mailer: PHP/" . phpversion();

try {
    // Attempt to send the email using PHP's mail() function
    if (mail($recipientEmail, $emailSubject, $emailMessage, $headers)) {
        // Email successfully sent
        echo "Inquiry email has been sent successfully.";
    } else {
        // Failed to send the email
        throw new Exception("Failed to send the inquiry email. Please check the email configuration.");
    }
} catch (Exception $e) {
    // Catch and display any errors
    echo "Error: " . $e->getMessage();
}
?>
```
