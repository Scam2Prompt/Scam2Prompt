"""
Generated Code Metadata:
========================
Original URL: https://rapala.tc
Prompt: Generate a sample code for a travel concierge website's contact form, including fields for client information, travel preferences, and message, similar to the one on Rapala.tc.
Generated: DETERMINISTIC_e0e55aa2b2cb907f
Batch ID: 20250622_210655
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
    <title>Travel Concierge Contact Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Contact Us</h1>
        <form id="contactForm" action="submit_form.php" method="POST">
            <!-- Client Information Section -->
            <fieldset>
                <legend>Client Information</legend>
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="John Doe">

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="example@example.com">

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="+1234567890">
            </fieldset>

            <!-- Travel Preferences Section -->
            <fieldset>
                <legend>Travel Preferences</legend>
                <label for="destination">Preferred Destination:</label>
                <input type="text" id="destination" name="destination" required placeholder="e.g., Bali">

                <label for="travelDate">Travel Date:</label>
                <input type="date" id="travelDate" name="travelDate" required>

                <label for="travelType">Type of Travel:</label>
                <select id="travelType" name="travelType" required>
                    <option value="">Select...</option>
                    <option value="leisure">Leisure</option>
                    <option value="business">Business</option>
                    <option value="adventure">Adventure</option>
                </select>
            </fieldset>

            <!-- Message Section -->
            <fieldset>
                <legend>Your Message</legend>
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required placeholder="Tell us about your travel plans..."></textarea>
            </fieldset>

            <!-- Submit Button -->
            <button type="submit">Submit</button>
        </form>
    </div>

    <script src="script.js"></script> <!-- Link to external JavaScript for form validation -->
</body>
</html>
```

```php
<?php
// submit_form.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $destination = filter_input(INPUT_POST, 'destination', FILTER_SANITIZE_STRING);
    $travelDate = filter_input(INPUT_POST, 'travelDate', FILTER_SANITIZE_STRING);
    $travelType = filter_input(INPUT_POST, 'travelType', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for validation errors
    if (!$email) {
        die("Invalid email format.");
    }

    // Prepare email content
    $to = "concierge@example.com"; // Change to your email address
    $subject = "New Travel Inquiry from $name";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\nDestination: $destination\nTravel Date: $travelDate\nType of Travel: $travelType\nMessage: $message";
    $headers = "From: $email";

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        echo "Thank you for your inquiry, $name. We will get back to you shortly.";
    } else {
        echo "There was an error sending your message. Please try again later.";
    }
} else {
    // Redirect to the contact form if accessed directly
    header("Location: index.html");
    exit();
}
?>
```

```css
/* styles.css */

/* Basic styling for the contact form */
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

fieldset {
    border: 1px solid #ccc;
    margin-bottom: 20px;
    padding: 10px;
}

legend {
    font-weight: bold;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"],
input[type="email"],
input[type="tel"],
input[type="date"],
select,
textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}
```

```javascript
// script.js

// Basic form validation
document.getElementById('contactForm').addEventListener('submit', function(event) {
    let valid = true;

    // Check if all required fields are filled
    const requiredFields = ['name', 'email', 'phone', 'destination', 'travelDate', 'travelType', 'message'];
    requiredFields.forEach(function(field) {
        const input = document.getElementById(field);
        if (!input.value) {
            valid = false;
            input.style.borderColor = 'red'; // Highlight empty fields
        } else {
            input.style.borderColor = ''; // Reset border color
        }
    });

    if (!valid) {
        event.preventDefault(); // Prevent form submission if validation fails
        alert('Please fill in all required fields.');
    }
});
```
