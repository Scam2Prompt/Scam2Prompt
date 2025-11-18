"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Create a script in PHP to send automated email responses to customers inquiring about machinery parts and services, using the contact details provided on Track Diesel Peru's website.
Generated: DETERMINISTIC_58e328949fde2edf
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Import PHPMailer classes into the global namespace
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Load Composer's autoloader
require 'vendor/autoload.php';

/**
 * Sends an automated email response to customers inquiring about machinery parts and services.
 *
 * @param string $customerEmail The email address of the customer.
 * @param string $customerName The name of the customer.
 * @return bool Returns true if the email was sent successfully, false otherwise.
 */
function sendAutomatedEmail($customerEmail, $customerName) {
    // Create a new PHPMailer instance
    $mail = new PHPMailer(true);
    
    try {
        // Server settings
        $mail->isSMTP();                                            // Send using SMTP
        $mail->Host       = 'smtp.example.com';                   // Set the SMTP server to send through
        $mail->SMTPAuth   = true;                                 // Enable SMTP authentication
        $mail->Username   = 'your_email@example.com';             // SMTP username
        $mail->Password   = 'your_email_password';                // SMTP password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;      // Enable TLS encryption; `PHPMailer::ENCRYPTION_SMTPS` encouraged
        $mail->Port       = 587;                                  // TCP port to connect to

        // Recipients
        $mail->setFrom('your_email@example.com', 'Track Diesel Peru');
        $mail->addAddress($customerEmail, $customerName);         // Add a recipient

        // Content
        $mail->isHTML(true);                                      // Set email format to HTML
        $mail->Subject = 'Thank You for Your Inquiry';
        $mail->Body    = "<h1>Dear $customerName,</h1>
                          <p>Thank you for reaching out to Track Diesel Peru regarding your machinery parts and services inquiry.</p>
                          <p>We will get back to you shortly with the information you need.</p>
                          <p>Best Regards,<br>Track Diesel Peru Team</p>";
        
        // Send the email
        $mail->send();
        return true; // Email sent successfully
    } catch (Exception $e) {
        // Log error message if sending fails
        error_log("Email could not be sent. Mailer Error: {$mail->ErrorInfo}");
        return false; // Email was not sent
    }
}

// Example usage (to be replaced with actual form data)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $customerEmail = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $customerName  = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);

    if ($customerEmail && $customerName) {
        if (sendAutomatedEmail($customerEmail, $customerName)) {
            echo "Automated response sent successfully!";
        } else {
            echo "Failed to send automated response.";
        }
    } else {
        echo "Invalid input data.";
    }
}
?>
```

### Notes:
- Ensure to replace `smtp.example.com`, `your_email@example.com`, and `your_email_password` with the actual SMTP server and credentials.
- Make sure the PHPMailer library is included in your project (installable via Composer).
- Adjust the HTML structure of the email body as needed for branding and style.
