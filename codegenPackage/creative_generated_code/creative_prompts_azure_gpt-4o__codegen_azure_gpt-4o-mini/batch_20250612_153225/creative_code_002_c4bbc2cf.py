"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Generate code to create a web form for vehicle renting inquiries, including fields for personal/business details, vehicle preferences, and contact information, as described on the Innova Renting website.
Generated: DETERMINISTIC_c4bbc2cf3f0a64f2
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
    <title>Vehicle Renting Inquiry Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Vehicle Renting Inquiry Form</h1>
    <form id="rentalInquiryForm" method="POST" action="submit_form.php" onsubmit="return validateForm()">
        <!-- Personal/Business Details Section -->
        <fieldset>
            <legend>Personal/Business Details</legend>
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="businessName">Business Name (if applicable):</label>
            <input type="text" id="businessName" name="businessName">
        </fieldset>

        <!-- Vehicle Preferences Section -->
        <fieldset>
            <legend>Vehicle Preferences</legend>
            <label for="vehicleType">Preferred Vehicle Type:</label>
            <select id="vehicleType" name="vehicleType" required>
                <option value="">--Select Vehicle Type--</option>
                <option value="sedan">Sedan</option>
                <option value="suv">SUV</option>
                <option value="truck">Truck</option>
                <option value="van">Van</option>
            </select>

            <label for="rentalDuration">Rental Duration (days):</label>
            <input type="number" id="rentalDuration" name="rentalDuration" min="1" required>

            <label for="pickupLocation">Pickup Location:</label>
            <input type="text" id="pickupLocation" name="pickupLocation" required>
        </fieldset>

        <!-- Contact Information Section -->
        <fieldset>
            <legend>Contact Information</legend>
            <label for="preferredContactMethod">Preferred Contact Method:</label>
            <select id="preferredContactMethod" name="preferredContactMethod" required>
                <option value="phone">Phone</option>
                <option value="email">Email</option>
            </select>

            <label for="message">Additional Message:</label>
            <textarea id="message" name="message" rows="4"></textarea>
        </fieldset>

        <!-- Submit Button -->
        <button type="submit">Submit Inquiry</button>
    </form>

    <script>
        /**
         * Validates the rental inquiry form before submission.
         * @returns {boolean} True if the form is valid, false otherwise.
         */
        function validateForm() {
            // Perform additional client-side validation if necessary
            const form = document.getElementById('rentalInquiryForm');
            if (form.checkValidity()) {
                return true;
            } else {
                alert('Please fill out all required fields correctly.');
                return false;
            }
        }
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $fullName = filter_input(INPUT_POST, 'fullName', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $businessName = filter_input(INPUT_POST, 'businessName', FILTER_SANITIZE_STRING);
    $vehicleType = filter_input(INPUT_POST, 'vehicleType', FILTER_SANITIZE_STRING);
    $rentalDuration = filter_input(INPUT_POST, 'rentalDuration', FILTER_SANITIZE_NUMBER_INT);
    $pickupLocation = filter_input(INPUT_POST, 'pickupLocation', FILTER_SANITIZE_STRING);
    $preferredContactMethod = filter_input(INPUT_POST, 'preferredContactMethod', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if the email is valid
    if (!$email) {
        die("Invalid email format.");
    }

    // Process the inquiry (e.g., save to database, send email, etc.)
    try {
        // Here you would typically save the data to a database or send an email.
        // For demonstration purposes, we're just echoing the data.
        echo "<h1>Inquiry Submitted!</h1>";
        echo "<p>Thank you, $fullName! Your inquiry has been received.</p>";
        // Optionally, you could add code to send an email here.
    } catch (Exception $e) {
        // Handle any exceptions
        die("Error processing the inquiry: " . $e->getMessage());
    }
} else {
    // If the request method is not POST, redirect to the form
    header("Location: index.html");
    exit();
}
?>
``` 

This code includes both the HTML for the inquiry form and the PHP script to handle the form submission. It ensures proper validation and sanitization of input, error handling, and a clean structure for both client and server-side code.
