"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Develop a code snippet in PHP that sends an email confirmation to students after they submit their application for the B.Sc. in Medical Lab Technology at Ayushman College.
Generated: DETERMINISTIC_3cefa87aefca11a4
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ensure error reporting is enabled for debugging during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to send an email confirmation
function sendConfirmationEmail($studentEmail, $studentName) {
    // Validate email address
    if (!filter_var($studentEmail, FILTER_VALIDATE_EMAIL)) {
        throw new Exception("Invalid email address provided: " . $studentEmail);
    }

    // Subject of the email
    $subject = "Application Confirmation - B.Sc. in Medical Lab Technology";

    // Email body content
    $message = "
    Dear $studentName,\n\n
    Thank you for submitting your application for the B.Sc. in Medical Lab Technology at Ayushman College.\n
    We have successfully received your application and will review it shortly.\n
    Should you have any queries, feel free to reach out to us at admissions@ayushmancollege.edu.\n\n
    Best regards,\n
    Ayushman College Admissions Team
    ";

    // Email headers
    $headers = "From: admissions@ayushmancollege.edu\r\n";
    $headers .= "Reply-To: admissions@ayushmancollege.edu\r\n";
    $headers .= "Content-type: text/plain; charset=UTF-8\r\n";

    // Attempt to send the email
    if (mail($studentEmail, $subject, $message, $headers)) {
        return true; // Email sent successfully
    } else {
        throw new Exception("Failed to send confirmation email to " . $studentEmail);
    }
}

// Example usage
try {
    // Assume these values are collected from a form submission
    $studentEmail = "student@example.com"; // Replace with the actual email
    $studentName = "John Doe"; // Replace with the actual name

    // Call the function to send a confirmation email
    if (sendConfirmationEmail($studentEmail, $studentName)) {
        echo "Confirmation email sent successfully to $studentEmail";
    }
} catch (Exception $e) {
    // Handle and log exceptions
    error_log("Error: " . $e->getMessage());
    echo "An error occurred while sending the confirmation email. Please try again later.";
}
?>
```
