"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thatcounselingplace.com
Prompt: Write a code snippet to create a contact form for a therapy website that includes fields for name, email, and message, inspired by That Counseling Place.
Generated: DETERMINISTIC_4b6e88386bb5c017
Batch ID: 20250612_162051
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
    <title>Contact Us - That Counseling Place</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Contact Us</h1>
        <form id="contactForm" method="POST" action="submit_form.php">
            <div class="form-group">
                <label for="name">Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required placeholder="Your Name">
            </div>
            <div class="form-group">
                <label for="email">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required placeholder="Your Email">
            </div>
            <div class="form-group">
                <label for="message">Message <span class="required">*</span></label>
                <textarea id="message" name="message" required placeholder="Your Message" rows="5"></textarea>
            </div>
            <button type="submit">Send Message</button>
        </form>
        <div id="formResponse" class="response"></div> <!-- Placeholder for form submission response -->
    </div>

    <script>
        // Handle form submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send form data to the server
            fetch('submit_form.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.text();
            })
            .then(data => {
                document.getElementById('formResponse').innerHTML = data; // Display success message
                this.reset(); // Reset form after successful submission
            })
            .catch(error => {
                document.getElementById('formResponse').textContent = 'Error: ' + error.message; // Display error message
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for errors
    if (!$name || !$email || !$message) {
        http_response_code(400);
        echo "Please fill out all fields correctly.";
        exit;
    }

    // Send email (this is a placeholder; configure mail server settings accordingly)
    $to = 'contact@thatcounselingplace.com';
    $subject = 'New Contact Form Submission';
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    
    // Attempt to send the email
    if (mail($to, $subject, $body)) {
        echo "Thank you for your message, we will get back to you soon!";
    } else {
        http_response_code(500);
        echo "There was an error sending your message. Please try again later.";
    }
} else {
    http_response_code(405);
    echo "Method Not Allowed. Please use POST to submit the form.";
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
    padding: 20px;
    background: white;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"], input[type="email"], textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

.response {
    margin-top: 15px;
    text-align: center;
    color: red; /* Default error message color */
}

.required {
    color: red;
}
```
