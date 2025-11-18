"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kesug.com
Prompt: Create a PHP script to send an email notification when harmful content is detected on a kesug.com subdomain, with a report sent to InfinityFree's abuse email.
Generated: DETERMINISTIC_c7542cc21678c8d9
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Set the recipient email for abuse reporting
define('ABUSE_EMAIL', 'abuse@infinityfree.net');

// Function to send email notification
function sendEmailNotification($subject, $message) {
    // Set the headers for the email
    $headers = "From: noreply@kesug.com\r\n" .
               "Reply-To: noreply@kesug.com\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Send the email
    if (!mail(ABUSE_EMAIL, $subject, $message, $headers)) {
        error_log("Email sending failed: " . error_get_last()['message']); // Log error if mail fails
        return false;
    }
    return true;
}

// Function to check for harmful content (dummy implementation for illustration)
function detectHarmfulContent($content) {
    // List of harmful keywords for demonstration purposes
    $harmfulKeywords = ['malware', 'phishing', 'spam'];

    // Check if the content contains any harmful keywords
    foreach ($harmfulKeywords as $keyword) {
        if (stripos($content, $keyword) !== false) {
            return true; // Harmful content detected
        }
    }
    return false; // No harmful content found
}

// Main script execution
try {
    // Simulated content to check (this would typically come from user input or a database)
    $contentToCheck = "This is a test message containing malware.";

    // Check for harmful content
    if (detectHarmfulContent($contentToCheck)) {
        // Prepare email subject and message
        $subject = "Harmful Content Detected on kesug.com Subdomain";
        $message = "Harmful content has been detected:\n\n" . $contentToCheck;

        // Send email notification
        if (sendEmailNotification($subject, $message)) {
            echo "Email notification sent successfully.";
        } else {
            echo "Failed to send email notification.";
        }
    } else {
        echo "No harmful content detected.";
    }
} catch (Exception $e) {
    // Handle any exceptions and log the error
    error_log("An error occurred: " . $e->getMessage());
    echo "An error occurred while processing your request.";
}
?>
```
