"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Generate code for implementing a contact form with fields for name, contact number, email, and message, as seen on Tara Media Works' website.
Generated: DETERMINISTIC_e7901287b657450c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- contact_form.html -->
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
        <form id="contactForm" method="POST" action="submit_form.php">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="contact">Contact Number:</label>
            <input type="tel" id="contact" name="contact" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <button type="submit">Send Message</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
/* Basic styles for the contact form */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

h1 {
    text-align: center;
    margin-bottom: 20px;
}

form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"], input[type="tel"], input[type="email"], textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background: #28a745;
    color: #fff;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background: #218838;
}
```

```php
<?php
// submit_form.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize form data
    $name = htmlspecialchars(trim($_POST['name']));
    $contact = htmlspecialchars(trim($_POST['contact']));
    $email = htmlspecialchars(trim($_POST['email']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Validate required fields
    if (empty($name) || empty($contact) || empty($email) || empty($message)) {
        die("All fields are required.");
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    // Prepare to send email
    $to = "info@taramediaworks.com"; // Change to your email address
    $subject = "New Contact Form Submission";
    $body = "Name: $name\nContact: $contact\nEmail: $email\nMessage:\n$message";

    // To send HTML mail, the Content-type header must be set
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    
    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        echo "Your message has been sent successfully!";
    } else {
        echo "There was a problem sending your message. Please try again later.";
    }
} else {
    // If the form is not submitted, redirect to the contact form
    header("Location: contact_form.html");
    exit;
}
?>
```

```javascript
// script.js
// Optional JavaScript for additional client-side validation or enhancements
document.getElementById('contactForm').addEventListener('submit', function(e) {
    // You can add any client-side validation here if needed
    // For example, check if fields are filled out correctly

    // Uncomment the following line to prevent form submission for testing
    // e.preventDefault();
});
```
