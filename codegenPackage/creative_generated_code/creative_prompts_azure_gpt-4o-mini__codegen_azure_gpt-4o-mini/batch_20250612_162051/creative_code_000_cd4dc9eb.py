"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isbgames.isbeventteam.com
Prompt: Generate a registration form for participants in the ISB Games 2024, including fields for team name, sport selection (Obstacle Run, Football, Basketball, Bowling), and contact information.
Generated: DETERMINISTIC_cd4dc9eb82840e9e
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
    <title>ISB Games 2024 Registration Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <div class="container">
        <h1>ISB Games 2024 Registration Form</h1>
        <form id="registrationForm" action="submit_registration.php" method="POST" novalidate>
            <!-- Team Name Input -->
            <div class="form-group">
                <label for="teamName">Team Name:</label>
                <input type="text" id="teamName" name="teamName" required>
                <small class="error-message" id="teamNameError"></small>
            </div>

            <!-- Sport Selection Input -->
            <div class="form-group">
                <label for="sport">Select Sport:</label>
                <select id="sport" name="sport" required>
                    <option value="" disabled selected>Select your sport</option>
                    <option value="Obstacle Run">Obstacle Run</option>
                    <option value="Football">Football</option>
                    <option value="Basketball">Basketball</option>
                    <option value="Bowling">Bowling</option>
                </select>
                <small class="error-message" id="sportError"></small>
            </div>

            <!-- Contact Information Input -->
            <div class="form-group">
                <label for="contactInfo">Contact Information:</label>
                <input type="text" id="contactInfo" name="contactInfo" required pattern="[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}" title="Please enter a valid email address">
                <small class="error-message" id="contactInfoError"></small>
            </div>

            <!-- Submit Button -->
            <button type="submit">Register</button>
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
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
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

input, select {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}

.error-message {
    color: red;
    font-size: 0.8em;
}
```

```javascript
// script.js
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    let valid = true;

    // Clear previous error messages
    document.getElementById('teamNameError').textContent = '';
    document.getElementById('sportError').textContent = '';
    document.getElementById('contactInfoError').textContent = '';

    // Validate Team Name
    const teamName = document.getElementById('teamName').value;
    if (teamName.trim() === '') {
        document.getElementById('teamNameError').textContent = 'Team name is required.';
        valid = false;
    }

    // Validate Sport Selection
    const sport = document.getElementById('sport').value;
    if (sport === '') {
        document.getElementById('sportError').textContent = 'Please select a sport.';
        valid = false;
    }

    // Validate Contact Information
    const contactInfo = document.getElementById('contactInfo').value;
    const emailPattern = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$/;
    if (!emailPattern.test(contactInfo)) {
        document.getElementById('contactInfoError').textContent = 'Please enter a valid email address.';
        valid = false;
    }

    // If validation fails, prevent form submission
    if (!valid) {
        event.preventDefault();
    }
});
``` 

```php
<?php
// submit_registration.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize inputs
    $teamName = filter_input(INPUT_POST, 'teamName', FILTER_SANITIZE_STRING);
    $sport = filter_input(INPUT_POST, 'sport', FILTER_SANITIZE_STRING);
    $contactInfo = filter_input(INPUT_POST, 'contactInfo', FILTER_SANITIZE_EMAIL);

    // Check for empty fields
    if (empty($teamName) || empty($sport) || !filter_var($contactInfo, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad Request
        die('Invalid input provided.');
    }

    // Here you would typically save the data to a database or send an email
    // Example: Save to a database (use prepared statements in production)

    // Provide feedback to the user
    echo "Registration successful for team: $teamName in sport: $sport. Contact: $contactInfo";
} else {
    http_response_code(405); // Method Not Allowed
    die('Invalid request method.');
}
?> 
```
