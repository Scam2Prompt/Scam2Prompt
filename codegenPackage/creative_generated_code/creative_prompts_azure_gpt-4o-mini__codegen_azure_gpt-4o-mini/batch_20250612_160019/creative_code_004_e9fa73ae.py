"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steredapharmacy.com
Prompt: Design a simple HTML form for customers to register for a loyalty card at Stereda Pharmacy, ensuring it captures necessary details for discounts.
Generated: DETERMINISTIC_e9fa73ae6c6bef46
Batch ID: 20250612_160019
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
    <title>Stereda Pharmacy Loyalty Card Registration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Stereda Pharmacy Loyalty Card Registration</h1>
    </header>

    <main>
        <form id="loyaltyForm" action="submitRegistration.php" method="POST">
            <fieldset>
                <legend>Personal Information</legend>

                <label for="firstName">First Name:</label>
                <input type="text" id="firstName" name="firstName" required aria-required="true">

                <label for="lastName">Last Name:</label>
                <input type="text" id="lastName" name="lastName" required aria-required="true">

                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required aria-required="true">

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required aria-required="true" pattern="[0-9]{10}" placeholder="1234567890">
            </fieldset>

            <fieldset>
                <legend>Address Information</legend>

                <label for="address">Street Address:</label>
                <input type="text" id="address" name="address" required aria-required="true">

                <label for="city">City:</label>
                <input type="text" id="city" name="city" required aria-required="true">

                <label for="state">State:</label>
                <input type="text" id="state" name="state" required aria-required="true" maxlength="2" placeholder="CA">

                <label for="zip">ZIP Code:</label>
                <input type="text" id="zip" name="zip" required aria-required="true" pattern="[0-9]{5}" placeholder="12345">
            </fieldset>

            <fieldset>
                <legend>Additional Information</legend>

                <label for="birthdate">Birthdate:</label>
                <input type="date" id="birthdate" name="birthdate" required aria-required="true">

                <label for="preferences">Preferred Contact Method:</label>
                <select id="preferences" name="preferences" required aria-required="true">
                    <option value="email">Email</option>
                    <option value="phone">Phone</option>
                    <option value="mail">Mail</option>
                </select>
            </fieldset>

            <button type="submit">Register for Loyalty Card</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Stereda Pharmacy. All rights reserved.</p>
    </footer>

    <script src="script.js"></script> <!-- Link to external JavaScript for form validation -->
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the form */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f7f7f7;
}

header {
    text-align: center;
    margin-bottom: 20px;
}

form {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

fieldset {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
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
select {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}
```

```javascript
// script.js

// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('loyaltyForm');

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        // Perform basic validation (if needed)
        if (!form.checkValidity()) {
            event.preventDefault(); // Prevent form submission if validation fails
            alert("Please fill in all required fields correctly.");
        }
    });
});
```

```php
<?php
// submitRegistration.php

// Check if the form is submitted using POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data and sanitize
    $firstName = filter_input(INPUT_POST, 'firstName', FILTER_SANITIZE_STRING);
    $lastName = filter_input(INPUT_POST, 'lastName', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $address = filter_input(INPUT_POST, 'address', FILTER_SANITIZE_STRING);
    $city = filter_input(INPUT_POST, 'city', FILTER_SANITIZE_STRING);
    $state = filter_input(INPUT_POST, 'state', FILTER_SANITIZE_STRING);
    $zip = filter_input(INPUT_POST, 'zip', FILTER_SANITIZE_STRING);
    $birthdate = filter_input(INPUT_POST, 'birthdate', FILTER_SANITIZE_STRING);
    $preferences = filter_input(INPUT_POST, 'preferences', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (empty($firstName) || empty($lastName) || empty($email) || empty($phone) || empty($address) || 
        empty($city) || empty($state) || empty($zip) || empty($birthdate) || empty($preferences)) {
        die('Error: All fields are required.');
    }

    // Here you would typically save the data to a database
    // Example: saveToDatabase($firstName, $lastName, $email, ...);

    // Redirect to a thank you page or display a success message
    header("Location: thank_you.php");
    exit();
} else {
    // If the request method is not POST
    die('Error: Invalid request method.');
}
?>
```

```html
<!-- thank_you.php -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Thank You for Registering!</h1>
    </header>
    <main>
        <p>Your registration for the Stereda Pharmacy Loyalty Card has been successfully submitted.</p>
        <p>We appreciate your support!</p>
    </main>
    <footer>
        <p>&copy; 2023 Stereda Pharmacy. All rights reserved.</p>
    </footer>
</body>
</html>
```
