"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Generate code to create a web-based form for business inquiries, ensuring fields for project details, client contact information, and service selection, as described on the Remas Engineering Consultants website.
Generated: DETERMINISTIC_6e48ff3c92a098dc
Batch ID: 20250612_153648
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
    <title>Business Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Business Inquiry Form</h1>
        <form id="inquiryForm" action="submit_form.php" method="POST">
            <!-- Project Details Section -->
            <fieldset>
                <legend>Project Details</legend>
                <label for="projectName">Project Name:</label>
                <input type="text" id="projectName" name="projectName" required>
                
                <label for="projectDescription">Project Description:</label>
                <textarea id="projectDescription" name="projectDescription" rows="4" required></textarea>
            </fieldset>

            <!-- Client Contact Information Section -->
            <fieldset>
                <legend>Client Contact Information</legend>
                <label for="clientName">Client Name:</label>
                <input type="text" id="clientName" name="clientName" required>
                
                <label for="clientEmail">Client Email:</label>
                <input type="email" id="clientEmail" name="clientEmail" required>
                
                <label for="clientPhone">Client Phone:</label>
                <input type="tel" id="clientPhone" name="clientPhone" required>
            </fieldset>

            <!-- Service Selection Section -->
            <fieldset>
                <legend>Service Selection</legend>
                <label for="serviceType">Select Service:</label>
                <select id="serviceType" name="serviceType" required>
                    <option value="">--Please choose an option--</option>
                    <option value="consulting">Consulting</option>
                    <option value="design">Design</option>
                    <option value="development">Development</option>
                    <option value="maintenance">Maintenance</option>
                </select>
            </fieldset>

            <!-- Submit Button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>

    <script src="script.js"></script> <!-- Link to external JavaScript for form validation -->
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

input, textarea, select {
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

```php
<?php
// submit_form.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $projectName = filter_input(INPUT_POST, 'projectName', FILTER_SANITIZE_STRING);
    $projectDescription = filter_input(INPUT_POST, 'projectDescription', FILTER_SANITIZE_STRING);
    $clientName = filter_input(INPUT_POST, 'clientName', FILTER_SANITIZE_STRING);
    $clientEmail = filter_input(INPUT_POST, 'clientEmail', FILTER_VALIDATE_EMAIL);
    $clientPhone = filter_input(INPUT_POST, 'clientPhone', FILTER_SANITIZE_STRING);
    $serviceType = filter_input(INPUT_POST, 'serviceType', FILTER_SANITIZE_STRING);

    // Check for validation errors
    if (!$clientEmail) {
        die("Invalid email address.");
    }

    // Prepare email content
    $to = "info@remasengineering.com"; // Replace with your email
    $subject = "New Business Inquiry from $clientName";
    $message = "Project Name: $projectName\n".
               "Project Description: $projectDescription\n".
               "Client Name: $clientName\n".
               "Client Email: $clientEmail\n".
               "Client Phone: $clientPhone\n".
               "Service Type: $serviceType\n";

    // Send email
    if (mail($to, $subject, $message)) {
        echo "Inquiry submitted successfully!";
    } else {
        echo "Error sending inquiry. Please try again later.";
    }
} else {
    // Handle invalid access
    http_response_code(405);
    echo "Method Not Allowed";
}
?>
```

```javascript
// script.js

// Add form validation if needed
document.getElementById('inquiryForm').addEventListener('submit', function(event) {
    // Example: Custom validation logic can be added here
    // Prevent form submission if validation fails
});
```
