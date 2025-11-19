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
/**
 * Sends an email confirmation to students after they submit their application
 * for the B.Sc. in Medical Lab Technology at Ayushman College.
 *
 * @param string $studentEmail The email address of the student.
 * @param string $studentName The name of the student.
 * @return bool True on success, false on failure.
 */
function sendApplicationConfirmation($studentEmail, $studentName) {
    // Validate the email address
    if (!filter_var($studentEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email format: $studentEmail");
    }

    // Set the email subject and message
    $subject = "Application Confirmation - B.Sc. in Medical Lab Technology";
    $message = "Dear $studentName,\n\nThank you for submitting your application for the B.Sc. in Medical Lab Technology program at Ayushman College. We appreciate your interest in our college and will review your application shortly.\n\nBest regards,\nAyushman College Admissions Team";

    // Set the headers for the email
    $headers = "From: admissions@ayushmancollege.edu\n";
    $headers .= "Reply-To: admissions@ayushmancollege.edu\n";
    $headers .= "Content-Type: text/plain; charset=utf-8\n";

    // Send the email and handle errors
    if (mail($studentEmail, $subject, $message, $headers)) {
        return true; // Email sent successfully
    } else {
        // Log the error or handle it appropriately
        error_log("Failed to send email to: $studentEmail");
        return false; // Email failed to send
    }
}

// Example usage
try {
    $studentEmail = "student@example.com"; // Replace with the actual student email
    $studentName = "John Doe"; // Replace with the actual student name
    if (sendApplicationConfirmation($studentEmail, $studentName)) {
        echo "Confirmation email sent successfully.";
    } else {
        echo "Failed to send confirmation email.";
    }
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . $e->getMessage();
}
?>
```
