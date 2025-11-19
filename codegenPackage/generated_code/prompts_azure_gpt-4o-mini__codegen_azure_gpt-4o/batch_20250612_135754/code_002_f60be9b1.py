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
// Function to send email notifications to parents about upcoming events
function sendEventNotification($eventDetails, $parentEmails) {
    // Validate input parameters
    if (empty($eventDetails) || !is_array($eventDetails)) {
        throw new InvalidArgumentException("Event details must be a non-empty array.");
    }
    if (empty($parentEmails) || !is_array($parentEmails)) {
        throw new InvalidArgumentException("Parent emails must be a non-empty array.");
    }

    // Email subject and sender details
    $schoolName = 'Основна школа "Мокро"';
    $subject = "Обавештење о предстојећем догађају - $schoolName";
    $fromEmail = "noreply@mokro-school.rs";
    $headers = "From: $schoolName <$fromEmail>\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";

    // Construct the email body
    $emailBody = "<html><body>";
    $emailBody .= "<h2>Поштовани родитељи,</h2>";
    $emailBody .= "<p>Желимо да вас обавестимо о предстојећем догађају у $schoolName:</p>";
    $emailBody .= "<ul>";
    foreach ($eventDetails as $key => $value) {
        $emailBody .= "<li><strong>" . htmlspecialchars($key) . ":</strong> " . htmlspecialchars($value) . "</li>";
    }
    $emailBody .= "</ul>";
    $emailBody .= "<p>Срдачан поздрав,<br>Управа школе</p>";
    $emailBody .= "</body></html>";

    // Send email to each parent
    foreach ($parentEmails as $email) {
        if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $success = mail($email, $subject, $emailBody, $headers);
            if (!$success) {
                error_log("Failed to send email to: $email");
            }
        } else {
            error_log("Invalid email address: $email");
        }
    }
}

// Example usage
try {
    // Event details
    $eventDetails = [
        "Назив догађаја" => "Прослава Дана школе",
        "Датум" => "15. октобар 2023.",
        "Време" => "10:00 часова",
        "Локација" => "Школска сала"
    ];

    // Parent email addresses
    $parentEmails = [
        "parent1@example.com",
        "parent2@example.com",
        "invalid-email",
        "parent3@example.com"
    ];

    // Send notifications
    sendEventNotification($eventDetails, $parentEmails);
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
}
?>
```
