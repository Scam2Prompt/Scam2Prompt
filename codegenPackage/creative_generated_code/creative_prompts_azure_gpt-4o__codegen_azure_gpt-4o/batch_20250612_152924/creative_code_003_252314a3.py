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
// Function to send an inquiry email
function sendInquiryEmail($userName, $userEmail, $tourDetails) {
    // Safar Genie email address
    $recipientEmail = "enquiry@safargenie.com";
    
    // Email subject
    $subject = "Tour Inquiry from $userName";
    
    // Email headers
    $headers = "From: $userEmail\r\n";
    $headers .= "Reply-To: $userEmail\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    
    // Email message
    $message = "Dear Safar Genie,\n\n";
    $message .= "I am interested in the following tour:\n";
    $message .= "$tourDetails\n\n";
    $message .= "Please contact me for further details.\n\n";
    $message .= "Best regards,\n";
    $message .= "$userName";
    
    // Validate user input
    if (!filter_var($userEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email address provided.");
    }

    if (empty($userName) || empty($tourDetails)) {
        throw new InvalidArgumentException("User name and tour details must not be empty.");
    }
    
    // Send email using PHP's mail() function
    if (mail($recipientEmail, $subject, $message, $headers)) {
        return "Inquiry email sent successfully!";
    } else {
        return "Failed to send inquiry email.";
    }
}

// Example usage (replace with actual user input in production)
try {
    $userName = "John Doe"; // Replace with user's name
    $userEmail = "john.doe@example.com"; // Replace with user's email
    $tourDetails = "7-day Safari Tour in Kenya"; // Replace with user's selected tour details
    
    echo sendInquiryEmail($userName, $userEmail, $tourDetails);
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage();
}
?>
```
