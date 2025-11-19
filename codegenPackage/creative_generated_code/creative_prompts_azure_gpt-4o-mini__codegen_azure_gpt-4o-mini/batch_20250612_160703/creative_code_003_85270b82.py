"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancermt.com
Prompt: Create a simple web form for patients to contact a massage therapist, referencing the email communication mentioned on balancermt.com.
Generated: DETERMINISTIC_85270b827d08cb2a
Batch ID: 20250612_160703
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
    <title>Contact Massage Therapist</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Contact Us</h1>
    <form id="contact-form" method="POST" action="submit_form.php">
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="4" required></textarea>

        <button type="submit">Send Message</button>
    </form>

    <script>
        // Add event listener for form submission
        document.getElementById('contact-form').addEventListener('submit', function(event) {
            // Validate form inputs if needed before submission
            // Here you can implement custom validation if necessary

            // Example: Simple email validation
            const email = document.getElementById('email').value;
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert('Please enter a valid email address.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize input data
    $name = trim(htmlspecialchars($_POST['name']));
    $email = trim(htmlspecialchars($_POST['email']));
    $phone = trim(htmlspecialchars($_POST['phone']));
    $message = trim(htmlspecialchars($_POST['message']));

    // Validate required fields
    if (empty($name) || empty($email) || empty($phone) || empty($message)) {
        die('Error: All fields are required.');
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Error: Invalid email format.');
    }

    // Prepare the email
    $to = "therapist@balancermt.com"; // Replace with the therapist's email
    $subject = "New Contact Form Submission";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\nMessage:\n$message";
    $headers = "From: $email\r\n";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        echo "Thank you for your message! We will get back to you shortly.";
    } else {
        echo "Error: Unable to send your message. Please try again later.";
    }
} else {
    // If the request method is not POST, redirect to the contact form
    header("Location: index.html");
    exit;
}
?>
```

```css
/* styles.css */

/* Basic styling for the contact form */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    text-align: center;
}

form {
    max-width: 600px;
    margin: 0 auto;
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 8px;
}

input[type="text"],
input[type="email"],
input[type="tel"],
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}
```
