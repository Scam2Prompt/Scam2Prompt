"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Develop a code example in PHP for creating a simple email sending functionality, similar to the "Send a Message" feature on the website, using a mail server for sending emails to the counselor.
Generated: DETERMINISTIC_f6082f6ef29002a4
Batch ID: 20250622_210650
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
 * EmailSender class for sending emails to counselors.
 */
class EmailSender {
    private $to;
    private $subject;
    private $message;
    private $headers;

    /**
     * Constructor to initialize email parameters.
     *
     * @param string $to Recipient email address.
     * @param string $subject Subject of the email.
     * @param string $message Body of the email.
     */
    public function __construct($to, $subject, $message) {
        $this->to = filter_var($to, FILTER_VALIDATE_EMAIL);
        $this->subject = htmlspecialchars($subject);
        $this->message = htmlspecialchars($message);
        $this->headers = "From: no-reply@example.com\r\n" .
                        "Reply-To: no-reply@example.com\r\n" .
                        "X-Mailer: PHP/" . phpversion();

        // Validate email address
        if (!$this->to) {
            throw new InvalidArgumentException("Invalid email address provided.");
        }
    }

    /**
     * Sends the email.
     *
     * @return bool True on success, false on failure.
     */
    public function send() {
        // Attempt to send the email
        if (mail($this->to, $this->subject, $this->message, $this->headers)) {
            return true;
        } else {
            throw new RuntimeException("Email could not be sent. Please try again later.");
        }
    }
}

// Usage example
try {
    // Initialize email parameters
    $recipient = "counselor@example.com"; // Replace with actual counselor email
    $emailSubject = "New Message from User";
    $emailMessage = "Hello Counselor,\n\nThis is a message from a user.";

    // Create an instance of EmailSender
    $emailSender = new EmailSender($recipient, $emailSubject, $emailMessage);

    // Send the email
    if ($emailSender->send()) {
        echo "Email sent successfully!";
    }
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . $e->getMessage();
}
?>
```
