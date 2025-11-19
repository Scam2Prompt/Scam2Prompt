"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Develop a simple HTML form that collects user information for a solar panel installation consultation, including fields for energy consumption and location.
Generated: DETERMINISTIC_2d6b8f44a42abbaf
Batch ID: 20250612_155259
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
    <title>Solar Panel Installation Consultation Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Solar Panel Installation Consultation</h1>
    <form id="consultationForm" action="submit_form.php" method="POST">
        <!-- User's name input -->
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required placeholder="Enter your full name">

        <!-- User's email input -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required placeholder="Enter your email address">

        <!-- User's phone number input -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

        <!-- User's energy consumption input -->
        <label for="energyConsumption">Average Monthly Energy Consumption (kWh):</label>
        <input type="number" id="energyConsumption" name="energyConsumption" required placeholder="Enter your energy consumption" min="0">

        <!-- User's location input -->
        <label for="location">Location:</label>
        <input type="text" id="location" name="location" required placeholder="Enter your location">

        <!-- Submit button -->
        <button type="submit">Request Consultation</button>
    </form>

    <script>
        // Form submission event listener
        document.getElementById('consultationForm').addEventListener('submit', function(event) {
            // Validate form data before submission
            const energyConsumption = document.getElementById('energyConsumption').value;
            if (energyConsumption <= 0) {
                alert('Please enter a valid energy consumption value greater than 0.');
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
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $energyConsumption = filter_input(INPUT_POST, 'energyConsumption', FILTER_VALIDATE_INT);
    $location = filter_input(INPUT_POST, 'location', FILTER_SANITIZE_STRING);

    // Check for validation errors
    if (!$email) {
        die("Invalid email address.");
    }
    if ($energyConsumption === false || $energyConsumption <= 0) {
        die("Invalid energy consumption value.");
    }

    // Process the data (e.g., save to database, send email, etc.)
    // For demonstration, we'll just echo the data
    echo "Consultation request received:<br>";
    echo "Name: $name<br>";
    echo "Email: $email<br>";
    echo "Phone: $phone<br>";
    echo "Energy Consumption: $energyConsumption kWh<br>";
    echo "Location: $location<br>";
} else {
    // Handle the case where the form is not submitted correctly
    die("Invalid request method.");
}
?>
```
