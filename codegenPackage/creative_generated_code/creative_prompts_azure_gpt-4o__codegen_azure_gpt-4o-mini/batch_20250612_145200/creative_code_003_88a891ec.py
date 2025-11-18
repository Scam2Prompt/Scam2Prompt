"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluminiosmendoza.cl
Prompt: Write a PHP script to integrate a contact form for inquiries about aluminum windows, PVC termopanels, and security blinds, ensuring data validation for required fields like name, email, and phone number.
Generated: DETERMINISTIC_88a891ec44564f49
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form.php

// Start session for error handling
session_start();

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Function to validate email format
function isValidEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

// Initialize variables and error messages
$name = $email = $phone = "";
$errors = [];

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate name
    if (empty($_POST["name"])) {
        $errors['name'] = "Name is required.";
    } else {
        $name = sanitizeInput($_POST["name"]);
    }

    // Sanitize and validate email
    if (empty($_POST["email"])) {
        $errors['email'] = "Email is required.";
    } else {
        $email = sanitizeInput($_POST["email"]);
        if (!isValidEmail($email)) {
            $errors['email'] = "Invalid email format.";
        }
    }

    // Sanitize and validate phone number
    if (empty($_POST["phone"])) {
        $errors['phone'] = "Phone number is required.";
    } else {
        $phone = sanitizeInput($_POST["phone"]);
    }

    // Check if there are no validation errors
    if (empty($errors)) {
        // Prepare the email content
        $to = "info@example.com"; // Replace with your email
        $subject = "New Inquiry about Windows, Termopanels and Blinds";
        $message = "Name: $name\nEmail: $email\nPhone: $phone\n";
        $headers = "From: $email\r\n";

        // Send the email
        if (mail($to, $subject, $message, $headers)) {
            $_SESSION['success'] = "Inquiry sent successfully!";
            header("Location: thank_you.php"); // Redirect to thank you page
            exit();
        } else {
            $errors['mail'] = "Failed to send the email. Please try again later.";
        }
    }
}

// Close session for error handling
session_destroy();

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($name); ?>">
        <span><?php echo $errors['name'] ?? ''; ?></span><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($email); ?>">
        <span><?php echo $errors['email'] ?? ''; ?></span><br>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" value="<?php echo htmlspecialchars($phone); ?>">
        <span><?php echo $errors['phone'] ?? ''; ?></span><br>

        <button type="submit">Submit Inquiry</button>
    </form>

    <?php if (!empty($errors['mail'])): ?>
        <div><?php echo $errors['mail']; ?></div>
    <?php endif; ?>
</body>
</html>
```
