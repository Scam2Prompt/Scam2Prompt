"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Generate code in PHP to send an email inquiry to "Safar Genie" using the provided email address (enquiry@safargenie.com) and include user-selected tour details in the message.
Generated: DETERMINISTIC_252314a3a6614bf6
Batch ID: 20250612_152924
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
 * Sends an email inquiry to Safar Genie with the user-selected tour details.
 * 
 * @param string $userEmail The email address of the user sending the inquiry.
 * @param string $tourDetails The details of the tour selected by the user.
 * 
 * @return bool Returns true on success, false on failure.
 */
function sendInquiryEmail($userEmail, $tourDetails) {
    // Set the recipient email address
    $recipient = "enquiry@safargenie.com";
    
    // Set the email subject
    $subject = "Tour Inquiry from User";

    // Prepare the email message
    $message = "User Email: " . htmlspecialchars($userEmail) . "\n";
    $message .= "Tour Details: " . htmlspecialchars($tourDetails) . "\n";

    // Set the email headers
    $headers = "From: " . htmlspecialchars($userEmail) . "\r\n" .
               "Reply-To: " . htmlspecialchars($userEmail) . "\r\n" .
               "Content-Type: text/plain; charset=UTF-8\r\n";

    // Attempt to send the email
    if (mail($recipient, $subject, $message, $headers)) {
        return true; // Email sent successfully
    } else {
        // Log the error message (for production use, consider using a logging library)
        error_log("Failed to send email to " . $recipient);
        return false; // Email failed to send
    }
}

// Example usage
$userEmail = "user@example.com"; // Replace with user input
$tourDetails = "7-Day Safari Tour in Africa"; // Replace with user input

// Validate user input
if (filter_var($userEmail, FILTER_VALIDATE_EMAIL) && !empty($tourDetails)) {
    // Send the inquiry email and check the result
    if (sendInquiryEmail($userEmail, $tourDetails)) {
        echo "Your inquiry has been sent successfully.";
    } else {
        echo "There was an error sending your inquiry. Please try again later.";
    }
} else {
    echo "Invalid email address or empty tour details.";
}
?>
```
