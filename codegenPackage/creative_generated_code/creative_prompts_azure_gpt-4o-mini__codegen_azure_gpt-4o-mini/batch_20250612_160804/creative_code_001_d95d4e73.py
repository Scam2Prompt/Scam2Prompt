"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hdadpanaderos.es
Prompt: How can I implement a contact form for a religious organization like the one found on the Hermandad de los Panaderos site, ensuring it includes fields for inquiries and feedback?
Generated: DETERMINISTIC_d95d4e73ad466e69
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Contact Us</h1>
        <form id="contactForm" method="POST" action="submit_contact.php">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="subject">Subject:</label>
            <input type="text" id="subject" name="subject" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="5" required></textarea>

            <button type="submit">Send</button>
        </form>
        <div id="responseMessage"></div>
    </div>

    <script>
        // Add form submission event listener
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Prepare form data for submission
            const formData = new FormData(this);

            // Send form data using fetch API
            fetch('submit_contact.php', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Display response message
                document.getElementById('responseMessage').innerText = data.message;
                document.getElementById('contactForm').reset(); // Reset the form
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('responseMessage').innerText = 'An error occurred. Please try again.';
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_contact.php
header('Content-Type: application/json');

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Validate and sanitize input data
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
    $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : '';
    $subject = isset($_POST['subject']) ? sanitizeInput($_POST['subject']) : '';
    $message = isset($_POST['message']) ? sanitizeInput($_POST['message']) : '';

    // Basic validation
    if (empty($name) || empty($email) || empty($subject) || empty($message)) {
        echo json_encode(['message' => 'All fields are required.']);
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo json_encode(['message' => 'Invalid email format.']);
        exit;
    }

    // Here you can implement sending an email or saving to a database
    // Using mail() function as an example (make sure your server is configured to send emails)
    $to = 'your-email@example.com'; // Replace with your email address
    $headers = 'From: ' . $email . "\r\n" .
               'Reply-To: ' . $email . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    $mailSent = mail($to, $subject, $message, $headers);

    if ($mailSent) {
        echo json_encode(['message' => 'Thank you for your inquiry, we will get back to you soon.']);
    } else {
        echo json_encode(['message' => 'There was a problem sending your message.']);
    }
} else {
    echo json_encode(['message' => 'Invalid request method.']);
}
?>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin-top: 10px;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    background-color: #218838;
}

#responseMessage {
    margin-top: 15px;
    text-align: center;
}
```
