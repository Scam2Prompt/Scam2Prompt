"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visitabroadtravels.com.np
Prompt: Write code in PHP to implement a contact form that sends user inquiries directly to the email address listed on the "Visit Abroad Travels" website.
Generated: DETERMINISTIC_2ae5f91f095963a3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact Form Script for "Visit Abroad Travels"

// Define recipient email address (replace this with the actual email address from the website).
$recipientEmail = "contact@visitabroadtravels.com";

// Check if the form is submitted via POST method
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize and validate user input
    $name = htmlspecialchars(strip_tags(trim($_POST["name"])));
    $email = filter_var(trim($_POST["email"]), FILTER_VALIDATE_EMAIL);
    $message = htmlspecialchars(strip_tags(trim($_POST["message"])));

    // Initialize an errors array to collect validation errors
    $errors = [];

    // Validate name
    if (empty($name)) {
        $errors[] = "Name is required.";
    }

    // Validate email
    if (empty($email)) {
        $errors[] = "Email is required.";
    } elseif ($email === false) {
        $errors[] = "Invalid email format.";
    }

    // Validate message
    if (empty($message)) {
        $errors[] = "Message is required.";
    }

    // If there are no errors, proceed to send the email
    if (empty($errors)) {
        // Email subject
        $subject = "Contact Inquiry from Visit Abroad Travels Website";

        // Email content
        $emailContent = "You have received a new contact inquiry:\n\n";
        $emailContent .= "Name: $name\n";
        $emailContent .= "Email: $email\n\n";
        $emailContent .= "Message:\n$message\n";

        // Email headers
        $headers = "From: $name <$email>" . "\r\n";
        $headers .= "Reply-To: $email" . "\r\n";

        // Send the email using the mail() function
        $isSent = mail($recipientEmail, $subject, $emailContent, $headers);

        // Check if the email was successfully sent
        if ($isSent) {
            echo "Thank you for your inquiry. Your message has been sent successfully.";
        } else {
            echo "Sorry, there was an error sending your message. Please try again later.";
        }
    } else {
        // Display errors if validation failed
        foreach ($errors as $error) {
            echo "<p style='color: red;'>$error</p>";
        }
    }
}
?>

<!-- HTML Form for Contact Inquiry -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Visit Abroad Travels</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        <br><br>

        <button type="submit">Send Message</button>
    </form>
</body>
</html>
```
