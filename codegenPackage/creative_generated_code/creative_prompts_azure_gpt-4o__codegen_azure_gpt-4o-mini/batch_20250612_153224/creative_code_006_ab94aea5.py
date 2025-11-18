"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Write code to integrate a contact form for equipment inquiries, similar to the one on SCOUT.kz, with validation for phone numbers and email formats.
Generated: DETERMINISTIC_ab94aea5136ee4d0
Batch ID: 20250612_153224
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
    <title>Equipment Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Equipment Inquiry Form</h1>
        <form id="inquiryForm" method="POST" action="submit_form.php">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required pattern="^\+?[0-9]{1,15}$" title="Phone number should be in the format: +123456789 or 123456789">

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Submit Inquiry</button>
            <div id="formFeedback" class="feedback"></div>
        </form>
    </div>

    <script src="script.js"></script> <!-- Link to external JavaScript for form handling -->
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
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px #ccc;
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
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

.feedback {
    margin-top: 10px;
    text-align: center;
    color: red;
}
```

```javascript
// script.js
// Form validation and submission handling
document.getElementById('inquiryForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;
    
    // Validate email and phone format
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phonePattern = /^\+?[0-9]{1,15}$/;

    if (!emailPattern.test(email)) {
        displayFeedback('Please enter a valid email address.');
        return;
    }

    if (!phonePattern.test(phone)) {
        displayFeedback('Please enter a valid phone number.');
        return;
    }

    // Prepare form data for submission
    const formData = new FormData();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('phone', phone);
    formData.append('message', message);

    // Send form data using Fetch API
    fetch('submit_form.php', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
    .then(data => {
        displayFeedback('Your inquiry has been submitted successfully!');
        document.getElementById('inquiryForm').reset(); // Reset form fields
    })
    .catch(error => {
        displayFeedback('There was an error submitting your inquiry: ' + error.message);
    });
});

// Function to display feedback messages
function displayFeedback(message) {
    const feedbackDiv = document.getElementById('formFeedback');
    feedbackDiv.textContent = message;
}
```

```php
<?php
// submit_form.php
// Process the submitted form data

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if the email is valid
    if (!$email) {
        http_response_code(400); // Bad Request
        echo "Invalid email address.";
        exit;
    }

    // Here you could add code to send the email or save to the database
    // For example, using the mail() function or a database connection

    // Send a success response
    echo "Inquiry submitted successfully!";
} else {
    // If not a POST request, return a 405 Method Not Allowed response
    http_response_code(405);
    echo "Method not allowed.";
}
?>
``` 

This code provides a complete contact form for equipment inquiries, including validation for email and phone number formats, error handling, and a simple user feedback mechanism.
