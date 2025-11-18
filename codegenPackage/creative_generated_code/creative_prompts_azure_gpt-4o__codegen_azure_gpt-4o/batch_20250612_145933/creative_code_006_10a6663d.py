"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Generate PHP code for a contact form on "The Balcone Suites & Resort" website that sends inquiries to [email protected] and includes fields for name, email, phone number, and message.
Generated: DETERMINISTIC_10a6663db5056f90
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact form handler for "The Balcone Suites & Resort"

// Define recipient email
define('RECIPIENT_EMAIL', '[email protected]');

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Prepare response messages
    $errors = [];
    $successMessage = '';

    // Validate required fields
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }
    if (empty($email)) {
        $errors[] = 'Valid email is required.';
    }
    if (empty($phone)) {
        $errors[] = 'Phone number is required.';
    }
    if (empty($message)) {
        $errors[] = 'Message is required.';
    }

    // Proceed if no errors
    if (empty($errors)) {
        // Compose email
        $subject = 'Contact Inquiry from The Balcone Suites & Resort Website';
        $body = "You have received a new inquiry:\n\n" .
                "Name: $name\n" .
                "Email: $email\n" .
                "Phone: $phone\n\n" .
                "Message:\n$message";

        $headers = "From: no-reply@thebalconesuites.com\r\n" .
                   "Reply-To: $email\r\n" .
                   "Content-Type: text/plain; charset=UTF-8";

        // Send email
        if (mail(RECIPIENT_EMAIL, $subject, $body, $headers)) {
            $successMessage = 'Your inquiry has been sent successfully!';
        } else {
            $errors[] = 'There was an error sending your inquiry. Please try again later.';
        }
    }

    // Output JSON response (for an AJAX-based form submission)
    header('Content-Type: application/json');
    echo json_encode([
        'success' => empty($errors),
        'errors' => $errors,
        'message' => $successMessage,
    ]);
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us | The Balcone Suites & Resort</title>
    <link rel="stylesheet" href="styles.css"> <!-- Replace with actual stylesheet -->
</head>
<body>
    <h1>Contact Us</h1>
    <form id="contactForm" method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="phone">Phone Number:</label>
        <input type="text" id="phone" name="phone" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        
        <button type="submit">Send Inquiry</button>
    </form>

    <script>
        // Optional JavaScript to handle form submission via AJAX
        document.getElementById('contactForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission
            const formData = new FormData(event.target);

            fetch('', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                    event.target.reset(); // Reset form on successful submission
                } else {
                    alert('Errors:\n' + data.errors.join('\n'));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An unexpected error occurred. Please try again.');
            });
        });
    </script>
</body>
</html>
```
