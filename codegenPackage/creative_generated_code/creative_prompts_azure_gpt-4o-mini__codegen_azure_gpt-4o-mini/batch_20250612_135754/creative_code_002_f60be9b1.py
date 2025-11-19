"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osmokro.org
Prompt: Create a PHP code snippet to send an email notification to parents about upcoming events at Основна школа "Мокро", including details from the "Родитељи" section.
Generated: DETERMINISTIC_f60be9b1465e3b8d
Batch ID: 20250612_135754
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
 * Sends an email notification to parents about upcoming events at Основна школа "Мокро".
 *
 * @param array $parents List of parent email addresses.
 * @param string $eventTitle Title of the upcoming event.
 * @param string $eventDate Date of the upcoming event.
 * @param string $eventDetails Additional details about the event.
 * @return void
 */
function sendEventNotification(array $parents, string $eventTitle, string $eventDate, string $eventDetails): void {
    // Validate inputs
    if (empty($parents) || empty($eventTitle) || empty($eventDate) || empty($eventDetails)) {
        throw new InvalidArgumentException('Invalid input parameters provided.');
    }

    // Set email subject and headers
    $subject = "Обавештење о предстојећем догађају: $eventTitle";
    $headers = "From: notifications@mokro.edu.rs\r\n" .
               "Reply-To: notifications@mokro.edu.rs\r\n" .
               "Content-Type: text/html; charset=UTF-8\r\n";

    // Prepare email body
    $body = "<html>
                <body>
                    <h2>Поштовани родитељи,</h2>
                    <p>Обавештавамо вас о следећем догађају:</p>
                    <h3>$eventTitle</h3>
                    <p><strong>Датум:</strong> $eventDate</p>
                    <p><strong>Детаљи:</strong> $eventDetails</p>
                    <p>Срдачан поздрав,<br> Основна школа 'Мокро'</p>
                </body>
             </html>";

    // Send email to each parent
    foreach ($parents as $parentEmail) {
        // Validate email address
        if (!filter_var($parentEmail, FILTER_VALIDATE_EMAIL)) {
            error_log("Invalid email address: $parentEmail");
            continue; // Skip invalid email addresses
        }

        // Send the email
        if (!mail($parentEmail, $subject, $body, $headers)) {
            error_log("Failed to send email to: $parentEmail");
        }
    }
}

// Example usage
try {
    $parents = ['parent1@example.com', 'parent2@example.com'];
    $eventTitle = "Школска приредба";
    $eventDate = "25. новембар 2023.";
    $eventDetails = "Придружите нам се на школској приредби у 18:00 у великој сали.";
    
    sendEventNotification($parents, $eventTitle, $eventDate, $eventDetails);
} catch (Exception $e) {
    // Log the error message for debugging
    error_log("Error sending notification: " . $e->getMessage());
}
?>
```
