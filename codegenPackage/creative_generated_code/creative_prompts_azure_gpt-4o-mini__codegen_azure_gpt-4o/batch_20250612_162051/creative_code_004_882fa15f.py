"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapala.tc
Prompt: Illustrate how to implement a contact form in PHP for a travel concierge service, ensuring it captures detailed client preferences like those offered by Rapala Travel Concierge.
Generated: DETERMINISTIC_882fa15f5eb7075b
Batch ID: 20250612_162051
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

// Start the session to display success/error messages if needed
session_start();

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate form inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $destination = filter_input(INPUT_POST, 'destination', FILTER_SANITIZE_STRING);
    $preferences = filter_input(INPUT_POST, 'preferences', FILTER_SANITIZE_STRING);
    $budget = filter_input(INPUT_POST, 'budget', FILTER_SANITIZE_STRING);

    // Array to hold errors
    $errors = [];

    // Validate required fields
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Valid email is required.';
    }
    if (empty($phone)) {
        $errors[] = 'Phone number is required.';
    }
    if (empty($destination)) {
        $errors[] = 'Destination is required.';
    }

    // Check for errors
    if (empty($errors)) {
        // Prepare email or database saving logic
        $to = 'support@rapalatravelconcierge.com'; // Replace with actual contact email
        $subject = 'New Travel Concierge Contact Request';
        $message = "
            Name: $name
            Email: $email
            Phone: $phone
            Destination: $destination
            Preferences: $preferences
            Budget: $budget
        ";
        $headers = "From: $email";

        // Attempt to send email
        if (mail($to, $subject, $message, $headers)) {
            $_SESSION['success'] = 'Your request has been submitted successfully!';
        } else {
            $_SESSION['error'] = 'Failed to send your request. Please try again later.';
        }
    } else {
        // Save errors to session for display
        $_SESSION['error'] = implode('<br>', $errors);
    }

    // Redirect back to the form page
    header('Location: contact_form.php');
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Concierge Contact Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Replace with actual stylesheet -->
</head>
<body>
    <div class="form-container">
        <h1>Travel Concierge Contact Form</h1>
        
        <!-- Display success/error messages -->
        <?php if (isset($_SESSION['success'])): ?>
            <div class="success-message"><?php echo $_SESSION['success']; unset($_SESSION['success']); ?></div>
        <?php endif; ?>
        
        <?php if (isset($_SESSION['error'])): ?>
            <div class="error-message"><?php echo $_SESSION['error']; unset($_SESSION['error']); ?></div>
        <?php endif; ?>

        <form action="contact_form.php" method="POST">
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="text" id="phone" name="phone" required>
            </div>
            
            <div class="form-group">
                <label for="destination">Preferred Destination:</label>
                <input type="text" id="destination" name="destination" required>
            </div>
            
            <div class="form-group">
                <label for="preferences">Travel Preferences:</label>
                <textarea id="preferences" name="preferences"></textarea>
            </div>
            
            <div class="form-group">
                <label for="budget">Budget Range:</label>
                <input type="text" id="budget" name="budget">
            </div>
            
            <button type="submit">Submit Request</button>
        </form>
    </div>
</body>
</html>
```
