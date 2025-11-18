"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enjin.pro
Prompt: Generate PHP code to create a contact form for car inquiries, including fields for name, email, phone number, and specific car details, similar to the "お問い合わせ" section on the "縁陣 -ENJIN-" website.
Generated: DETERMINISTIC_35967c030d20d03e
Batch ID: 20250612_145300
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

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input
    $name = htmlspecialchars(trim($_POST['name']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $phone = htmlspecialchars(trim($_POST['phone']));
    $carDetails = htmlspecialchars(trim($_POST['car_details']));

    // Error messages array
    $errors = [];

    // Validate name
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }

    // Validate email
    if (empty($email)) {
        $errors[] = 'A valid email is required.';
    }

    // Validate phone number
    if (empty($phone)) {
        $errors[] = 'Phone number is required.';
    }

    // Validate car details
    if (empty($carDetails)) {
        $errors[] = 'Car details are required.';
    }

    // If no errors, process the form
    if (empty($errors)) {
        // Example: Send email or save to the database
        $to = 'contact@example.com'; // Replace with the recipient's email address
        $subject = 'Car Inquiry Contact Form Submission';
        $message = "Name: $name\nEmail: $email\nPhone: $phone\nCar Details: $carDetails";
        $headers = "From: $email";

        if (mail($to, $subject, $message, $headers)) {
            $successMessage = 'Your inquiry has been successfully sent!';
        } else {
            $errors[] = 'Failed to send the inquiry. Please try again later.';
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Inquiry Contact Form</title>
</head>
<body>
    <h1>Car Inquiry Contact Form</h1>

    <!-- Display errors if any -->
    <?php if (!empty($errors)): ?>
        <div style="color: red;">
            <ul>
                <?php foreach ($errors as $error): ?>
                    <li><?php echo $error; ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
    <?php endif; ?>

    <!-- Display success message -->
    <?php if (!empty($successMessage)): ?>
        <div style="color: green;">
            <p><?php echo $successMessage; ?></p>
        </div>
    <?php endif; ?>

    <!-- Contact Form -->
    <form method="POST" action="">
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div>
            <label for="phone">Phone Number:</label>
            <input type="text" id="phone" name="phone" required>
        </div>
        <div>
            <label for="car_details">Car Details:</label>
            <textarea id="car_details" name="car_details" required></textarea>
        </div>
        <button type="submit">Submit Inquiry</button>
    </form>
</body>
</html>
```
