"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Write a PHP script to send a callback request form submission, including fields for "Name" and "Telephone," as seen on the Health Insurance Shop website.
Generated: DETERMINISTIC_895a53462d8e64d4
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Callback request form submission script

// Define variables for form fields
$name = '';
$telephone = '';

// Define an array to hold error messages
$errors = [];

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    
    // Validate and sanitize the name input
    if (isset($_POST['name']) && !empty(trim($_POST['name']))) {
        $name = htmlspecialchars(trim($_POST['name']));
    } else {
        $errors[] = "Name is required.";
    }

    // Validate and sanitize the telephone input
    if (isset($_POST['telephone']) && !empty(trim($_POST['telephone']))) {
        $telephone = htmlspecialchars(trim($_POST['telephone']));
        
        // Check if the telephone number is valid (basic validation example)
        if (!preg_match('/^\+?[0-9]*$/', $telephone)) {
            $errors[] = "Invalid telephone number format.";
        }
    } else {
        $errors[] = "Telephone is required.";
    }

    // If there are no errors, proceed to send the callback request
    if (empty($errors)) {
        // Prepare the email parameters
        $to = "info@healthinsuranceshop.com"; // Replace with your email address
        $subject = "Callback Request from: $name";
        $message = "Name: $name\nTelephone: $telephone";
        $headers = "From: noreply@healthinsuranceshop.com"; // Replace with your domain
        
        // Send the email
        if (mail($to, $subject, $message, $headers)) {
            // Output success message
            echo "Callback request sent successfully. We will contact you shortly.";
        } else {
            // Output error message if email sending fails
            echo "There was an error sending your callback request. Please try again later.";
        }
    } else {
        // Output the error messages
        foreach ($errors as $error) {
            echo "<p>Error: $error</p>";
        }
    }
}
?>

<!-- HTML form for callback request -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Callback Request Form</title>
</head>
<body>
    <h2>Request a Callback</h2>
    <form action="" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="telephone">Telephone:</label>
        <input type="tel" id="telephone" name="telephone" required>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
