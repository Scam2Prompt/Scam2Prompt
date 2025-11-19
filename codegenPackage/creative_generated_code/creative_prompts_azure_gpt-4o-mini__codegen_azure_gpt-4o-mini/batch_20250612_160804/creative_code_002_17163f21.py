"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Create a PHP script to handle customer inquiries about personalized flip-flops, similar to the services offered by Surff Ojotas.
Generated: DETERMINISTIC_17163f2144e0c379
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Personalized Flip-Flops Inquiry Handler

// Start the session to handle user data
session_start();

// Constants for configuration
define('EMAIL_TO', 'support@surffojotas.com'); // Support email address
define('SUCCESS_MESSAGE', 'Thank you for your inquiry! We will get back to you soon.');
define('ERROR_MESSAGE', 'There was an error processing your request. Please try again.');

// Function to send email
function sendInquiryEmail($name, $email, $message) {
    $subject = "New Inquiry from $name";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email\r\n" .
               "Reply-To: $email\r\n" .
               "X-Mailer: PHP/" . phpversion();

    return mail(EMAIL_TO, $subject, $body, $headers);
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate required fields
    if ($name && $email && $message) {
        // Send the inquiry email
        if (sendInquiryEmail($name, $email, $message)) {
            // Set success message in session
            $_SESSION['message'] = SUCCESS_MESSAGE;
        } else {
            // Set error message in session
            $_SESSION['message'] = ERROR_MESSAGE;
        }
    } else {
        // Set error message for invalid inputs
        $_SESSION['message'] = ERROR_MESSAGE;
    }

    // Redirect to the same page to avoid form resubmission
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit();
}

// Display session message if exists
if (isset($_SESSION['message'])) {
    echo "<p>" . htmlspecialchars($_SESSION['message']) . "</p>";
    unset($_SESSION['message']); // Clear message after displaying
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personalized Flip-Flops Inquiry</title>
    <link rel="stylesheet" href="styles.css"> <!-- Optional: Link to CSS for styling -->
</head>
<body>
    <h1>Inquire About Personalized Flip-Flops</h1>
    <form action="" method="POST">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Your Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send Inquiry</button>
    </form>
</body>
</html>
```
