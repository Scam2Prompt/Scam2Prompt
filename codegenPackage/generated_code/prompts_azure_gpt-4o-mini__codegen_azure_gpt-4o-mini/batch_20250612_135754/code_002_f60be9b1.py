"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Create a PHP code snippet to send an email notification to parents about upcoming events at Основна школа "Мокро", including details from the "Родитељи" section.
Generated: DETERMINISTIC_f60be9b1465e3b8d
Batch ID: 20250612_135754
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
 * Sends an email notification to parents about upcoming events at Основна школа "Мокро".
 *
 * @param array $parents List of parents' email addresses.
 * @param string $eventTitle Title of the upcoming event.
 * @param string $eventDate Date of the upcoming event.
 * @param string $eventDetails Additional details about the event.
 * @return void
 */
function sendEventNotification(array $parents, string $eventTitle, string $eventDate, string $eventDetails): void {
    // Validate input parameters
    if (empty($parents) || empty($eventTitle) || empty($eventDate) || empty($eventDetails)) {
        throw new InvalidArgumentException('All parameters are required.');
    }

    // Email subject and headers
    $subject = "Upcoming Event: $eventTitle";
    $headers = "From: no-reply@mokroschool.edu\n";
    $headers .= "Reply-To: no-reply@mokroschool.edu\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\n";

    // Email body
    $message = "<html><body>";
    $message .= "<h1>Dear Parents,</h1>";
    $message .= "<p>We are excited to inform you about an upcoming event:</p>";
    $message .= "<h2>$eventTitle</h2>";
    $message .= "<p><strong>Date:</strong> $eventDate</p>";
    $message .= "<p><strong>Details:</strong> $eventDetails</p>";
    $message .= "<p>We look forward to seeing you there!</p>";
    $message .= "<p>Best regards,<br>Основна школа \"Мокро\"</p>";
    $message .= "</body></html>";

    // Send email to each parent
    foreach ($parents as $parentEmail) {
        // Validate email address
        if (!filter_var($parentEmail, FILTER_VALIDATE_EMAIL)) {
            error_log("Invalid email address: $parentEmail");
            continue; // Skip invalid email addresses
        }

        // Attempt to send the email
        if (!mail($parentEmail, $subject, $message, $headers)) {
            error_log("Failed to send email to: $parentEmail");
        }
    }
}

// Example usage
try {
    $parents = ['parent1@example.com', 'parent2@example.com']; // Replace with actual email addresses
    $eventTitle = "School Annual Day";
    $eventDate = "2023-12-15";
    $eventDetails = "Join us for a day of fun, food, and festivities!";
    
    sendEventNotification($parents, $eventTitle, $eventDate, $eventDetails);
} catch (Exception $e) {
    error_log("Error sending event notification: " . $e->getMessage());
}
?>
```
