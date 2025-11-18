"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Generate code to create a web form for scheduling a polygraph test appointment, including fields for selecting test types like fidelity tests, fraud investigations, or legal cases, as mentioned on the Euro Poligraf Center website.
Generated: DETERMINISTIC_6d2cfdc93e535d25
Batch ID: 20250612_153225
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
    <title>Polygraph Test Appointment Scheduling</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript -->
</head>
<body>
    <div class="container">
        <h1>Schedule Your Polygraph Test Appointment</h1>
        <form id="appointmentForm" action="submit_appointment.php" method="POST">
            <!-- Full Name Field -->
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required>

            <!-- Email Field -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <!-- Phone Number Field -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <!-- Test Type Selection -->
            <label for="testType">Select Test Type:</label>
            <select id="testType" name="testType" required>
                <option value="" disabled selected>Select a test type</option>
                <option value="fidelity">Fidelity Test</option>
                <option value="fraud">Fraud Investigation</option>
                <option value="legal">Legal Case</option>
            </select>

            <!-- Appointment Date Field -->
            <label for="date">Select Appointment Date:</label>
            <input type="date" id="date" name="date" required>

            <!-- Submit Button -->
            <button type="submit">Schedule Appointment</button>
        </form>
    </div>
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
    max-width: 600px;
    margin: auto;
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
}

button {
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}
```

```javascript
// script.js

document.getElementById('appointmentForm').addEventListener('submit', function (event) {
    // Perform client-side validation before submission
    const fullName = document.getElementById('fullName').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const testType = document.getElementById('testType').value;
    const date = document.getElementById('date').value;

    // Check if all fields are filled
    if (!fullName || !email || !phone || !testType || !date) {
        alert('Please fill in all fields.');
        event.preventDefault(); // Prevent form submission
        return;
    }

    // Add logic for further validation if needed

    // Log to console (for debugging purposes)
    console.log('Form submitted successfully.');
});
```

```php
<?php
// submit_appointment.php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Capture form inputs
    $fullName = $_POST['fullName'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $testType = $_POST['testType'];
    $date = $_POST['date'];

    // Validate inputs (simple validation)
    if (empty($fullName) || empty($email) || empty($phone) || empty($testType) || empty($date)) {
        die('All fields are required.');
    }

    // Prepare data for storage (e.g. database)
    // Here you would typically insert the data into a database
    // Example: insertAppointment($fullName, $email, $phone, $testType, $date);

    // Respond to user
    echo "Appointment scheduled successfully for $fullName on $date for a $testType test.";
} else {
    // Handle incorrect request method
    http_response_code(405);
    echo "Method Not Allowed";
}
?>
```
