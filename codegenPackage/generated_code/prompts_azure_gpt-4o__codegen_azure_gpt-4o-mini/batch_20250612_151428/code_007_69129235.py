"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Generate code in PHP to send automated email notifications to NSW Police about film shoots involving hired police uniforms, ensuring compliance with the recommendations on Powered Production Film Services.
Generated: DETERMINISTIC_6912923569486ebd
Batch ID: 20250612_151428
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
 * Class EmailNotification
 * Handles the sending of automated email notifications to NSW Police
 * regarding film shoots involving hired police uniforms.
 */
class EmailNotification
{
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
    public function __construct($to, $subject, $message)
    {
        $this->to = $to;
        $this->subject = $subject;
        $this->message = $message;
        $this->headers = "From: noreply@filmproduction.com\r\n" .
                        "Reply-To: noreply@filmproduction.com\r\n" .
                        "Content-Type: text/plain; charset=UTF-8\r\n";
    }

    /**
     * Sends the email notification.
     *
     * @return bool True on success, false on failure.
     */
    public function send()
    {
        // Validate email address
        if (!filter_var($this->to, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException("Invalid email address: " . $this->to);
        }

        // Attempt to send the email
        if (mail($this->to, $this->subject, $this->message, $this->headers)) {
            return true;
        } else {
            throw new RuntimeException("Failed to send email to: " . $this->to);
        }
    }
}

/**
 * Function to prepare and send notification about film shoots.
 *
 * @param string $recipientEmail Email address of the recipient.
 * @param string $filmTitle Title of the film.
 * @param string $shootDate Date of the film shoot.
 * @param string $location Location of the film shoot.
 * @return void
 */
function notifyNSWPolice($recipientEmail, $filmTitle, $shootDate, $location)
{
    // Prepare email subject and message
    $subject = "Notification of Film Shoot: " . $filmTitle;
    $message = "Dear NSW Police,\n\n" .
               "This is to inform you about an upcoming film shoot involving hired police uniforms.\n" .
               "Film Title: $filmTitle\n" .
               "Shoot Date: $shootDate\n" .
               "Location: $location\n\n" .
               "Please ensure compliance with the recommendations on Powered Production Film Services.\n\n" .
               "Best regards,\n" .
               "Film Production Team";

    // Create an instance of EmailNotification
    $emailNotification = new EmailNotification($recipientEmail, $subject, $message);

    // Send the email and handle any exceptions
    try {
        $emailNotification->send();
        echo "Notification sent successfully to $recipientEmail.\n";
    } catch (Exception $e) {
        // Log the error message (could be to a file or monitoring system)
        error_log($e->getMessage());
        echo "Error sending notification: " . $e->getMessage() . "\n";
    }
}

// Example usage
$recipientEmail = "nswpolice@example.com";
$filmTitle = "The Great Chase";
$shootDate = "2023-11-15";
$location = "Sydney CBD";

// Notify NSW Police about the film shoot
notifyNSWPolice($recipientEmail, $filmTitle, $shootDate, $location);

?>
```
