"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Write a PHP script to integrate a real estate inquiry form for properties in Hurghada, El Gouna, and Sahl Hasheesh, using fields like property type, location, and budget as described on sunnyhurghada.com.
Generated: DETERMINISTIC_70046b56ef79884d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// real_estate_inquiry.php

// Ensure proper error reporting during development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user input
    $propertyType = sanitizeInput($_POST['property_type'] ?? '');
    $location = sanitizeInput($_POST['location'] ?? '');
    $budget = sanitizeInput($_POST['budget'] ?? '');
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $message = sanitizeInput($_POST['message'] ?? '');

    // Validate required fields
    $errors = [];
    if (empty($propertyType)) {
        $errors[] = "Property type is required.";
    }
    if (empty($location)) {
        $errors[] = "Location is required.";
    }
    if (empty($budget)) {
        $errors[] = "Budget is required.";
    }
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Valid email is required.";
    }

    // If there are no errors, process the inquiry
    if (empty($errors)) {
        // Example: Sending an email (modify as needed for your environment)
        $to = "contact@sunnyhurghada.com"; // Replace with your own email address
        $subject = "Real Estate Inquiry from $name";
        $body = "Property Type: $propertyType\nLocation: $location\nBudget: $budget\n\nMessage:\n$message";
        $headers = "From: $email";

        if (mail($to, $subject, $body, $headers)) {
            $successMessage = "Your inquiry has been successfully submitted. We will get back to you shortly.";
        } else {
            $errors[] = "Failed to send your inquiry. Please try again later.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real Estate Inquiry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        .error {
            color: red;
        }
        .success {
            color: green;
        }
    </style>
</head>
<body>

<h1>Real Estate Inquiry Form</h1>

<?php
// Display success message or errors
if (!empty($successMessage)) {
    echo "<p class='success'>$successMessage</p>";
}
if (!empty($errors)) {
    echo "<ul class='error'>";
    foreach ($errors as $error) {
        echo "<li>$error</li>";
    }
    echo "</ul>";
}
?>

<form action="" method="POST">
    <div class="form-group">
        <label for="property_type">Property Type:</label>
        <select name="property_type" id="property_type" required>
            <option value="">Select a property type</option>
            <option value="Apartment">Apartment</option>
            <option value="Villa">Villa</option>
            <option value="Studio">Studio</option>
        </select>
    </div>
    <div class="form-group">
        <label for="location">Location:</label>
        <select name="location" id="location" required>
            <option value="">Select a location</option>
            <option value="Hurghada">Hurghada</option>
            <option value="El Gouna">El Gouna</option>
            <option value="Sahl Hasheesh">Sahl Hasheesh</option>
        </select>
    </div>
    <div class="form-group">
        <label for="budget">Budget:</label>
        <input type="number" name="budget" id="budget" required>
    </div>
    <div class="form-group">
        <label for="name">Your Name:</label>
        <input type="text" name="name" id="name" required>
    </div>
    <div class="form-group">
        <label for="email">Your Email:</label>
        <input type="email" name="email" id="email" required>
    </div>
    <div class="form-group">
        <label for="message">Additional Message:</label>
        <textarea name="message" id="message" rows="4"></textarea>
    </div>
    <button type="submit">Submit Inquiry</button>
</form>

</body>
</html>
```
