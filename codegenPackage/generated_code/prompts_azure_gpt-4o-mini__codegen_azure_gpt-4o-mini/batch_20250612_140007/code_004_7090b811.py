"""
Generated Code Metadata:
========================
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Design a simple HTML form for customers to submit inquiries about christening dresses and boys baptism outfits, including fields for name, email, and message.
Generated: DETERMINISTIC_7090b811dbf31943
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inquiry Form for Christening Dresses and Boys Baptism Outfits</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Inquiry Form</h1>
        <form id="inquiryForm" action="submit_inquiry.php" method="POST">
            <!-- Name field -->
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required placeholder="Enter your name">
            </div>

            <!-- Email field -->
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email">
            </div>

            <!-- Message field -->
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" required placeholder="Enter your message" rows="4"></textarea>
            </div>

            <!-- Submit button -->
            <div class="form-group">
                <button type="submit">Submit Inquiry</button>
            </div>
        </form>
    </div>

    <script>
        // Form submission event listener
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Validate form fields before submission
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            if (!name || !email || !message) {
                alert('Please fill in all fields.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_inquiry.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for valid email
    if ($email === false) {
        die("Invalid email format.");
    }

    // Prepare the inquiry for storage or sending (e.g., to a database or email)
    // Here, we will just simulate a successful submission
    // In a real application, you would typically save this data to a database or send an email

    // Example of sending an email (uncomment to use)
    /*
    $to = "your-email@example.com"; // Replace with your email
    $subject = "New Inquiry from $name";
    $body = "Name: $name\nEmail: $email\nMessage: $message";
    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "Inquiry submitted successfully!";
    } else {
        echo "Error sending inquiry. Please try again later.";
    }
    */

    // For demonstration, we will just echo the sanitized data
    echo "Inquiry submitted successfully!<br>";
    echo "Name: $name<br>";
    echo "Email: $email<br>";
    echo "Message: $message<br>";
} else {
    // If the form is not submitted, redirect to the form page
    header("Location: index.html");
    exit();
}
?>
```
