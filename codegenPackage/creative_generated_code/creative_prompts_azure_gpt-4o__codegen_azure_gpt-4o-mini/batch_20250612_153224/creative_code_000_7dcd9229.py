"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Write code to create a contact form for a web design agency, similar to the one described on digistrategy.in, including error handling for form submission.
Generated: DETERMINISTIC_7dcd9229958276c6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- contact-form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Web Design Agency</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="contact-form-container">
        <h1>Contact Us</h1>
        <form id="contactForm" method="POST" action="submit_form.php">
            <div class="form-group">
                <label for="name">Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="subject">Subject <span class="required">*</span></label>
                <input type="text" id="subject" name="subject" required>
            </div>
            <div class="form-group">
                <label for="message">Message <span class="required">*</span></label>
                <textarea id="message" name="message" required></textarea>
            </div>
            <button type="submit">Send Message</button>
            <div id="formResponse" class="response-message"></div>
        </form>
    </div>

    <script>
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            const formData = new FormData(this);

            // Send the form data using fetch
            fetch('submit_form.php', {
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.text();
            })
            .then(data => {
                document.getElementById('formResponse').innerText = data; // Display success message
                this.reset(); // Reset the form fields
            })
            .catch(error => {
                document.getElementById('formResponse').innerText = 'Error: ' + error.message; // Display error message
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate input fields
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $subject = filter_input(INPUT_POST, 'subject', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for validation errors
    if (empty($name) || empty($email) || empty($subject) || empty($message)) {
        http_response_code(400);
        echo "All fields are required.";
        exit;
    }

    if (!$email) {
        http_response_code(400);
        echo "Invalid email address.";
        exit;
    }

    // Here you would typically send an email or save to a database
    // For demonstration, we will just simulate a successful submission
    // mail($to, $subject, $message, $headers);

    // Send a success response
    http_response_code(200);
    echo "Thank you for contacting us, we will get back to you shortly.";
} else {
    // Method not allowed
    http_response_code(405);
    echo "Method not allowed.";
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

.contact-form-container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
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

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

textarea {
    height: 100px;
}

button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.response-message {
    margin-top: 15px;
    color: red;
    text-align: center;
}

.required {
    color: red;
}
```
