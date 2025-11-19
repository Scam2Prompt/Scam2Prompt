"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govssc.edu.bd
Prompt: Generate a code snippet for an online form that allows students to fill out their admission forms for the 2024 Honors first year at Govt. Shah Sultan College, Bogura.
Generated: DETERMINISTIC_4c587036530b2e7e
Batch ID: 20250612_164214
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
    <title>Admission Form - Govt. Shah Sultan College, Bogura</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <div class="container">
        <h1>Admission Form for 2024 Honors First Year</h1>
        <form id="admissionForm" action="submit_form.php" method="POST">
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required placeholder="Enter your full name">

            <label for="dob">Date of Birth:</label>
            <input type="date" id="dob" name="dob" required>

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

            <label for="address">Permanent Address:</label>
            <textarea id="address" name="address" required placeholder="Enter your permanent address"></textarea>

            <label for="subject">Desired Subject:</label>
            <select id="subject" name="subject" required>
                <option value="" disabled selected>Select your subject</option>
                <option value="Mathematics">Mathematics</option>
                <option value="Physics">Physics</option>
                <option value="Chemistry">Chemistry</option>
                <option value="Biology">Biology</option>
                <option value="Computer Science">Computer Science</option>
            </select>

            <label for="agree">
                <input type="checkbox" id="agree" name="agree" required>
                I agree to the terms and conditions
            </label>

            <button type="submit">Submit Application</button>
        </form>
    </div>

    <script src="script.js"></script> <!-- Link to external JavaScript file -->
</body>
</html>
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
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    max-width: 600px;
    margin: auto;
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, textarea, select {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```

```javascript
// script.js
document.getElementById('admissionForm').addEventListener('submit', function(event) {
    // Basic form validation
    const fullName = document.getElementById('fullName').value;
    const email = document.getElementById('email').value;

    // Check if name and email are valid
    if (fullName.trim() === "" || !validateEmail(email)) {
        alert("Please fill out the form correctly.");
        event.preventDefault(); // Stop form submission
    }
});

// Function to validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
```

```php
<?php
// submit_form.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate inputs
    $fullName = filter_input(INPUT_POST, 'fullName', FILTER_SANITIZE_STRING);
    $dob = filter_input(INPUT_POST, 'dob', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $address = filter_input(INPUT_POST, 'address', FILTER_SANITIZE_STRING);
    $subject = filter_input(INPUT_POST, 'subject', FILTER_SANITIZE_STRING);
    $agree = filter_input(INPUT_POST, 'agree', FILTER_SANITIZE_STRING);

    // Check for required fields
    if (!$fullName || !$dob || !$email || !$phone || !$address || !$subject || !$agree) {
        http_response_code(400);
        echo "Please fill all required fields.";
        exit;
    }

    // Here you can add code to save the data to a database or send an email

    // Return a success response
    echo "Application submitted successfully!";
} else {
    http_response_code(405);
    echo "Method not allowed.";
}
?> 
```
