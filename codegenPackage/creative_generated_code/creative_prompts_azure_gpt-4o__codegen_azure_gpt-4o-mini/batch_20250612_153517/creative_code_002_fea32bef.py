"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchlawinc.com
Prompt: Generate code for a "Contact Us" form tailored for a legal services website, incorporating fields like name, email, and inquiry type, inspired by the Launch Law site.
Generated: DETERMINISTIC_fea32befe27a36af
Batch ID: 20250612_153517
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
    <title>Contact Us - Legal Services</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>

<body>
    <header>
        <h1>Contact Us</h1>
        <p>We are here to assist you with your legal needs.</p>
    </header>

    <main>
        <form id="contactForm" action="submitContactForm.php" method="POST">
            <label for="name">Name <span class="required">*</span></label>
            <input type="text" id="name" name="name" required placeholder="Your Full Name">

            <label for="email">Email <span class="required">*</span></label>
            <input type="email" id="email" name="email" required placeholder="Your Email Address">

            <label for="inquiryType">Type of Inquiry <span class="required">*</span></label>
            <select id="inquiryType" name="inquiryType" required>
                <option value="" disabled selected>Select an option</option>
                <option value="consultation">Consultation</option>
                <option value="legal_advice">Legal Advice</option>
                <option value="document_review">Document Review</option>
                <option value="other">Other</option>
            </select>

            <label for="message">Message</label>
            <textarea id="message" name="message" rows="4" placeholder="Your Message (optional)"></textarea>

            <button type="submit">Submit</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Legal Services. All rights reserved.</p>
    </footer>

    <script>
        // Form submission event handler
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            // Prevent form from submitting until validations are checked
            let isValid = true;

            // Check required fields
            const requiredFields = ['name', 'email', 'inquiryType'];
            requiredFields.forEach(function(field) {
                const input = document.getElementById(field);
                if (!input.value) {
                    isValid = false;
                    input.classList.add('error'); // Highlight invalid fields
                } else {
                    input.classList.remove('error');
                }
            });

            // If form is not valid, prevent submission
            if (!isValid) {
                event.preventDefault();
                alert('Please fill out all required fields.');
            }
        });
    </script>
</body>

</html>
```

```php
<?php
// submitContactForm.php

// Start session to manage potential error messaging
session_start();

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize inputs
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
    $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : '';
    $inquiryType = isset($_POST['inquiryType']) ? sanitizeInput($_POST['inquiryType']) : '';
    $message = isset($_POST['message']) ? sanitizeInput($_POST['message']) : '';

    // Check if required fields are filled
    if (empty($name) || empty($email) || empty($inquiryType)) {
        $_SESSION['error'] = 'All fields marked with * are required.';
        header('Location: contact_us.php'); // Redirect back to contact form
        exit;
    }

    // Prepare email components
    $to = "info@legalservices.com"; // Change to your email address
    $subject = "New Inquiry from Contact Us Form";
    $body = "Name: $name\nEmail: $email\nInquiry Type: $inquiryType\nMessage: $message";
    $headers = "From: $email";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        $_SESSION['success'] = 'Your message has been sent successfully!';
    } else {
        $_SESSION['error'] = 'There was an error sending your message. Please try again later.';
    }

    // Redirect back to contact form after submission
    header('Location: contact_us.php');
    exit;
}
?>
```

```css
/* styles.css */

/* Basic reset for styling */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #0044cc;
    color: white;
    text-align: center;
    padding: 10px 0;
}

h1 {
    margin: 0;
}

main {
    padding: 20px;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin: 10px 0 5px;
}

input, select, textarea {
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    padding: 10px;
    background-color: #0044cc;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #003399;
}

.required {
    color: red;
}

.error {
    border-color: red; /* Highlight invalid fields */
}

footer {
    text-align: center;
    padding: 10px;
    background-color: #f1f1f1;
}
```
