"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Generate PHP code for a contact form that sends service inquiries (e.g., "bathroom updating & repair") to the email "jesse.winger@protonmail.com."
Generated: DETERMINISTIC_18b18f1f7cf58ea2
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact form handler script

// Define the recipient email address
define('RECIPIENT_EMAIL', 'jesse.winger@protonmail.com');

// Check if the form was submitted via POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);
    $service = filter_input(INPUT_POST, 'service', FILTER_SANITIZE_STRING);

    // Error messages array
    $errors = [];

    // Validate required fields
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }

    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'A valid email address is required.';
    }

    if (empty($message)) {
        $errors[] = 'Message cannot be empty.';
    }

    if (empty($service)) {
        $errors[] = 'Please specify the service inquiry.';
    }

    // Check for errors before proceeding
    if (empty($errors)) {
        // Prepare email headers
        $headers = "From: $name <$email>\r\n";
        $headers .= "Reply-To: $email\r\n";
        $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

        // Create the email subject and body
        $subject = "Service Inquiry: $service";
        $emailBody = "You have received a new service inquiry.\n\n";
        $emailBody .= "Name: $name\n";
        $emailBody .= "Email: $email\n";
        $emailBody .= "Service: $service\n";
        $emailBody .= "Message:\n$message\n";

        // Send the email
        if (mail(RECIPIENT_EMAIL, $subject, $emailBody, $headers)) {
            // Email sent successfully
            echo json_encode(['success' => true, 'message' => 'Your inquiry has been sent successfully!']);
        } else {
            // Email sending failed
            echo json_encode(['success' => false, 'message' => 'Failed to send your inquiry. Please try again later.']);
        }
    } else {
        // Return validation errors
        echo json_encode(['success' => false, 'errors' => $errors]);
    }
} else {
    // Handle invalid request method
    echo json_encode(['success' => false, 'message' => 'Invalid request method.']);
}
?>
```

```html
<!-- Contact Form HTML -->
<form id="contactForm" method="POST" action="contact_form_handler.php">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="service">Service Inquiry:</label>
    <input type="text" id="service" name="service" required>

    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>

    <button type="submit">Send Inquiry</button>
</form>
```

```javascript
<!-- Optional JavaScript for AJAX submission -->
<script>
document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(this);

    fetch('contact_form_handler.php', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
        } else {
            alert(data.errors ? data.errors.join('\n') : data.message);
        }
    })
    .catch(error => console.error('Error:', error));
});
</script>
```
